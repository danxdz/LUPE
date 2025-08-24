# Web OCR Scanner Application

A modern web-based OCR (Optical Character Recognition) application that extracts text from images using your camera or uploaded files. Built with vanilla HTML/JavaScript and powered by Tesseract.js.

## 🚀 Live Demo

Deploy your own version instantly:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/danxdz/LUPE)

## ✨ Features

- **📷 Camera Capture**: Use your device camera to capture images in real-time
- **📁 File Upload**: Upload images from your device (drag & drop supported)
- **🔍 OCR Processing**: Extract text from images using Tesseract.js
- **📋 Copy to Clipboard**: Easily copy extracted text
- **📱 Mobile Responsive**: Works on desktop and mobile devices
- **🎨 Modern UI**: Beautiful, intuitive interface with smooth animations
- **⚡ Real-time Progress**: Visual feedback during OCR processing

## 📦 Files

- **`index.html`** - Main application with camera and upload support
- **`index-basic.html`** - Basic camera-only version
- **`README.md`** - This documentation

## 🚀 Deploy to Vercel (Recommended)

### Option 1: One-Click Deploy
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/danxdz/LUPE)

### Option 2: Import from GitHub
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import `danxdz/LUPE`
4. Click "Deploy"

### Option 3: Vercel CLI
```bash
npx vercel
```

## 🌐 Deploy to Other Platforms

### Netlify
- Drag and drop the project folder to [Netlify Drop](https://app.netlify.com/drop)
- Or connect GitHub for auto-deploy

### GitHub Pages
1. Go to Settings → Pages
2. Source: Deploy from branch
3. Branch: main / (root)
4. Save

### Any Static Host
Works on any static hosting:
- Surge.sh: `npx surge`
- Render.com
- Firebase Hosting
- AWS S3 + CloudFront

## 💻 Local Development

### Option 1: Python HTTP Server
```bash
python3 -m http.server 8000
```

### Option 2: Node.js HTTP Server
```bash
npx http-server
```

### Option 3: VS Code Live Server
Install "Live Server" extension and right-click → "Open with Live Server"

Then open: `http://localhost:8000`

## 📱 How to Use

### Camera Mode
1. Allow camera permissions when prompted
2. Position text within the frame
3. Click "📸 Capture Image"
4. Wait for OCR processing
5. Copy extracted text

### Upload Mode
1. Click "📁 Upload Image" tab
2. Click to browse or drag & drop an image
3. Wait for OCR processing
4. Copy extracted text

## 🔧 Technical Details

- **Tesseract.js v5** - OCR processing
- **MediaDevices API** - Camera access
- **Canvas API** - Image manipulation
- **File API** - File uploads
- **No backend required** - Runs entirely in browser
- **No build process** - Pure HTML/JS/CSS

## 📝 Browser Requirements

- Modern browser (Chrome, Firefox, Safari, Edge)
- HTTPS or localhost for camera
- JavaScript enabled

## 🎯 Tips for Best OCR Results

- ✅ Good lighting
- ✅ Clear, printed text
- ✅ High contrast
- ✅ Steady camera
- ✅ Proper focus

## ⚠️ Troubleshooting

**Camera not working?**
- Check permissions in browser settings
- Must use HTTPS or localhost
- Try upload mode as alternative

**OCR not accurate?**
- Use clearer image
- Ensure good lighting
- Try different angle

**Deployment issues?**
- Make sure repository is public
- Check Vercel has GitHub access
- Try deploying without config files

## 📄 License

Open source - uses Tesseract.js (Apache 2.0)

---

**Ready to deploy!** Click the Vercel button above for instant deployment 🚀
