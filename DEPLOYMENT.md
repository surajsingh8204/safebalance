# SafeBalance - Deployment Guide 🚀

## Quick Deployment Options

### Option 1: Render.com (Recommended - Free & Easy)

1. **Create GitHub Repository**
   ```powershell
   cd "c:\Users\Suraj\Desktop\coding\mlproject\bankruptcy prediction"
   git init
   git add .
   git commit -m "Initial commit - SafeBalance bankruptcy prediction app"
   ```

2. **Push to GitHub**
   - Go to https://github.com/new
   - Create a new repository named "safebalance"
   - Run:
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/safebalance.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Render**
   - Go to https://render.com
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect settings from `render.yaml`
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at: `https://safebalance.onrender.com`

**Pros**: Free tier, auto-deploys on git push, HTTPS included
**Cons**: Sleeps after 15 min inactivity (wakes up in ~30 seconds)

---

### Option 2: Railway.app (Free with GitHub Student Pack)

1. **Push to GitHub** (same as above)

2. **Deploy on Railway**
   - Go to https://railway.app
   - Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add environment variable: `PORT=5000`
   - Railway will auto-deploy
   - Live at: `https://safebalance-production.up.railway.app`

**Pros**: Fast, always-on, great free tier
**Cons**: Requires GitHub Student Pack for extended free usage

---

### Option 3: Vercel (Serverless)

1. Install Vercel CLI:
   ```powershell
   npm install -g vercel
   ```

2. Create `vercel.json`:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. Deploy:
   ```powershell
   cd "c:\Users\Suraj\Desktop\coding\mlproject\bankruptcy prediction"
   vercel
   ```

**Pros**: Fast, free, global CDN
**Cons**: Serverless (cold starts), limited to 10 second execution time

---

### Option 4: PythonAnywhere (Simple)

1. Go to https://www.pythonanywhere.com
2. Sign up for free account
3. Upload your files via "Files" tab
4. Install requirements in Bash console:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure web app in "Web" tab
6. Live at: `https://yourusername.pythonanywhere.com`

**Pros**: Very simple, Python-focused
**Cons**: Limited free tier, slower

---

### Option 5: Ngrok (Temporary Testing)

For quick internet access without deployment:

```powershell
# Install ngrok from https://ngrok.com/download
ngrok http 5000
```

This creates a temporary public URL like: `https://abc123.ngrok.io`

**Pros**: Instant, no code changes
**Cons**: Temporary URL, requires running locally

---

## Recommended: Render Deployment Steps

### Step 1: Initialize Git (if not already done)
```powershell
cd "c:\Users\Suraj\Desktop\coding\mlproject\bankruptcy prediction"
git init
git add .
git commit -m "SafeBalance - Corporate Bankruptcy Prediction System"
```

### Step 2: Create GitHub Repository
1. Visit: https://github.com/new
2. Repository name: `safebalance`
3. Keep it public (for free hosting)
4. Don't initialize with README (already have one)
5. Click "Create repository"

### Step 3: Push to GitHub
```powershell
git remote add origin https://github.com/YOUR_USERNAME/safebalance.git
git branch -M main
git push -u origin main
```

### Step 4: Deploy on Render
1. Visit: https://render.com
2. Click "Get Started" or "Sign Up"
3. Sign up with GitHub
4. Click "New +" → "Web Service"
5. Click "Connect GitHub" → Find your `safebalance` repo
6. Settings will auto-populate from `render.yaml`:
   - Name: `safebalance`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. Click "Create Web Service"
8. Wait 5-10 minutes for build

### Step 5: Access Your Live App
Your app will be live at: `https://safebalance.onrender.com`

---

## Files Created for Deployment

✅ `Procfile` - Heroku/Render deployment config
✅ `render.yaml` - Render.com configuration
✅ `runtime.txt` - Python version specification
✅ `requirements.txt` - Updated with gunicorn

---

## Important Notes

1. **First Load**: Render free tier sleeps after 15 min inactivity. First load takes ~30 seconds to wake up.

2. **Custom Domain**: You can add your own domain in Render settings (free)

3. **Environment Variables**: Add in Render dashboard if needed

4. **Logs**: Check Render dashboard → Logs tab for debugging

5. **Auto-Deploy**: Every `git push` to main branch will auto-deploy

---

## Need Help?

- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- Vercel Docs: https://vercel.com/docs

**Your SafeBalance app is ready to go live! 🎉**
