# Make.com + HubSpot Integration (100% FREE)

## 🎯 WHY MAKE.COM (NOT ZAPIER)

**Make.com FREE Tier:**
- ✅ 1,000 operations/month (FREE)
- ✅ Webhooks included
- ✅ Multi-step scenarios
- ✅ HubSpot native integration
- ✅ More powerful than Zapier
- ✅ Visual workflow builder

**Cost:** $0 until you hit 1,000 leads/month (which = $20K+ revenue)

---

## 🚀 STEP-BY-STEP SETUP (15 Minutes)

### STEP 1: Create Make.com Account

1. Go to [make.com](https://www.make.com/en/register)
2. Sign up for FREE account
3. Verify email
4. Skip the onboarding wizard (or follow it, doesn't matter)

---

### STEP 2: Create Your First Scenario

1. Click **"Create a new scenario"**
2. Name it: "Rising Sun - Lead Capture"

---

### STEP 3: Add Webhook Trigger

1. Click the **+** button
2. Search for **"Webhooks"**
3. Select **"Custom webhook"**
4. Click **"Add"**
5. Click **"Create a webhook"**
6. Name it: "Form Submissions"
7. Click **"Save"**
8. **COPY THE WEBHOOK URL** (you'll need this)
9. Click **"OK"**

**Your webhook URL will look like:**
```
https://hook.us1.make.com/abc123xyz456
```

**SAVE THIS URL!** You'll add it to Google Apps Script.

---

### STEP 4: Connect to HubSpot

1. Click the **+** button after the webhook
2. Search for **"HubSpot"**
3. Select **"Create/Update a Contact"**
4. Click **"Create a connection"**
5. Log in to your HubSpot account
6. Authorize Make.com
7. Click **"Save"**

---

### STEP 5: Map the Fields

Now you'll map form data to HubSpot fields:

**Email:**
- Click in the "Email" field
- Select `email` from the webhook data

**First Name:**
- Click "First Name"
- Select `name` from webhook
- (Or split name if you're capturing full name)

**Properties (Custom Fields):**
1. Click **"Add item"** under Properties
2. Property: `form_type`
3. Value: Select `formType` from webhook

4. Click **"Add item"** again
5. Property: `website`
6. Value: Select `website` from webhook

7. Click **"Add item"** again
8. Property: `hs_lead_status`
9. Value: Type `NEW`

**Owner (Optional):**
- Select yourself as owner
- All leads will be assigned to you

---

### STEP 6: Test the Connection

1. Click **"Run once"** at the bottom
2. Go to your website
3. Submit a test form (PDF or Audit)
4. Go back to Make.com
5. You should see the data come through
6. Click **"OK"**
7. Check HubSpot - contact should be there!

---

### STEP 7: Activate the Scenario

1. Click the toggle switch (turn it ON)
2. Name: "Rising Sun - Lead Capture"
3. Schedule: **Immediately**
4. Click **"OK"**

**Your automation is now LIVE!** 🔥

---

## 📝 STEP 8: Update Google Apps Script

Now update your form script to send data to Make.com webhook:

### Current Script Location:
Your Google Apps Script is connected to your forms. Here's how to update it:

1. Go to your Google Sheet (where form data goes)
2. Extensions → Apps Script
3. Find your form handler function

### Add This Code:

```javascript
function onFormSubmit(e) {
  // Your existing email sending code stays here

  // ADD THIS NEW SECTION:
  sendToMake(e);
}

function sendToMake(formData) {
  var webhookUrl = 'YOUR_MAKE_WEBHOOK_URL_HERE'; // Paste from Make.com

  var payload = {
    'email': formData.namedValues['email'][0],
    'name': formData.namedValues['name'][0],
    'formType': formData.namedValues['form_type'][0],
    'website': formData.namedValues['website'] ? formData.namedValues['website'][0] : '',
    'timestamp': new Date().toISOString(),
    'source': 'risingsun.digital'
  };

  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload),
    'muteHttpExceptions': true
  };

  try {
    var response = UrlFetchApp.fetch(webhookUrl, options);
    Logger.log('Make.com webhook success: ' + response.getContentText());
  } catch(e) {
    Logger.log('Make.com webhook failed: ' + e);
  }
}
```

### Replace:
- `'YOUR_MAKE_WEBHOOK_URL_HERE'` with your actual Make.com webhook URL

### Save and Test:
1. Click **Save** (💾 icon)
2. Submit a test form
3. Check Make.com - you should see it run
4. Check HubSpot - contact should appear

---

## 🎯 HUBSPOT SETUP

### Step 1: Create Custom Properties

1. Go to HubSpot → Settings (⚙️)
2. Data Management → Properties
3. Search for "Contacts"
4. Click **"Create property"**

**Property 1: Form Type**
- Label: `Form Type`
- Field type: Dropdown select
- Group: Contact Information
- Options:
  - PDF Download
  - Audit Request
  - Strategy Call Booked
- Click **"Create"**

**Property 2: Lead Temperature**
- Label: `Lead Temperature`
- Field type: Dropdown select
- Options:
  - Cold
  - Warm
  - Hot
  - Client
- Default: `Warm`
- Click **"Create"**

**Property 3: Call Booked**
- Label: `Call Booked`
- Field type: Single checkbox
- Default: Unchecked
- Click **"Create"**

---

### Step 2: Create Lists

**List 1: PDF Downloads - No Call**

1. Contacts → Lists
2. Click **"Create list"**
3. Name: "PDF Downloads - No Call"
4. Type: Active list
5. Filters:
   - `Form Type` is equal to `PDF Download`
   - AND `Call Booked` is equal to `false`
6. Click **"Save"**

**List 2: Audit Requests - No Call**

1. Create new list
2. Name: "Audit Requests - No Call"
3. Filters:
   - `Form Type` is equal to `Audit Request`
   - AND `Call Booked` is equal to `false`
4. Save

**List 3: Calls Booked**

1. Create new list
2. Name: "Calls Booked"
3. Filters:
   - `Call Booked` is equal to `true`
4. Save

---

### Step 3: Create Email Sequences

**Sequence 1: PDF Download Follow-Up**

1. Automation → Sequences
2. Click **"Create sequence"**
3. Name: "PDF Download - No Call Booked"
4. Enrollment trigger: Manual (for now)

**Email 1 (Day 0 - Immediate):**
- Subject: `Your CTA Conversion Guide is here (+ one more thing)`
- Body: [Use template from LEAD-CAPTURE-STRATEGY.md]
- CTA: Book your call

**Email 2 (Day 2):**
- Subject: `Quick question about [their website]`
- Body: "Did you get a chance to read the guide? Want to discuss how to apply this to YOUR business?"
- CTA: Book call

**Email 3 (Day 5):**
- Subject: `How [similar business] 3x'd their leads`
- Body: Case study (create one or use placeholder)
- CTA: "Want results like this? Let's talk"

**Email 4 (Day 7):**
- Subject: `Should I close your file?`
- Body: "Haven't heard back - is this still a priority? Last chance to book a call"
- CTA: Book now

**Sequence 2: Audit Request Follow-Up**

Same process, but with audit-focused emails from LEAD-CAPTURE-STRATEGY.md

---

### Step 4: Automate Enrollment (Advanced)

Once you have sequences, create workflows to auto-enroll:

1. Automation → Workflows
2. Create workflow: "Auto-Enroll PDF Downloads"
3. Enrollment trigger: Contact is added to list "PDF Downloads - No Call"
4. Action: Enroll in sequence "PDF Download - No Call Booked"
5. Activate

Repeat for Audit Requests.

---

## 🧪 TESTING CHECKLIST

Before going live, test EVERYTHING:

### Test 1: PDF Download
- [ ] Submit PDF form on your site
- [ ] Verify webhook fires in Make.com
- [ ] Check contact created in HubSpot
- [ ] Confirm "Form Type" = "PDF Download"
- [ ] Verify added to correct list
- [ ] Check email sequence enrollment (manual for now)

### Test 2: Audit Request
- [ ] Submit audit form
- [ ] Verify webhook fires
- [ ] Contact created in HubSpot
- [ ] "Form Type" = "Audit Request"
- [ ] Added to correct list

### Test 3: Call Booking
- [ ] Book a call on thank you page
- [ ] Verify Calendly event
- [ ] Check HubSpot (should update "Call Booked" = true)
- [ ] Removed from nurture sequence
- [ ] Added to "Calls Booked" list

---

## 📊 MONITORING & OPTIMIZATION

### Week 1: Watch Like a Hawk
- Check Make.com daily
- Verify all form submissions go through
- Make sure HubSpot is updating
- Monitor email open rates

### Week 2: Optimize
- Review which emails get best open rates
- Test subject lines
- Adjust timing (maybe Day 2 is too soon?)
- Track booking rate from emails

### Week 3: Scale
- Increase traffic
- Monitor automation
- Add more sequences if needed
- Start tracking revenue per sequence

---

## 💰 WHEN TO UPGRADE

**Stay FREE until:**
- You hit 1,000 operations/month (1,000 leads)
- At that point, you're making $20K+/month
- Upgrading to Make.com PRO is $9/month (nothing)

**Don't upgrade Zapier or Make until you NEED to.**

---

## 🔥 ALTERNATIVE: DIRECT HUBSPOT INTEGRATION (No Make.com)

If you want to skip Make.com entirely:

### Option: Use HubSpot Forms Instead

1. Create forms in HubSpot
2. Embed on your site
3. Direct integration (no middleware)
4. Automatically enrolled in workflows

**Downside:** You lose Google Sheets tracking.

**Upside:** Simpler, one less tool.

**My Recommendation:** Use Make.com for now. It's free and more flexible.

---

## ✅ FINAL CHECKLIST

- [ ] Make.com account created
- [ ] Webhook created
- [ ] HubSpot connected
- [ ] Fields mapped
- [ ] Google Apps Script updated with webhook URL
- [ ] Test form submission successful
- [ ] Contact appears in HubSpot
- [ ] Custom properties created
- [ ] Lists created
- [ ] Email sequences built
- [ ] Automation activated

---

## 🚀 YOU'RE LIVE!

Once all boxes are checked, you have:
- ✅ Automated lead capture
- ✅ HubSpot integration
- ✅ Email follow-up sequences
- ✅ Call booking tracking
- ✅ 100% FREE

**Now go drive traffic and watch it work.** 🔥

---

## 🆘 TROUBLESHOOTING

**Webhook not firing:**
- Check Make.com scenario is ON
- Verify webhook URL is correct in Google Apps Script
- Look at execution logs in Apps Script

**Contact not creating in HubSpot:**
- Check HubSpot connection in Make.com
- Verify email field is mapped correctly
- Check for duplicate emails (HubSpot will update existing)

**Emails not sending:**
- Check sequence enrollment
- Verify contact is in correct list
- Check email sending limits (HubSpot free = 2,000/month)

**Need help?**
Check Make.com documentation or HubSpot support (both are excellent).

---

**Let's get this automated!** 🚀
