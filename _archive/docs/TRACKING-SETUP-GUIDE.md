# GA4 Tracking Setup Guide — Rising Sun Digital

## ✅ WHAT'S INSTALLED

GA4 tracking is now configured on both pages:
- ✓ [index.html](c:\Users\alkal\Documents\official\index.html) (homepage)
- ✓ [thank-you.html](c:\Users\alkal\Documents\official\thank-you.html) (post-conversion)

---

## 🎯 EVENTS BEING TRACKED

### 1. **Page Views** (Automatic)
- Fires on every page load
- Tracks: Homepage visits, thank-you page visits

### 2. **generate_lead** (Form Submissions)
- **PDF Download Form**: Value = $100
- **Audit Request Form**: Value = $200
- Fires when user successfully submits either lead magnet form
- Redirects to thank-you page after tracking

### 3. **cta_click** (Button Engagement)
- Fires when user clicks any "Book Call" CTA button
- Value = $50
- Tracks interest before booking

### 4. **conversion** (Calendly Booking)
- Fires when user actually schedules a strategy call
- Value = $500 (highest value conversion)
- Tracks on both homepage and thank-you page

---

## 🚀 HOW TO ACTIVATE TRACKING

### Step 1: Get Your GA4 Measurement ID

1. Go to [Google Analytics](https://analytics.google.com)
2. Create a new GA4 property (if you don't have one):
   - Click **Admin** (gear icon, bottom left)
   - Under **Property**, click **Create Property**
   - Name it: "Rising Sun Digital"
   - Select timezone and currency
   - Click **Next** → Choose **Small/Medium business** → **Get leads**
   - Click **Create**

3. Get your Measurement ID:
   - Go to **Admin** → **Data Streams**
   - Click **Add stream** → **Web**
   - Website URL: `https://risingsun.digital`
   - Stream name: "Rising Sun Website"
   - Click **Create Stream**
   - Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 2: Add Your ID to Both Files

**In index.html** (lines 42-52):
```html
<!-- TODO: Replace YOUR_GA4_MEASUREMENT_ID with your actual GA4 ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX', {
        'send_page_view': true,
        'cookie_flags': 'SameSite=None;Secure'
    });
</script>
```

**In thank-you.html** (lines 30-40):
```html
<!-- Same as above -->
```

**Search & Replace:**
1. Open both files
2. Find: `YOUR_GA4_MEASUREMENT_ID`
3. Replace with: `G-XXXXXXXXXX` (your actual ID)

### Step 3: Deploy to Production

Upload both updated files to your server:
- `index.html`
- `thank-you.html`

---

## 🧪 HOW TO TEST (CRITICAL)

### Real-Time Verification:

1. **Open GA4 Real-Time Report:**
   - Go to [Google Analytics](https://analytics.google.com)
   - Click **Reports** → **Realtime**

2. **Test Each Conversion Event:**

   **Test 1: Page View**
   - Visit: `https://risingsun.digital`
   - Check: Real-time report should show 1 active user
   - ✓ **Pass if:** You see yourself in the report

   **Test 2: CTA Click**
   - Click any "Book a Call" button
   - Check: Event `cta_click` appears in real-time
   - ✓ **Pass if:** Event appears within 5 seconds

   **Test 3: Form Submission**
   - Fill out PDF download form with test email
   - Submit and wait for redirect
   - Check: Event `generate_lead` with label `pdf_download` appears
   - ✓ **Pass if:** Event shows value = $100

   **Test 4: Calendly Booking**
   - Scroll to booking section
   - Click "Select a Date & Time" in Calendly widget
   - Pick a time and fill out form
   - Complete booking
   - Check: Event `conversion` with label `Strategy Call Booked` appears
   - ✓ **Pass if:** Event shows value = $500

3. **Common Issues:**
   - **No events showing?** Check that you replaced `YOUR_GA4_MEASUREMENT_ID`
   - **Page views but no events?** Clear browser cache and test again
   - **Events delayed?** GA4 can take 1-2 minutes; be patient

---

## 📊 WHAT YOU'LL SEE IN GA4 (After 24-48 Hours)

### Reports to Monitor:

1. **Acquisition Report:**
   - Where users are coming from (Google Ads, organic, direct)
   - Which sources convert best

2. **Engagement Report:**
   - Event count breakdown (page_view, generate_lead, conversion)
   - Top pages (index.html should dominate)

3. **Conversions Report:**
   - Total leads captured (PDF + audit requests)
   - Total bookings (Calendly conversions)
   - Conversion rate by source

### Custom Funnel to Create:

1. Go to **Explore** → **Blank**
2. Create funnel:
   - Step 1: `page_view` (homepage)
   - Step 2: `cta_click` (engagement)
   - Step 3: `generate_lead` (form submit)
   - Step 4: `conversion` (booking)
3. This shows drop-off at each stage

---

## 🎯 CONVERSION VALUES (Why They Matter)

Each event has a monetary value so you can calculate ROI:

- **Page View**: $0 (baseline)
- **CTA Click**: $50 (shows interest)
- **PDF Download**: $100 (lead magnet)
- **Audit Request**: $200 (higher intent)
- **Calendly Booking**: $500 (qualified call)

**Example Calculation:**
- 1,000 visitors → 50 CTA clicks → 20 form submits → 5 bookings
- Revenue potential: 5 bookings × $2,000 avg deal = $10,000
- If you spent $1,000 on ads, ROI = 10x

---

## ⚠️ IMPORTANT NOTES

### Before Running Paid Ads:

1. ✅ Verify all 4 event types are firing in real-time
2. ✅ Check that conversions appear in GA4 dashboard
3. ✅ Set up email alerts for daily conversion counts
4. ✅ Create custom dashboard showing: traffic → leads → bookings

### Privacy Compliance:

- GA4 tracking is cookie-based
- Consider adding cookie consent banner if targeting EU users
- Current setup uses `SameSite=None;Secure` for cross-site tracking

### DO NOT:

- Run ads before verifying tracking works
- Use different GA4 IDs on homepage vs. thank-you page
- Test with personal email (it won't send duplicate leads to HubSpot)

---

## ✅ PHASE 2 COMPLETE CHECKLIST

- [ ] GA4 property created
- [ ] Measurement ID added to both files
- [ ] Files deployed to production
- [ ] Page view tracking verified (real-time)
- [ ] CTA click tracking verified
- [ ] Form submission tracking verified
- [ ] Calendly booking tracking verified
- [ ] Funnel visualization created in GA4

**Estimated Time:** 30-45 minutes

---

## 🚀 NEXT: PHASE 3 (FUNNEL OPTIMIZATION)

Once tracking is verified, Phase 3 will address:
- Choice section redundancy
- Countdown banner positioning
- Mobile experience testing

---

## 📞 QUICK REFERENCE

**Files Modified:**
- `index.html` (lines 42-52, 1012-1041)
- `thank-you.html` (lines 30-40)

**GA4 Dashboard:**
- [analytics.google.com](https://analytics.google.com)

**Real-Time Report:**
- Reports → Realtime → Event count by Event name

---

**Tracking is the foundation of optimization. No tracking = flying blind.**
