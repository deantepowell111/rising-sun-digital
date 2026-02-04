# Google Sheets Auto-Send + HubSpot Capture (100% Free)

This setup keeps your onsite forms, auto-sends the PDF, saves leads to Google Sheets, and forwards every submission into HubSpot using the free Forms API.

## What You Will Build
- A Google Sheet that stores every submission
- A Google Apps Script web app that:
  - Writes rows to the sheet
  - Sends the right email based on form type
  - Forwards the lead to HubSpot
  - Redirects users to your thank-you page

## Step 1: Create the Google Sheet
1. Go to sheets.google.com and create a new sheet named `Rising Sun Leads`.
2. Add these headers in Row 1:
   - Date
   - Email
   - Form Type
   - Website URL
   - Status

## Step 2: Create HubSpot Forms (Free)
1. In HubSpot, create two forms:
   - `Digital Growth Blueprint`
   - `Website Audit Request`
2. Copy the Form GUID for each form.
3. Find your HubSpot `portalId` (visible in your HubSpot URL or account settings).

## Step 3: Create the Apps Script
1. In the Google Sheet, click Extensions -> Apps Script.
2. Delete any boilerplate and paste the script below.
3. Update these constants:
   - `PDF_URL`
   - `HUBSPOT_PORTAL_ID`
   - `HUBSPOT_PDF_FORM_GUID`
   - `HUBSPOT_AUDIT_FORM_GUID`

```javascript
const SHEET_NAME = 'Rising Sun Leads';
const PDF_URL = 'https://drive.google.com/file/d/1iG19-syvTmsolIpTizt_RFB6ZZcMe9Gp/view?usp=drive_link';
const HUBSPOT_PORTAL_ID = '245055639';
const HUBSPOT_PDF_FORM_GUID = '8c4c68d7-6bb3-4efa-a174-2ebecb7f18f8';
const HUBSPOT_AUDIT_FORM_GUID = '3c0a6313-e659-49f5-b6e2-54fd7c44bed7';

function doPost(e) {
  const data = e.parameter || {};
  const sheet = getOrCreateSheet_();

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Date', 'First Name', 'Last Name', 'Email', 'Phone', 'Has Website', 'Website URL', 'Challenge', 'Form Type', 'Status', 'HubSpot Status']);
  }

  const now = new Date();
  let hubspotStatus = 'Not Sent';

  // Forward to HubSpot (non-blocking)
  try {
    hubspotStatus = forwardToHubSpot_(data);
  } catch (err) {
    hubspotStatus = 'Error';
    Logger.log('HubSpot forward error: ' + err);
  }

  sheet.appendRow([
    now,
    data.firstname || '',
    data.lastname || '',
    data.email || '',
    data.phone || '',
    data.has_website || '',
    data.website || '',
    data.challenge || '',
    data.form_type || '',
    'New',
    hubspotStatus
  ]);

  if (data.email) {
    if (data.form_type === 'Digital Growth Blueprint') {
      sendPdfEmail_(data.email);
    } else if (data.form_type === 'Website Audit Request') {
      sendAuditEmail_(data.email, data.website || '');
    }
  }

  const redirect = data.redirect || 'https://risingsun.digital/thank-you.html';
  return HtmlService.createHtmlOutput(
    '<html><head><meta http-equiv="refresh" content="0; url=' + redirect + '"></head></html>'
  );
}

function doGet() {
  return HtmlService.createHtmlOutput('OK');
}

function getOrCreateSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) sheet = ss.insertSheet(SHEET_NAME);
  return sheet;
}

function sendPdfEmail_(email) {
  const subject = 'Your Free Digital Growth Blueprint is Ready';
  const body =
    'Hi there,

' +
    'Thanks for downloading the Digital Growth Blueprint.

' +
    'Download your free PDF here:
' + PDF_URL + '

' +
    'Questions? Just reply to this email or call us at (915) 234-3570.

' +
    'Best,
Rising Sun Digital Team
www.risingsun.digital';
  GmailApp.sendEmail(email, subject, body);
}

function sendAuditEmail_(email, website) {
  const subject = 'Your Free Website Audit is Coming';
  const body =
    'Hi there,

' +
    'We received your website audit request for: ' + website + '

' +
    'Our team will analyze your site and send a detailed report within 48 hours.

' +
    'Talk soon,
Rising Sun Digital Team
(915) 234-3570';
  GmailApp.sendEmail(email, subject, body);
}

function forwardToHubSpot_(data) {
  const formGuid = data.form_type === 'Digital Growth Blueprint'
    ? HUBSPOT_PDF_FORM_GUID
    : HUBSPOT_AUDIT_FORM_GUID;

  const url = 'https://api.hsforms.com/submissions/v3/integration/submit/' + HUBSPOT_PORTAL_ID + '/' + formGuid;

  const payload = {
    fields: [
      { name: 'firstname', value: data.firstname || '' },
      { name: 'lastname', value: data.lastname || '' },
      { name: 'email', value: data.email || '' },
      { name: 'phone', value: data.phone || '' },
      { name: 'website', value: data.website || '' },
      { name: 'has_website', value: data.has_website || '' },
      { name: 'challenge', value: data.challenge || '' },
      { name: 'form_type', value: data.form_type || '' }
    ]
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(url, options);
  const code = response.getResponseCode();
  if (code >= 200 && code < 300) return 'OK ' + code;
  return 'Error ' + code + ': ' + response.getContentText();
}
```

## Step 4: Deploy the Web App
1. Click Deploy -> New deployment.
2. Select type: Web app.
3. Execute as: Me.
4. Who has access: Anyone.
5. Click Deploy and copy the Web app URL.

## Step 5: Update the Website Forms
In `index.html`, replace `YOUR_SCRIPT_ID` with your Web app URL in both forms.

The form actions are already set to:
- `https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec`

## Step 6: Test
1. Submit each form with your email.
2. Confirm a new row appears in the sheet.
3. Confirm you receive the correct email.
4. Confirm the contact shows in HubSpot.

## Notes
- This is completely free.
- HubSpot free tier supports the Forms API.

## HubSpot Properties Note
Make sure these properties exist in HubSpot (they can be custom):
- `challenge` (Dropdown with options: Traffic, Conversions, Brand, SEO, Ads, Other)
- `has_website` (Dropdown with options: Yes, No)
