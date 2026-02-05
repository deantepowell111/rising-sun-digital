# Rising Sun Digital - Deployment Checklist

## 🚀 PRE-LAUNCH CHECKLIST

Go through this **line by line** before going live.

---

## ✅ CONTENT & COPY

- [ ] All placeholder text replaced with real copy
- [ ] Phone number is correct: (915) 234-3570
- [ ] Email is correct: hello@risingsun.digital
- [ ] Address is correct (if showing): El Paso, TX
- [ ] Social media links work:
  - [ ] Facebook: https://www.facebook.com/profile.php?id=61567085197749
  - [ ] Instagram: https://www.instagram.com/risingsundigital/
  - [ ] LinkedIn: https://linkedin.com/company/risingsundigital
- [ ] All internal links work (#services, #about, #booking, etc.)
- [ ] Privacy Policy is complete
- [ ] No "Lorem Ipsum" or dummy text anywhere

---

## 🖼️ IMAGES & MEDIA

- [ ] Logo displays correctly (rising-sun-logo.png)
- [ ] Favicon shows in browser tab
- [ ] All images load (no broken image icons)
- [ ] Images are optimized (<200KB each)
- [ ] Alt text on all images for SEO/accessibility

---

## 📱 MOBILE RESPONSIVENESS

Test on actual devices:
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] Tablet

Check:
- [ ] Navigation menu works on mobile
- [ ] Forms are easy to fill out
- [ ] Buttons are tap-friendly (44x44px minimum)
- [ ] Text is readable (no tiny fonts)
- [ ] No horizontal scrolling
- [ ] Countdown banner looks good on mobile
- [ ] Exit popup works on mobile
- [ ] Sticky CTA bar stacks properly

---

## 🔗 FORMS & INTEGRATIONS

### PDF Form:
- [ ] Submit test form
- [ ] Confirm email received in inbox
- [ ] Check Google Sheet populated correctly
- [ ] Verify redirect to thank-you.html works
- [ ] Test with fake data first, then real email

### Audit Form:
- [ ] Submit test form
- [ ] Confirm email received
- [ ] Check Google Sheet populated
- [ ] Verify redirect works
- [ ] Include website URL in test

### Calendly Booking:
- [ ] Calendar widget loads
- [ ] Can select date/time
- [ ] Booking confirmation works
- [ ] Receives confirmation email
- [ ] Syncs with your Google Calendar

### Email Deliverability:
- [ ] Check spam folder (form submissions)
- [ ] Whitelist hello@risingsun.digital in your email
- [ ] Set up email forwarding if needed

---

## ⚡ PERFORMANCE

### Page Speed:
- [ ] Run [PageSpeed Insights](https://pagespeed.web.dev/)
- [ ] Desktop score >90
- [ ] Mobile score >80
- [ ] Largest Contentful Paint <2.5s
- [ ] First Input Delay <100ms
- [ ] Cumulative Layout Shift <0.1

### If Slow:
- Optimize images (use tinypng.com)
- Enable browser caching
- Minimize CSS/JS
- Use CDN for external resources

---

## 🔍 SEO BASICS

- [ ] Title tags unique on every page
- [ ] Meta descriptions on every page
- [ ] H1 tag on every page (only one per page)
- [ ] robots.txt allows crawling
- [ ] sitemap.xml submitted to Google Search Console
- [ ] Google My Business claimed (El Paso location)
- [ ] Schema markup implemented
- [ ] Canonical URLs set correctly
- [ ] Open Graph tags for social sharing

### Submit to Google:
1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add property: risingsun.digital
3. Verify ownership (HTML tag or DNS)
4. Submit sitemap.xml
5. Request indexing for homepage

---

## 🛡️ SECURITY & PRIVACY

- [ ] HTTPS enabled (SSL certificate active)
- [ ] Privacy policy page exists and is linked
- [ ] Terms of service (if needed)
- [ ] Cookie notice (if using tracking cookies)
- [ ] No exposed API keys or credentials
- [ ] Forms protected from spam (honeypot or reCAPTCHA)
- [ ] Security headers in vercel.json:
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection

---

## 📊 ANALYTICS & TRACKING

- [ ] Google Analytics 4 installed
- [ ] GA4 tracking code on all pages
- [ ] Test with GA4 DebugView
- [ ] Conversion events set up
- [ ] Microsoft Clarity installed (optional but recommended)
- [ ] Facebook Pixel installed (if using FB ads)
- [ ] Google Ads remarketing tag (if using Google ads)
- [ ] HubSpot tracking active
- [ ] UTM parameters ready for campaigns

---

## 🎨 BRANDING & DESIGN

- [ ] Colors match brand (green/red/yellow)
- [ ] Fonts load correctly (Playfair Display + DM Sans)
- [ ] Buttons have hover states
- [ ] Animations work smoothly
- [ ] No broken layouts
- [ ] Consistent spacing throughout
- [ ] Professional, not "DIY" looking

---

## 🧪 CROSS-BROWSER TESTING

Test in:
- [ ] Chrome (most users)
- [ ] Safari (iPhone users)
- [ ] Firefox
- [ ] Edge
- [ ] Mobile browsers

Check:
- Countdown timer works
- Forms submit correctly
- Exit popup triggers
- Sticky CTA appears
- All animations smooth

---

## 📞 CONTACT METHODS

- [ ] Phone number clickable (tel: link)
- [ ] Email clickable (mailto: link)
- [ ] Calendly loads correctly
- [ ] Social links open in new tab
- [ ] Contact info in footer
- [ ] "Contact Us" clear and visible

---

## 🎯 CONVERSION OPTIMIZATION

- [ ] Primary CTA above the fold
- [ ] CTAs stand out visually
- [ ] Forms as short as possible
- [ ] Trust signals near CTAs
- [ ] Guarantee prominently displayed
- [ ] "What Happens Next" section clear
- [ ] Exit popup working
- [ ] Sticky CTA bar shows on scroll
- [ ] No broken user journeys

---

## 🚨 ERROR HANDLING

- [ ] 404 page exists and looks good
- [ ] 404 redirects to helpful content
- [ ] Form validation messages clear
- [ ] Error messages user-friendly
- [ ] No console errors (check browser DevTools)
- [ ] No 404s for images/CSS/JS

---

## 📝 CONTENT ACCURACY

- [ ] Business hours correct (if showing)
- [ ] Service areas listed (El Paso, TX)
- [ ] Pricing accurate (or "starting from")
- [ ] Testimonials are real (when you get them)
- [ ] Case studies accurate
- [ ] No typos or grammar mistakes
- [ ] Professional tone throughout
- [ ] Active voice, not passive

---

## 🔄 BACKUP & VERSION CONTROL

- [ ] Latest code pushed to GitHub
- [ ] All changes committed
- [ ] README updated
- [ ] .gitignore excludes sensitive files
- [ ] Backup of Vercel config
- [ ] Document any custom settings

---

## 🌐 DOMAIN & HOSTING

### Vercel Deployment:
- [ ] Connected to GitHub repo
- [ ] Auto-deploy on push enabled
- [ ] Custom domain connected (risingsun.digital)
- [ ] DNS configured correctly
- [ ] HTTPS forced
- [ ] www redirects to non-www (or vice versa)

### DNS Settings (Namecheap):
- [ ] A records pointing to Vercel
- [ ] CNAME for www
- [ ] MX records for email (if custom email)
- [ ] TXT record for domain verification

---

## 📧 EMAIL SETUP

- [ ] hello@risingsun.digital forwards to your inbox
- [ ] Can send/receive from professional email
- [ ] Email signature set up
- [ ] Auto-responder (optional)
- [ ] Spam filters configured

---

## 🎯 CONVERSION TRACKING

Test every conversion path:

**Path 1: PDF Download**
1. [ ] Land on homepage
2. [ ] Scroll to lead magnets
3. [ ] Fill form (2 fields)
4. [ ] Submit
5. [ ] Redirect to thank-you page
6. [ ] Receive email with PDF

**Path 2: Audit Request**
1. [ ] Land on homepage
2. [ ] Click "Get Free Audit"
3. [ ] Fill form (3 fields)
4. [ ] Submit
5. [ ] Redirect to thank-you
6. [ ] Receive confirmation email

**Path 3: Strategy Call**
1. [ ] Land on homepage
2. [ ] Click "Book Free Call"
3. [ ] Calendly loads
4. [ ] Select time
5. [ ] Fill details
6. [ ] Confirm booking
7. [ ] Receive calendar invite

---

## 🧠 USER TESTING

Get 3-5 people to test:
- [ ] Can they understand what you do in 5 seconds?
- [ ] Can they book a call without help?
- [ ] Can they download the PDF easily?
- [ ] Any confusing parts?
- [ ] Mobile experience smooth?
- [ ] Load time acceptable?

---

## 📱 LOCAL SEO

- [ ] Google My Business claimed
- [ ] Business name: Rising Sun Digital
- [ ] Category: Digital Marketing Agency
- [ ] Service area: El Paso, TX
- [ ] Hours listed (if applicable)
- [ ] Photos uploaded (logo, team, office if applicable)
- [ ] First review requested (from friend/family)

---

## 🚀 LAUNCH DAY CHECKLIST

**Morning of Launch:**
- [ ] Final mobile test
- [ ] Final desktop test
- [ ] Clear browser cache, test again
- [ ] Submit sitemap to Google
- [ ] Post on social media
- [ ] Email announce to contacts
- [ ] LinkedIn post
- [ ] Facebook/Instagram announcement

**First Week:**
- [ ] Monitor analytics daily
- [ ] Check for errors/bugs
- [ ] Respond to all inquiries <24hrs
- [ ] Ask first clients for feedback
- [ ] Document what's working

---

## ⚠️ COMMON MISTAKES TO AVOID

- ❌ Launching with broken forms
- ❌ Not testing on mobile
- ❌ Forgetting to set up analytics
- ❌ No clear CTA
- ❌ Slow page load
- ❌ Not submitting sitemap to Google
- ❌ Broken social links
- ❌ No 404 page
- ❌ Not testing conversion paths
- ❌ Launching without backup

---

## 🎯 POST-LAUNCH (Week 1)

- [ ] Check analytics daily
- [ ] Monitor conversion rate
- [ ] Review heatmaps (Clarity)
- [ ] Check for technical issues
- [ ] Test forms daily
- [ ] Respond to leads immediately
- [ ] Document learnings
- [ ] Plan first optimization

---

## 💰 REVENUE READINESS

- [ ] Payment method set up (Stripe/PayPal/Zelle)
- [ ] Contract/agreement template ready
- [ ] Onboarding process defined
- [ ] Project management tool ready
- [ ] Client communication system set
- [ ] Invoicing system ready

---

## 🔥 FINAL GO/NO-GO

**GO if:**
✅ All forms work
✅ Mobile looks good
✅ Analytics tracking
✅ No broken links
✅ Page loads <3 seconds
✅ At least 3 friends tested it
✅ Confident in delivery

**NO-GO if:**
❌ Forms don't work
❌ Mobile is broken
❌ Major bugs
❌ Not confident in offer
❌ Can't deliver on promises

---

## 🎊 LAUNCH!

When everything above is checked:

1. Push to production
2. Announce on all channels
3. Monitor closely for 48 hours
4. Celebrate 🎉
5. Start optimizing based on data

---

## 📞 EMERGENCY CONTACTS

If something breaks:
- Vercel Status: [vercel-status.com](https://vercel-status.com)
- GitHub Status: [githubstatus.com](https://githubstatus.com)
- Google Apps Status: [google.com/appsstatus](https://google.com/appsstatus)

---

**Remember:** Done is better than perfect. Launch, learn, optimize.

You've got this. 🔥
