# Form Setup (Onsite Forms + HubSpot Capture)

Your onsite forms stay in place. A free Google Apps Script web app handles:
- Sending the PDF or audit confirmation
- Saving leads to Google Sheets
- Forwarding submissions into HubSpot

## Step 1: Apps Script
Follow `AUTO-SEND-SETUP.md` to:
- Create the Google Sheet
- Paste the script
- Add your HubSpot portalId + form GUIDs
- Deploy the web app

## Step 2: Update Form Actions
Open `index.html` and replace `YOUR_SCRIPT_ID` with your web app URL in both forms.

You should see:
- `https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec`

## Step 3: Test
1. Submit each form with a test email.
2. Confirm the lead shows in Google Sheets.
3. Confirm the correct email is sent.
4. Confirm the contact appears in HubSpot.

If you want to switch to native HubSpot embedded forms later, just say the word.
