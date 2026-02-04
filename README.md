# Rising Sun Digital - Website Deployment Guide

## 🚀 Free Hosting Setup (GitHub Pages)

### Step 1: Create a GitHub Account
1. Go to https://github.com/signup
2. Create a free account if you don't have one

### Step 2: Create a New Repository
1. Click the "+" icon in the top right → "New repository"
2. Name it: `risingsun-digital`
3. Make it **Public**
4. Click "Create repository"

### Step 3: Upload Your Website Files
1. Click "uploading an existing file"
2. Drag and drop ALL files from this folder:
   - `index.html`
   - `rising sun logo.png` (once added)
   - Any other images you add
3. Scroll down and click "Commit changes"

### Step 4: Enable GitHub Pages
1. Go to Settings (in your repository)
2. Click "Pages" in the left sidebar
3. Under "Source", select "main" branch
4. Click "Save"
5. Wait 1-2 minutes

Your site will be live at: `https://yourusername.github.io/risingsun-digital/`

---

## 🌐 Connect Your Custom Domain (risingsun.digital)

### After GitHub Pages is live:

1. **In GitHub Settings → Pages:**
   - Enter `risingsun.digital` in the "Custom domain" field
   - Click "Save"

2. **In Your Domain Registrar (where you bought risingsun.digital):**
   Add these DNS records:

   **A Records (for apex domain):**
   ```
   Type: A
   Name: @
   Value: 185.199.108.153

   Type: A
   Name: @
   Value: 185.199.109.153

   Type: A
   Name: @
   Value: 185.199.110.153

   Type: A
   Name: @
   Value: 185.199.111.153
   ```

   **CNAME Record (for www):**
   ```
   Type: CNAME
   Name: www
   Value: yourusername.github.io
   ```

3. **Wait 24-48 hours** for DNS to propagate
4. Enable "Enforce HTTPS" in GitHub Pages settings

---

## 📁 File Structure
```
risingsun-digital/
├── index.html          (your main website)
├── rising-sun-logo.png (your logo)
└── og-image.jpg        (social media image - optional)
```

---

## 🆓 Alternative Free Hosting Options

### **Netlify** (Easiest, recommended!)
1. Go to https://netlify.com
2. Sign up with GitHub
3. Drag and drop your folder
4. Connect domain in Settings → Domain management

### **Vercel**
1. Go to https://vercel.com
2. Import your GitHub repo
3. Deploy automatically

### **Cloudflare Pages**
1. Go to https://pages.cloudflare.com
2. Connect GitHub
3. Deploy your site

---

## ✅ Next Steps
1. Find your logo file and tell me the path
2. I'll integrate it into the HTML
3. Choose a hosting option above
4. Upload your site
5. Connect risingsun.digital

Need help with any step? Just ask!
