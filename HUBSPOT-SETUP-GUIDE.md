# HubSpot Setup Guide - Keep Your Custom Forms

## 🎯 Goal: Connect Your Beautiful Forms to HubSpot CRM

You'll keep your exact form design and connect it to HubSpot for automatic lead tracking and email automation.

---

## Step 1: Sign Up for HubSpot Free CRM (5 minutes)

1. Go to [hubspot.com/products/crm](https://www.hubspot.com/products/crm)
2. Click **"Get started free"**
3. Sign up with **risingsundigital4@gmail.com**
4. Complete the onboarding (choose "Marketing Agency" as your industry)
5. Skip any paid plan offers - the free plan has everything you need

---

## Step 2: Create Your First Form - PDF Download (10 minutes)

### Create the Form:

1. In HubSpot dashboard, go to **Marketing → Lead Capture → Forms**
2. Click **"Create form"** → Choose **"Embedded form"**
3. Name it: `Digital Growth Blueprint - PDF Download`

### Add Form Fields:

Click **"Add"** and add these fields in order:

1. **Email** (required)
   - Make it required ✓
   - Label: "Email address"

### Form Settings:

Click the **Settings** tab at the top:

**Form Options:**
- Always create contact for new email: ✓ ON
- Update existing contacts: ✓ ON

**What should happen after someone fills out this form?**
- Choose: **"Display a thank you message"**
- Message: `Thanks! Check your email for the PDF download link.`

Click **"Update"** to save

---

## Step 3: Get Your PDF Form Endpoint

1. In your form settings, click **"Share"** tab
2. You'll see two options:
   - **Embed code** (we won't use this)
   - **Use the form API** (this is what we need)

3. Click **"Use the form API"**
4. Copy this URL format:
   ```
   https://api.hsforms.com/submissions/v3/integration/submit/{portalId}/{formId}
   ```

5. **Find your Portal ID:**
   - Click your account name (top right)
   - Click **"Account & Billing"**
   - Your Portal ID is shown at the top (looks like: `12345678`)

6. **Find your Form ID:**
   - In the form editor, look at the URL in your browser
   - It ends with something like: `/form-editor/12345678/abc-123-def`
   - The part after the last `/` is your Form ID

7. **Your final endpoint URL will look like:**
   ```
   https://api.hsforms.com/submissions/v3/integration/submit/12345678/abc-123-def
   ```

**SAVE THIS URL** - you'll need it in Step 5.

---

## Step 4: Create Your Second Form - Website Audit (10 minutes)

### Create the Form:

1. Go back to **Marketing → Lead Capture → Forms**
2. Click **"Create form"** → **"Embedded form"**
3. Name it: `Free Website Audit Request`

### Add Form Fields:

1. **Email** (required)
2. **Website**
   - Click "Add" → "Create new property"
   - Label: "Website URL"
   - Field type: "Single-line text"
   - Make it required ✓

### Form Settings:

Same as before:
- Always create contact ✓
- Update existing ✓
- Thank you message: `Thanks! We'll send your audit within 48 hours.`

### Get the Form Endpoint:

Same process as Step 3 - save this URL too.

---

## Step 5: Update Your Website Forms (I'll do this for you)

I'll update your `index.html` to connect to HubSpot instead of Formspree.

**What I need from you:**
1. Your Portal ID (from Step 3)
2. Your PDF Form ID (from Step 3)
3. Your Audit Form ID (from Step 4)

**Example:**
- Portal ID: `12345678`
- PDF Form ID: `abc-123-def`
- Audit Form ID: `xyz-456-ghi`

Give me these 3 IDs and I'll update your forms right now.

---

## Step 6: Set Up PDF Auto-Send Email (15 minutes)

### First, Upload Your PDF to Google Drive:

1. Upload your **Digital Growth Blueprint.pdf** to Google Drive
2. Right-click → Share → Change to **"Anyone with the link"**
3. Copy the link (example: `https://drive.google.com/file/d/abc123/view`)

### Create Email Template in HubSpot:

1. Go to **Marketing → Email → Email Templates**
2. Click **"Create template"** → Choose **"Drag and drop"**
3. Name it: `PDF Download - Digital Growth Blueprint`

4. Design your email (simple template):

**Subject:** Your Free Digital Growth Blueprint is Ready! 🚀

**Body:**
```
Hi there!

Thanks for downloading the Digital Growth Blueprint!

🎁 Download your free PDF here:
[PASTE YOUR GOOGLE DRIVE LINK]

This guide includes:
✓ 5 website mistakes killing conversions
✓ Content formula that attracts leads
✓ SEO checklist for top rankings
✓ Social media posting template

Questions? Just reply to this email or call us:
📞 (915) 234-3570

Let's grow your business together!

Best,
Rising Sun Digital Team
www.risingsun.digital
```

5. Click **"Save"**

### Create Workflow to Auto-Send:

1. Go to **Automation → Workflows**
2. Click **"Create workflow"** → **"Contact-based"** → **"Blank workflow"**
3. Name it: `Auto-Send PDF Download`

4. **Set enrollment trigger:**
   - Click **"Set enrollment triggers"**
   - Choose: **"Form submission"**
   - Select form: `Digital Growth Blueprint - PDF Download`
   - Click **"Apply filter"**

5. **Add email action:**
   - Click the **"+"** button
   - Choose **"Send email"**
   - Select your template: `PDF Download - Digital Growth Blueprint`
   - From: `Rising Sun Digital <risingsundigital4@gmail.com>`
   - Click **"Save"**

6. **Review and activate:**
   - Click **"Review"** (top right)
   - Turn workflow **ON**

**DONE!** Now when someone submits the PDF form, they'll get the email automatically.

---

## Step 7: Set Up Website Audit Email (Optional)

Repeat Step 6 for the audit form:

**Email Template Subject:** Your Free Website Audit is Coming! 🔍

**Body:**
```
Hi there!

We received your website audit request for: {{contact.website}}

Our team will analyze your site and send a detailed report within 48 hours.

Your audit will include:
✓ Full SEO health check & score
✓ Page speed analysis
✓ Mobile responsiveness review
✓ Conversion opportunities

Talk soon!

Rising Sun Digital Team
📞 (915) 234-3570
```

Create a workflow called `Auto-Send Audit Confirmation` with this template.

---

## What Happens Now?

✅ **Someone submits PDF form** → Saved to HubSpot CRM → Auto-email with PDF link
✅ **Someone submits audit form** → Saved to HubSpot CRM → Auto-email confirmation
✅ **All leads in one place** → HubSpot CRM dashboard
✅ **Track everything** → See who downloaded what, when they visited, etc.

---

## 🚀 Ready to Connect?

**Give me your 3 IDs and I'll update your forms right now:**

1. Portal ID: `_____________`
2. PDF Form ID: `_____________`
3. Audit Form ID: `_____________`

Paste them here and I'll have your site connected to HubSpot in 2 minutes.
