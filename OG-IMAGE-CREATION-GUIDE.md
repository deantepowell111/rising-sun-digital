# OG Image Creation Walkthrough — Rising Sun Digital

## 🎯 WHAT ARE OG IMAGES?

OG (Open Graph) images are the preview images that appear when you share your website on:
- Facebook
- Twitter/X
- LinkedIn
- Slack
- WhatsApp
- Any platform that shows link previews

**Without OG images:** Your link shows a generic preview (plain text, no branding)
**With OG images:** Your link shows a beautiful branded card that drives clicks

---

## 📐 REQUIRED SPECS

- **Dimensions:** 1200 x 630 pixels (exactly)
- **Format:** JPG or PNG (JPG recommended for smaller file size)
- **File Size:** Under 8MB (aim for under 300KB)
- **Aspect Ratio:** 1.91:1

---

## 🎨 YOUR OG TEMPLATES

You have 3 pre-designed templates ready to screenshot:

### 1. **og-light.html** (Recommended for Most Shares)
- Light cream background (#FEF9F0)
- Headline: "Predictable Leads. Real Growth."
- Subheadline: "Lead Generation Funnels for Small Businesses"
- Clean, professional, easy to read

### 2. **og-primary.html** (Best for Homepage)
- Dark background
- Headline: "Systems That Turn Traffic Into Revenue"
- Subheadline: "Growth Systems • Not Gimmicks"
- Bold, high-contrast

### 3. **og-textless.html** (Minimalist Option)
- Just logo and brand mark
- No text
- Universal for any page

---

## 📸 METHOD 1: BROWSER SCREENSHOT (EASIEST)

### Step 1: Open Template in Chrome
1. Open Chrome browser
2. Navigate to: `file:///c:/Users/alkal/Documents/official/og-light.html`
   - Or just drag `og-light.html` into Chrome window

### Step 2: Enable Device Toolbar
1. Press **F12** (or right-click → Inspect)
2. Press **Ctrl + Shift + M** (Windows) or **Cmd + Shift + M** (Mac)
   - This opens "Device Toolbar" at the top
3. You'll see dropdown that says "Responsive" or a device name

### Step 3: Set Exact Dimensions
1. Click the dropdown at top that shows dimensions
2. Select **"Edit..."** at bottom of list
3. Click **"Add custom device"**
4. Enter:
   - Device name: `OG Image`
   - Width: `1200`
   - Height: `630`
   - Device pixel ratio: `1`
5. Click **"Add"**
6. Select your new "OG Image" device from dropdown

### Step 4: Take Screenshot
1. Press **Ctrl + Shift + P** (Windows) or **Cmd + Shift + P** (Mac)
   - This opens Chrome's command palette
2. Type: `screenshot`
3. Select: **"Capture screenshot"** (NOT full page or node)
4. Chrome will save the screenshot to your Downloads folder

### Step 5: Save & Optimize
1. Rename file from `og-light.html.png` to `og-primary.jpg`
2. If PNG file is large, convert to JPG:
   - Open in Paint / Photos
   - File → Save As → JPEG
   - Quality: 90% (good balance of size vs quality)

### Step 6: Repeat for Other Templates
- Screenshot `og-primary.html` → save as `og-primary.jpg`
- Screenshot `og-textless.html` → save as `og-textless.jpg`

---

## 📸 METHOD 2: ONLINE SCREENSHOT TOOL (IF BROWSER METHOD FAILS)

### Option A: Social Sizes
1. Go to https://www.socialsizes.io/tools/screenshot-generator
2. Upload your HTML file OR enter the URL if hosted
3. Select preset: **"Facebook Share"** (1200x630)
4. Download JPG

### Option B: Screenshot.rocks
1. Go to https://screenshot.rocks/
2. Upload HTML or paste file URL
3. Set dimensions: 1200 x 630
4. Download

---

## 🖼️ METHOD 3: PHOTOSHOP / DESIGN TOOL (ADVANCED)

If you want pixel-perfect control:

### Step 1: Create New Document
- Width: 1200px
- Height: 630px
- Resolution: 72 DPI (web standard)
- Color Mode: RGB

### Step 2: Recreate Design
- Use the HTML templates as visual reference
- Match fonts (Inter font family)
- Match colors:
  - Cream: #FEF9F0
  - Teal: #1A5C54
  - Marigold: #E9A820
  - Orange: #D4652F
  - Forest: #1B5E3B

### Step 3: Export
- File → Export → Export As
- Format: JPEG
- Quality: 80-90%
- Save as `og-primary.jpg`

---

## ✅ AFTER CREATING YOUR IMAGES

### 1. Upload to Your Website
Place all 3 images in your website's root directory (same folder as index.html):
```
/rising-sun-digital/
  ├── index.html
  ├── thank-you.html
  ├── og-primary.jpg    ← NEW
  ├── og-light.jpg      ← NEW
  ├── og-textless.jpg   ← NEW
  ├── minimal-design-system.css
  └── rising-sun-logo.png
```

### 2. Verify File Names Match HTML
Your `index.html` already references `og-primary.jpg` (lines 19, 28):
```html
<meta property="og:image" content="https://risingsun.digital/og-primary.jpg">
<meta name="twitter:image" content="https://risingsun.digital/og-primary.jpg">
```

**Make sure your filename is exactly:** `og-primary.jpg` (not `og-primary.jpeg` or `og_primary.jpg`)

### 3. Test Your OG Images

#### Facebook Sharing Debugger:
1. Go to https://developers.facebook.com/tools/debug/
2. Enter: `https://risingsun.digital`
3. Click **"Debug"**
4. You should see your OG image preview
5. If not showing, click **"Scrape Again"** (Facebook caches aggressively)

#### Twitter Card Validator:
1. Go to https://cards-dev.twitter.com/validator
2. Enter: `https://risingsun.digital`
3. Click **"Preview card"**
4. Your image should appear

#### LinkedIn Post Inspector:
1. Go to https://www.linkedin.com/post-inspector/
2. Enter: `https://risingsun.digital`
3. Click **"Inspect"**
4. View your OG image preview

---

## 🎨 CUSTOMIZING YOUR OG IMAGES

### Quick Text Changes:

**Edit og-light.html:**
- Line 170: Headline (currently: "Predictable Leads. Real Growth.")
- Line 174: Subheadline (currently: "Lead Generation Funnels for Small Businesses")

**Edit og-primary.html:**
- Line 173: Headline (currently: "Systems That Turn Traffic Into Revenue")
- Line 177: Subheadline (currently: "Growth Systems • Not Gimmicks")

Just open in a text editor, change the text, save, and re-screenshot!

### Color Adjustments:
- Background: Line 21 (`background: #FEF9F0`)
- Headline: Line 111 (`color: #1A1A2E`)
- Gradient: Line 118 (change gradient colors)

---

## 🚨 COMMON ISSUES & FIXES

### Issue 1: Image Not Showing on Social Media
**Cause:** Cached old preview or wrong file path
**Fix:**
1. Clear cache using Facebook Debugger (Scrape Again button)
2. Verify file exists: Visit `https://risingsun.digital/og-primary.jpg` directly in browser
3. Check exact filename (case-sensitive on some servers)

### Issue 2: Image Looks Blurry
**Cause:** Wrong dimensions or too much compression
**Fix:**
- Re-screenshot at EXACTLY 1200x630 (use device toolbar)
- If saving as JPG, use quality 90% or higher

### Issue 3: Text is Cut Off
**Cause:** Browser zoom or incorrect device settings
**Fix:**
- Reset browser zoom to 100% (Ctrl + 0)
- Verify Device Pixel Ratio = 1 in device settings
- Make sure you selected "Capture screenshot" NOT "Capture full size screenshot"

### Issue 4: Colors Look Different
**Cause:** Color profile or monitor calibration
**Fix:**
- Use sRGB color space
- Test on multiple devices
- JPG format handles colors more consistently than PNG for web

### Issue 5: File Size Too Large
**Cause:** PNG format or high-res screenshot
**Fix:**
- Save as JPG instead of PNG (10x smaller)
- Use JPG quality 80-90% (still looks great)
- Use online compressor: https://tinyjpg.com/

---

## 📊 WHICH OG IMAGE FOR WHICH PAGE?

### Homepage (index.html):
**Use:** `og-primary.jpg`
**Why:** Bold headline captures attention, shows value immediately

### Thank-You Page (thank-you.html):
**Use:** `og-light.jpg`
**Why:** Friendly, soft tone matches post-conversion vibe

### Blog Posts / Articles (future):
**Use:** Create custom OG images per post with article title

### Generic Fallback:
**Use:** `og-textless.jpg`
**Why:** No text means it works for any page without customization

---

## ⚡ QUICK START (FASTEST PATH)

**Total time: 5 minutes**

1. Open Chrome
2. Drag `og-light.html` into Chrome window
3. Press F12 → Ctrl+Shift+M
4. Set dimensions: 1200 x 630 (click "Edit..." to add custom device)
5. Press Ctrl+Shift+P → type "screenshot" → Capture screenshot
6. Rename downloaded file to `og-primary.jpg`
7. Repeat for `og-primary.html` and `og-textless.html`
8. Upload all 3 JPGs to your website root directory
9. Test with Facebook Debugger

**Done!** Your links will now show beautiful previews.

---

## 🎯 EXPECTED RESULTS

### Before OG Images:
When you share `https://risingsun.digital` on Facebook:
- Plain text title
- Generic description
- No image
- Low click-through rate

### After OG Images:
When you share `https://risingsun.digital` on Facebook:
- Beautiful branded card
- Professional logo and design
- Clear headline with your value prop
- 3-5x higher click-through rate

---

## 📱 MOBILE PREVIEW

OG images also appear when:
- Sharing via SMS (iPhone shows preview)
- Sharing in WhatsApp
- Sharing in Slack
- Sharing in Discord

Make sure to test on mobile after uploading!

---

## 🔧 TROUBLESHOOTING CHECKLIST

If your OG image isn't showing:

- [ ] File is exactly 1200 x 630 pixels
- [ ] File is named `og-primary.jpg` (exact match to HTML)
- [ ] File is uploaded to website root directory
- [ ] File is accessible: Visit `https://risingsun.digital/og-primary.jpg` in browser
- [ ] Meta tags in index.html reference correct filename
- [ ] Cleared Facebook cache with Debugger tool
- [ ] File size is under 8MB (ideally under 300KB)
- [ ] Format is JPG or PNG (JPG recommended)

---

## 🚀 BONUS: DYNAMIC OG IMAGES (FUTURE)

Once you have traffic, consider:
- Creating unique OG images for each service
- A/B testing different headlines
- Adding social proof numbers ("Join 500+ businesses")
- Seasonal variations (holiday themes)

Tools for dynamic OG generation:
- https://www.bannerbear.com/
- https://og-image.vercel.app/
- https://www.placid.app/

---

## ✅ YOU'RE DONE WHEN:

- [ ] All 3 OG images created (og-primary.jpg, og-light.jpg, og-textless.jpg)
- [ ] Files uploaded to website root
- [ ] Facebook Debugger shows your image
- [ ] Twitter Card Validator shows your image
- [ ] Test share on actual social media looks good
- [ ] File sizes are reasonable (under 300KB each)

---

**Your links will now look professional and drive 3-5x more clicks.** 🎨

Need help? Screenshot the issue and I can troubleshoot!
