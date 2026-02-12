"""
Content Agent for Rising Sun Digital
Fetches trending topics and generates blog post ideas without duplicates.

Requirements:
    pip install pytrends anthropic python-dotenv

Usage:
    python content-agent.py                    # Fetch trends and show ideas
    python content-agent.py --generate         # Generate draft content
    python content-agent.py --category hvac    # Filter by category
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

# Optional imports - will work without them for manual mode
try:
    from pytrends.request import TrendReq
    PYTRENDS_AVAILABLE = True
except ImportError:
    PYTRENDS_AVAILABLE = False
    print("Note: pytrends not installed. Run: pip install pytrends")

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Note: anthropic not installed. Run: pip install anthropic")

# Configuration
BASE_DIR = Path(__file__).parent.parent
MANIFEST_PATH = BASE_DIR / "content-manifest.json"
DRAFTS_DIR = BASE_DIR / "blog" / "drafts"
BLOG_DIR = BASE_DIR / "blog"

# Home service keywords to filter trends
NICHE_KEYWORDS = [
    "plumber", "plumbing", "hvac", "air conditioning", "heating", "cooling",
    "electrician", "electrical", "wiring", "roofing", "roofer", "roof repair",
    "contractor", "home repair", "handyman", "remodel", "renovation",
    "car detailing", "auto detailing", "detailer",
    "home service", "local business", "small business marketing",
    "google ads", "seo", "local seo", "lead generation", "marketing"
]

# Categories mapping
CATEGORY_MAP = {
    "hvac": ["hvac", "air conditioning", "heating", "cooling", "furnace", "ac repair"],
    "plumbers": ["plumber", "plumbing", "pipe", "drain", "water heater", "leak"],
    "electricians": ["electrician", "electrical", "wiring", "panel", "outlet", "ev charger"],
    "roofers": ["roof", "roofing", "roofer", "shingle", "gutter"],
    "detailing": ["detailing", "car detail", "auto detail", "ceramic coating", "paint correction"],
    "contractors": ["contractor", "remodel", "renovation", "handyman", "home repair"],
    "local": ["local", "near me", "city", "area"],
    "strategy": ["marketing", "ads", "seo", "lead", "budget", "roi"]
}


def load_manifest():
    """Load the content manifest."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, 'r') as f:
            return json.load(f)
    return {"posts": [], "pillarPages": []}


def save_manifest(manifest):
    """Save the content manifest."""
    manifest["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")
    with open(MANIFEST_PATH, 'w') as f:
        json.dump(manifest, f, indent=2)


def get_existing_topics(manifest):
    """Extract all existing topics and keywords from manifest."""
    existing = set()
    for post in manifest.get("posts", []):
        existing.add(post["slug"].lower())
        existing.add(post["title"].lower())
        for topic in post.get("topics", []):
            existing.add(topic.lower())
        for kw in post.get("keywords", []):
            existing.add(kw.lower())
    return existing


def is_duplicate(query, existing_topics, threshold=0.6):
    """Check if a query is too similar to existing content."""
    query_lower = query.lower()
    query_words = set(query_lower.split())

    # Guard against empty query
    if not query_words:
        return False

    for existing in existing_topics:
        existing_words = set(existing.split())
        # Skip empty existing topics
        if not existing_words:
            continue
        overlap = len(query_words & existing_words) / max(len(query_words), len(existing_words))
        if overlap > threshold:
            return True
        if query_lower in existing or existing in query_lower:
            return True
    return False


def categorize_query(query):
    """Determine which category a query belongs to."""
    query_lower = query.lower()
    scores = {}

    for category, keywords in CATEGORY_MAP.items():
        score = sum(1 for kw in keywords if kw in query_lower)
        if score > 0:
            scores[category] = score

    if scores:
        return max(scores, key=scores.get)
    return "strategy"  # Default category


def fetch_google_trends(keywords=None):
    """Fetch trending topics from Google Trends."""
    if not PYTRENDS_AVAILABLE:
        print("pytrends not available. Using sample trends.")
        return get_sample_trends()

    pytrends = TrendReq(hl='en-US', tz=360)
    trending_queries = []

    # Search terms to check
    search_terms = keywords or [
        "plumber marketing",
        "hvac leads",
        "contractor advertising",
        "electrician marketing",
        "roofing leads",
        "local service ads",
        "google ads contractors"
    ]

    for term in search_terms:
        try:
            pytrends.build_payload([term], cat=0, timeframe='now 7-d', geo='US')
            related = pytrends.related_queries()

            if term in related and related[term]['rising'] is not None:
                rising = related[term]['rising']
                for _, row in rising.head(5).iterrows():
                    query = row['query']
                    if any(kw in query.lower() for kw in NICHE_KEYWORDS):
                        trending_queries.append({
                            "query": query,
                            "source_term": term,
                            "type": "rising"
                        })

            if term in related and related[term]['top'] is not None:
                top = related[term]['top']
                for _, row in top.head(3).iterrows():
                    query = row['query']
                    if any(kw in query.lower() for kw in NICHE_KEYWORDS):
                        trending_queries.append({
                            "query": query,
                            "source_term": term,
                            "type": "top"
                        })
        except Exception as e:
            print(f"Error fetching trends for '{term}': {e}")
            continue

    return trending_queries


def get_sample_trends():
    """Sample trends for testing without API."""
    return [
        {"query": "hvac marketing ideas 2026", "source_term": "hvac", "type": "rising"},
        {"query": "best crm for plumbers", "source_term": "plumber", "type": "rising"},
        {"query": "google local service ads electricians", "source_term": "electrician", "type": "rising"},
        {"query": "roofing company seo tips", "source_term": "roofing", "type": "top"},
        {"query": "contractor website must haves", "source_term": "contractor", "type": "rising"},
        {"query": "how to get more reviews plumbing", "source_term": "plumber", "type": "rising"},
        {"query": "hvac seasonal marketing", "source_term": "hvac", "type": "top"},
        {"query": "electrician google ads cost", "source_term": "electrician", "type": "rising"},
    ]


def generate_content_ideas(trends, existing_topics, category_filter=None):
    """Filter trends and generate content ideas."""
    ideas = []
    seen_queries = set()  # Track queries to prevent duplicates

    for trend in trends:
        query = trend["query"]
        query_lower = query.lower()

        # Skip if we've already seen this query
        if query_lower in seen_queries:
            continue
        seen_queries.add(query_lower)

        category = categorize_query(query)

        # Apply category filter if specified
        if category_filter and category != category_filter:
            continue

        # Skip duplicates against existing content
        if is_duplicate(query, existing_topics):
            continue

        # Generate title suggestion
        title = query.title()
        if not any(word in title.lower() for word in ["how", "what", "why", "best", "top"]):
            title = f"How to {title}" if "marketing" in query.lower() else f"The Truth About {title}"

        ideas.append({
            "query": query,
            "suggested_title": title,
            "category": category,
            "source": trend["source_term"],
            "trend_type": trend["type"]
        })

    return ideas


def generate_draft_with_claude(idea, manifest):
    """Generate a blog post draft using Claude API."""
    if not ANTHROPIC_AVAILABLE:
        return generate_template_draft(idea)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set. Using template draft.")
        return generate_template_draft(idea)

    client = anthropic.Anthropic(api_key=api_key)

    # Get existing post titles for context
    existing_titles = [p["title"] for p in manifest.get("posts", [])]

    prompt = f"""Write a blog post for Rising Sun Digital, a digital marketing agency for home service businesses.

Topic: {idea['query']}
Suggested Title: {idea['suggested_title']}
Category: {idea['category']}

IMPORTANT RULES:
1. Write in a calm, analytical tone - no hype or pushy language
2. Be honest about trade-offs and when things DON'T work
3. Include specific, actionable advice
4. Keep it 800-1200 words
5. Use subheadings for easy scanning
6. End with a soft CTA mentioning Rising Sun Digital

EXISTING POSTS (don't repeat these topics):
{chr(10).join(f'- {t}' for t in existing_titles[:10])}

Write the blog post in HTML format with proper semantic markup (h2, h3, p, ul tags).
Start with a brief intro, then dive into the content. No fluff."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        # Validate response before accessing
        if message.content and len(message.content) > 0 and hasattr(message.content[0], 'text'):
            return message.content[0].text
        else:
            print("Unexpected API response format. Using template draft.")
            return generate_template_draft(idea)
    except Exception as e:
        print(f"Claude API error: {e}")
        return generate_template_draft(idea)


def generate_template_draft(idea):
    """Generate a template draft without AI."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{idea['suggested_title']} | Rising Sun Digital</title>
    <meta name="description" content="[WRITE META DESCRIPTION - 150-160 chars]">
</head>
<body>
    <article>
        <h1>{idea['suggested_title']}</h1>

        <p><strong>Category:</strong> {idea['category'].title()}</p>
        <p><strong>Based on trending query:</strong> {idea['query']}</p>
        <p><strong>Trend type:</strong> {idea['trend_type']}</p>

        <h2>Introduction</h2>
        <p>[Write 2-3 sentences introducing the topic and why it matters to {idea['category']} businesses]</p>

        <h2>The Problem</h2>
        <p>[Describe the challenge or question this post addresses]</p>

        <h2>What Actually Works</h2>
        <p>[Provide specific, actionable advice]</p>
        <ul>
            <li>[Point 1]</li>
            <li>[Point 2]</li>
            <li>[Point 3]</li>
        </ul>

        <h2>Common Mistakes to Avoid</h2>
        <p>[List 2-3 mistakes and why they happen]</p>

        <h2>The Bottom Line</h2>
        <p>[Summarize key takeaways in 2-3 sentences]</p>

        <hr>
        <p><em>Need help implementing this for your {idea['category']} business?
        <a href="/#booking">Book a free strategy call</a> with Rising Sun Digital.</em></p>
    </article>
</body>
</html>
"""


def save_draft(idea, content):
    """Save a draft to the drafts folder."""
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

    # Generate filename from title
    slug = re.sub(r'[^a-z0-9]+', '-', idea['suggested_title'].lower()).strip('-')
    date_prefix = datetime.now().strftime("%Y%m%d")
    filename = f"{date_prefix}-{slug}.html"

    filepath = DRAFTS_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Content Agent for Rising Sun Digital")
    parser.add_argument("--generate", action="store_true", help="Generate draft content")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument("--sample", action="store_true", help="Use sample trends (no API)")
    parser.add_argument("--limit", type=int, default=3, help="Max drafts to generate (default: 3)")
    args = parser.parse_args()

    print("=" * 60)
    print("RISING SUN DIGITAL - Content Agent")
    print("=" * 60)

    # Load manifest
    manifest = load_manifest()
    existing_topics = get_existing_topics(manifest)
    print(f"\nLoaded {len(manifest.get('posts', []))} existing posts from manifest.")

    # Fetch trends
    print("\nFetching trending topics...")
    if args.sample or not PYTRENDS_AVAILABLE:
        trends = get_sample_trends()
        print("(Using sample trends)")
    else:
        trends = fetch_google_trends()

    print(f"Found {len(trends)} raw trending queries.")

    # Generate ideas
    ideas = generate_content_ideas(trends, existing_topics, args.category)

    if not ideas:
        print("\nNo new content ideas found (all trends already covered).")
        return

    print(f"\n{len(ideas)} NEW CONTENT IDEAS:")
    print("-" * 60)

    for i, idea in enumerate(ideas, 1):
        print(f"\n{i}. {idea['suggested_title']}")
        print(f"   Category: {idea['category']} | Source: {idea['source']} | Type: {idea['trend_type']}")

    # Generate drafts if requested
    if args.generate:
        print("\n" + "=" * 60)
        print("GENERATING DRAFTS")
        print("=" * 60)

        for idea in ideas[:args.limit]:
            print(f"\nGenerating: {idea['suggested_title']}...")
            content = generate_draft_with_claude(idea, manifest)
            filepath = save_draft(idea, content)
            print(f"Saved to: {filepath}")

        print(f"\nDrafts saved to: {DRAFTS_DIR}")
    else:
        print(f"\nRun with --generate to create draft files in {DRAFTS_DIR}")


if __name__ == "__main__":
    main()
