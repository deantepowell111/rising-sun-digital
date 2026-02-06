# Rising Sun Digital - Lead Capture & Follow-Up Strategy

## 🎯 THE PROBLEM WITH YOUR CURRENT FLOW

**What's happening now:**
1. People download PDF → disappear
2. People request audit → wait 48 hours → disappear
3. You're giving away value with ZERO commitment to call

**Result:** Lots of downloads, few conversations, minimal revenue.

---

## ✅ THE OPTIMIZED FLOW (Based on 20+ Years Experience)

### Core Principle:
**Strike while the iron is HOT. Book the call BEFORE they leave your site.**

---

## 🔥 OPTION A: IMMEDIATE CALL BOOKING (RECOMMENDED)

### PDF Download Flow:
```
Visitor lands on site
    ↓
Downloads PDF (name + email)
    ↓
NEW Thank You Page with:
  - "Your PDF is in your email"
  - "But here's the thing..."
  - "Want me to walk you through YOUR situation?"
  - Calendly embedded RIGHT THERE
    ↓
Books call (30-40% conversion)
    ↓
Enters HubSpot workflow
    ↓
Gets reminder sequence
    ↓
Shows up for call (60-70% show rate)
```

### Site Audit Flow:
```
Visitor requests audit
    ↓
NEW Thank You Page:
  - "Let's do this LIVE instead of sending a report"
  - "Book 20-min call - I'll audit your site WITH you"
  - Calendly embedded
    ↓
Books live audit call (40-50% conversion)
    ↓
Shows up (70-80% show rate because it's THEIR site)
    ↓
You close on the call
```

**Why this works:**
- ⚡ **Immediate commitment** (while engaged)
- 🔥 **Higher show rate** (booked in the moment)
- 💬 **You're on the call** (builds relationship)
- 🎯 **No ghosting** (they committed before leaving)

---

## 🔥 OPTION B: HYBRID FLOW (If You Want Both)

### Give Them a Choice:
```
Thank You Page offers:

[Primary CTA]
"Book Your Free Strategy Call Now" (Calendly)

[Secondary CTA]
"Just send me the guide, I'll book later" (Email only)
```

**80% of people who "will book later" never do.**
**But this lets the 20% who truly aren't ready to still get value.**

---

## 📊 HUBSPOT INTEGRATION STRATEGY

### The Complete Automation Flow:

```
STEP 1: Form Submission
  ↓
Google Apps Script (current setup)
  ↓
STEP 2: Zapier/Make.com Webhook
  ↓
Creates contact in HubSpot with properties:
  - Email
  - Name
  - Form Type (PDF / Audit / Booking)
  - Website URL (if provided)
  - Source (organic, paid, referral)
  - Timestamp
  ↓
STEP 3: Assign to Workflow Based on Action
```

---

## 🤖 HUBSPOT WORKFLOWS TO CREATE

### Workflow 1: PDF Download (No Call Booked)

**Trigger:** Contact fills PDF form, no call booked

**Sequence:**
- **Minute 0:** Email with PDF + P.S. "Book your call"
- **Day 2:** "Did you read the guide? Let's discuss YOUR site"
  - Subject: "Quick question about [their business]"
  - Body: Personalized based on industry
  - CTA: Book call
- **Day 5:** Value email (case study or tip)
  - Subject: "How [Similar Business] got 3x more leads"
  - CTA: "Want results like this? Let's talk"
- **Day 7:** Last chance
  - Subject: "Should I close your file?"
  - Create urgency
  - Final CTA to book

**Exit condition:** They book a call (move to Workflow 3)

---

### Workflow 2: Audit Request (No Call Booked)

**Trigger:** Contact requests audit, no call booked

**Sequence:**
- **Minute 0:** Email
  - Subject: "Your live audit is waiting"
  - Body: "Instead of sending a report, let's do this live"
  - CTA: Book your live audit call
- **Day 1:** Follow-up
  - Subject: "I found 3 issues on your site..."
  - Tease what you found
  - CTA: "Want to see them? Book here"
- **Day 3:** Social proof
  - Subject: "How we helped [Similar Business]"
  - Case study
  - CTA: Book call
- **Day 5:** Final offer
  - Subject: "Last chance for free audit"
  - Urgency
  - CTA: Book now

**Exit condition:** They book (move to Workflow 3)

---

### Workflow 3: Call Booked (Pre-Call Nurture)

**Trigger:** Contact books a call

**Sequence:**
- **Immediately:** Calendar invite
  - Zoom/Google Meet link
  - Add to calendar
  - What to prepare
- **1 Day Before:**
  - Subject: "Tomorrow: Your strategy call with Deante"
  - Reminder
  - What to have ready (website login if applicable)
- **2 Hours Before:**
  - Subject: "See you in 2 hours!"
  - Confirmation
  - Link to join

**During Call:**
- Discovery questions
- Live audit
- Show quick wins
- Present offer

**After Call (Within 1 Hour):**
- Email: "Great talking to you!"
- Recap call
- Send proposal/next steps
- CTA: "Ready to move forward?"

---

### Workflow 4: Post-Call Follow-Up (Didn't Close)

**Trigger:** Call completed, no deal closed

**Sequence:**
- **Same Day:** Thank you + recap
- **Day 2:** Answer objection
  - "You mentioned [concern]..."
  - Address it
- **Day 5:** Case study
  - Similar business that had same concern
  - How you solved it
- **Day 7:** Final offer
  - Limited-time bonus
  - "Spots filling up"
- **Day 14:** Last touch
  - "Should I close your file?"
  - Final CTA

**Exit condition:** They become client or mark as closed-lost

---

## 📧 EMAIL TEMPLATES (Use These)

### Email 1: PDF Delivery (Immediate)

**Subject:** Your CTA Conversion Guide is here (+ one more thing)

**Body:**
```
Hey [Name],

Your free CTA guide is attached.

But here's the thing...

Most people read this and STILL make the same mistakes on their site.

Want me to walk you through how to apply this to YOUR specific business?

I'm offering free 15-minute strategy calls this week (only 3 spots left).

I'll:
✓ Audit your site live
✓ Show you exactly what's costing you leads
✓ Give you a custom action plan (yours to keep)

Zero pressure. Just value.

Book here: [Calendly Link]

Talk soon,
Deante Powell
Rising Sun Digital
(915) 234-3570
```

---

### Email 2: Audit Request (Immediate)

**Subject:** Let's do your audit LIVE (way better than a report)

**Body:**
```
Hey [Name],

Instead of sending you a boring PDF report that you might read (or might not 😅)...

Let's do something better:

Book a 20-minute call and I'll audit [their website] WITH you.

You'll see:
✓ What's working (and why)
✓ What's costing you leads (and how to fix it)
✓ Quick wins you can implement TODAY

Way more valuable than a static report.

Plus, you can ask questions in real-time.

Book your live audit: [Calendly Link]

Only 3 spots this week, so grab one while you can.

Deante
Rising Sun Digital
```

---

## 🎯 HUBSPOT SETUP (Step-by-Step)

### Step 1: Create Custom Properties

Go to Settings → Properties → Create Custom Properties:

1. **Form Type**
   - Type: Dropdown
   - Options: PDF Download, Audit Request, Strategy Call

2. **Call Booked**
   - Type: Yes/No
   - Default: No

3. **Lead Temperature**
   - Type: Dropdown
   - Options: Cold, Warm, Hot, Client

4. **Website URL**
   - Type: Single-line text
   - Use: Store their site for audit

5. **Industry**
   - Type: Dropdown
   - Options: Home Services, E-commerce, Professional Services, etc.

### Step 2: Create Lists

1. **PDF Downloaded - No Call**
   - Filter: Form Type = PDF Download AND Call Booked = No

2. **Audit Requested - No Call**
   - Filter: Form Type = Audit Request AND Call Booked = No

3. **Call Booked - Upcoming**
   - Filter: Call Booked = Yes AND Deal Stage ≠ Closed Won

4. **Call Completed - No Sale**
   - Filter: Call Completed = Yes AND Deal Stage = Closed Lost

### Step 3: Create Workflows

Use the sequences outlined above.

Set enrollment triggers based on form submissions.

### Step 4: Connect to Zapier/Make.com

**Zap Setup:**
```
Trigger: Webhook (from Google Apps Script)
    ↓
Action 1: Create/Update Contact in HubSpot
    ↓
Action 2: Add to appropriate list
    ↓
Action 3: Trigger workflow
```

---

## 🔧 GOOGLE APPS SCRIPT MODIFICATION

Update your form script to send webhook to Zapier:

```javascript
function sendToZapier(formData) {
  var webhookUrl = 'YOUR_ZAPIER_WEBHOOK_URL';

  var payload = {
    'email': formData.email,
    'name': formData.name,
    'formType': formData.form_type,
    'website': formData.website || '',
    'timestamp': new Date().toISOString(),
    'source': 'risingsun.digital'
  };

  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload)
  };

  try {
    UrlFetchApp.fetch(webhookUrl, options);
  } catch(e) {
    Logger.log('Zapier webhook failed: ' + e);
  }
}
```

---

## 📞 THE CALL STRATEGY

### Before the Call:
- [ ] Review their website (if provided)
- [ ] Note 3 quick wins
- [ ] Prepare questions

### During the Call (15-20 min):
**Minutes 0-3:** Build rapport
- "Thanks for hopping on"
- "Tell me about your business"
- "What's your #1 challenge?"

**Minutes 3-10:** Discovery + Live Audit
- Share screen
- Walk through their site
- Point out issues (gently)
- Show quick fixes
- Get them saying "oh wow" 3+ times

**Minutes 10-15:** Soft Pitch
- "Want me to help you fix this?"
- Present offer
- Handle objections
- Ask for the sale

**Minutes 15-17:** Next Steps
- If yes: Send proposal
- If maybe: "What would you need to see?"
- If no: "Can I follow up in a week?"

### After the Call:
- Send recap email immediately
- If interested: Proposal within 24 hours
- If not ready: Add to nurture sequence

---

## 🎯 CONVERSION MATH

### Current Flow (Broken):
- 100 visitors → 5 PDF downloads → 0 calls → 0 clients

### Optimized Flow:
- 100 visitors → 10 PDF downloads → 4 calls booked → 2-3 clients

**4x improvement from same traffic.**

---

## 🚀 IMPLEMENTATION PRIORITY

### Week 1:
- [ ] Replace thank-you.html with thank-you-new.html
- [ ] Test the new flow (PDF + Audit)
- [ ] Set up Zapier webhook

### Week 2:
- [ ] Create HubSpot properties
- [ ] Build HubSpot lists
- [ ] Create email templates

### Week 3:
- [ ] Build HubSpot workflows
- [ ] Test full automation
- [ ] Go live

### Week 4:
- [ ] Monitor conversion rates
- [ ] Optimize based on data
- [ ] Scale what works

---

## 💰 EXPECTED RESULTS (90 Days)

**Month 1:**
- 50 visitors → 10 downloads → 4 calls → 1-2 clients → $2-5K

**Month 2:**
- 150 visitors → 30 downloads → 12 calls → 4-6 clients → $8-15K

**Month 3:**
- 300 visitors → 60 downloads → 25 calls → 10-15 clients → $20-30K

**This is what a real funnel looks like.**

---

## 🔥 PRO TIPS

1. **Don't overthink the call**
   - It's just a conversation
   - Be helpful, not salesy
   - Show value first

2. **Follow up FAST**
   - Within 1 hour of call
   - Send proposal same day
   - Strike while iron is hot

3. **Track everything**
   - Booking rate from thank you page
   - Show rate for calls
   - Close rate on calls
   - Optimize the weakest link

4. **Test your own funnel**
   - Go through it yourself
   - Is it smooth?
   - Would YOU book a call?

---

## ✅ CHECKLIST

- [ ] Replace thank-you.html with new version
- [ ] Update form redirect URLs
- [ ] Set up Zapier webhook
- [ ] Create HubSpot properties
- [ ] Build HubSpot workflows
- [ ] Write email templates
- [ ] Test entire flow end-to-end
- [ ] Go live and monitor

---

**This is how you turn traffic into revenue.**

No more "I'll think about it" — book the call NOW.
