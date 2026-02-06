# Rising Sun Digital - Analytics & Tracking Setup

## 🎯 TRACKING STRATEGY

Track everything that matters. Ignore vanity metrics.

---

## 📊 GOOGLE ANALYTICS 4 SETUP

### Step 1: Create GA4 Property
1. Go to [analytics.google.com](https://analytics.google.com)
2. Create account: "Rising Sun Digital"
3. Create property: "risingsun.digital"
4. Set timezone: US/Mountain (El Paso)
5. Enable Enhanced Measurement

### Step 2: Install Tracking Code
Add this to `<head>` of all pages (index.html, 404.html, privacy.html, thank-you.html):

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

---

## 🎯 CONVERSION EVENTS TO TRACK

### Priority 1: Lead Capture Events

```javascript
// PDF Download
gtag('event', 'generate_lead', {
  'event_category': 'Lead Magnet',
  'event_label': 'CTA Guide PDF Download',
  'value': 50
});

// Website Audit Request
gtag('event', 'generate_lead', {
  'event_category': 'Lead Magnet',
  'event_label': 'Free Website Audit',
  'value': 150
});

// Strategy Call Booking
gtag('event', 'generate_lead', {
  'event_category': 'Booking',
  'event_label': 'Free Strategy Call',
  'value': 500
});
```

### Priority 2: Engagement Events

```javascript
// Scroll Depth
gtag('event', 'scroll', {
  'event_category': 'Engagement',
  'event_label': '50% Scroll',
  'value': 50
});

// CTA Clicks
gtag('event', 'click', {
  'event_category': 'CTA',
  'event_label': 'Book Free Call - Hero',
  'value': 0
});

// Exit Intent Popup
gtag('event', 'popup_shown', {
  'event_category': 'Popup',
  'event_label': 'Exit Intent',
  'value': 0
});
```

---

## 🔥 MICROSOFT CLARITY (FREE HEATMAPS)

### Why Clarity?
- **100% FREE** (unlike Hotjar)
- Heatmaps
- Session recordings
- Rage clicks
- Dead clicks
- Scroll maps

### Setup:
1. Go to [clarity.microsoft.com](https://clarity.microsoft.com)
2. Sign up with Microsoft account
3. Add new project: "risingsun.digital"
4. Copy tracking code
5. Add before `</head>`:

```html
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "YOUR_PROJECT_ID");
</script>
```

---

## 📞 CALL TRACKING (OPTIONAL)

### If using phone as primary CTA:
- **CallRail** (starts $45/mo)
- **CallTrackingMetrics**
- Track which marketing source drives calls
- Record calls for quality/training

### For now:
Use Google Voice number forwarding to your cell
- Free
- Can see call volume
- Separate from personal number

---

## 🧪 A/B TESTING SETUP

### Google Optimize (FREE but sunsetting)
Currently active until Sept 2023. Consider alternatives.

### Alternatives:
1. **VWO** (Visual Website Optimizer) - starts $199/mo
2. **Optimizely** - enterprise pricing
3. **Manual Split Testing** - create 2 versions, rotate weekly

### What to Test First:
1. Hero headline
2. CTA button copy
3. Form length (2 vs 3 fields)
4. Guarantee prominence
5. Exit popup offer

---

## 📈 CONVERSION FUNNEL TRACKING

### Track These Steps:

```
1. Landing (Homepage View)
   ↓
2. Scroll 50%
   ↓
3. CTA Click
   ↓
4. Form View
   ↓
5. Form Submit
   ↓
6. Thank You Page
```

### Set Up in GA4:
1. Go to "Explore" → "Funnel exploration"
2. Add steps above
3. Track drop-off points
4. Optimize weakest steps

---

## 🎯 GOALS TO SET

### GA4 Conversions:
- [ ] PDF Download (Event: `generate_lead` where label = 'CTA Guide')
- [ ] Audit Request (Event: `generate_lead` where label = 'Website Audit')
- [ ] Call Booking (Event: `generate_lead` where label = 'Strategy Call')
- [ ] 50% Scroll (Event: `scroll`)
- [ ] Email Click (Event: `click` where label contains 'email')
- [ ] Phone Click (Event: `click` where label contains 'phone')

### Assign Values:
- PDF Download: $50
- Audit Request: $150
- Call Booking: $500

Why? Shows ROI even before closing deals.

---

## 🔍 UTM PARAMETERS FOR TRACKING

### For All Marketing Channels:

**Organic Social:**
```
?utm_source=instagram&utm_medium=social&utm_campaign=launch
?utm_source=facebook&utm_medium=social&utm_campaign=launch
```

**Paid Ads:**
```
?utm_source=google&utm_medium=cpc&utm_campaign=digital_marketing_elpaso
?utm_source=facebook&utm_medium=paid_social&utm_campaign=retargeting
```

**Email:**
```
?utm_source=newsletter&utm_medium=email&utm_campaign=welcome_series
```

**Referral:**
```
?utm_source=partner_website&utm_medium=referral&utm_campaign=co_marketing
```

### URL Builder:
Use [ga-dev-tools.google/campaign-url-builder](https://ga-dev-tools.google/campaign-url-builder)

---

## 📊 WEEKLY KPI DASHBOARD

### Track Every Monday:

| Metric | Target | Actual | Notes |
|--------|--------|--------|-------|
| Visitors | 100/week | ___ | |
| Conversion Rate | 3-5% | ___ | |
| PDF Downloads | 3-5 | ___ | |
| Audit Requests | 2-3 | ___ | |
| Calls Booked | 2-3 | ___ | |
| Show Rate | 60%+ | ___ | |
| Cost Per Lead | <$30 | ___ | (when ads start) |

---

## 🚨 ALERTS TO SET UP

### In GA4:
1. **Traffic Drop Alert**: 50% decrease week-over-week
2. **Conversion Drop**: 30% decrease in form submissions
3. **Bounce Rate Spike**: >75% bounce rate
4. **Page Load Alert**: Pages loading >3 seconds

### How to Set:
GA4 → Admin → Custom Alerts → Create Alert

---

## 🎯 RETARGETING PIXEL SETUP

### Facebook Pixel:
1. Go to Facebook Events Manager
2. Create Pixel: "Rising Sun Digital"
3. Add base code to all pages
4. Set up custom events:
   - ViewContent (page views)
   - AddToCart (form starts)
   - Lead (form submissions)

### Google Ads Remarketing Tag:
1. Google Ads → Tools → Audience Manager
2. Create remarketing list
3. Add tag to all pages
4. Build audiences:
   - All visitors
   - Visited but didn't convert
   - Downloaded PDF
   - Abandoned forms

---

## 📱 MOBILE vs DESKTOP TRACKING

### Segments to Create:
- Mobile traffic
- Desktop traffic
- Tablet traffic

### Why?
Mobile might convert differently. Test separate:
- Headlines
- CTA placement
- Form length
- Call vs Form preference

---

## 🧠 BEHAVIOR FLOW ANALYSIS

### Questions to Answer:
1. What's the most common path to conversion?
2. Where do people drop off?
3. Which pages drive the most conversions?
4. Which traffic sources convert best?

### Monthly Review:
- Identify top 3 pages by conversions
- Find top 3 exit pages
- Optimize worst performers first

---

## 🎯 COST PER ACQUISITION TRACKING

### Formula:
```
CPA = Total Marketing Spend / Total Conversions
```

### Track By Channel:
- Organic (SEO): ~$0 (time investment)
- Paid Search: Track in Google Ads
- Paid Social: Track in Meta Ads Manager
- Email: ~$0-50/mo (tool cost)

### Target CPA (when ads start):
- PDF Download: <$10
- Audit Request: <$25
- Call Booking: <$50

---

## ✅ IMPLEMENTATION CHECKLIST

Phase 1 (Week 1):
- [ ] Install GA4 tracking code
- [ ] Install Microsoft Clarity
- [ ] Set up conversion events
- [ ] Create UTM templates
- [ ] Test all tracking (use GA4 DebugView)

Phase 2 (Week 2):
- [ ] Set up conversion goals
- [ ] Create custom dashboards
- [ ] Set up alerts
- [ ] Install retargeting pixels

Phase 3 (Week 3):
- [ ] Review first week data
- [ ] Identify optimization opportunities
- [ ] Start A/B test planning

---

## 🔥 PRO TIPS

1. **Test Tracking Before Launch**
   - Use GA4 DebugView
   - Submit test forms
   - Check events fire correctly

2. **Don't Obsess Over Traffic**
   - 100 targeted visitors > 1,000 random visitors
   - Focus on conversion rate, not traffic volume

3. **Review Data Weekly**
   - Every Monday morning
   - Look for trends
   - Make ONE optimization per week

4. **Trust the Data, Not Opinions**
   - What you "think" works ≠ what actually works
   - Let numbers guide decisions

---

## 📈 LONG-TERM TRACKING STRATEGY

### Month 1:
- Establish baseline
- Track everything
- Don't change anything yet

### Month 2:
- Identify worst-performing elements
- Run first A/B test
- Optimize based on data

### Month 3:
- Scale what works
- Kill what doesn't
- Start building case studies

---

## 💰 EXPECTED ROI TIMELINE

**Month 1:** Baseline data, $0-2K revenue
**Month 2:** 1-2 clients closed, $2-5K revenue
**Month 3:** Optimized funnel, $5-10K revenue
**Month 6:** Predictable lead flow, $15-25K revenue

**This is what we're building toward.**
