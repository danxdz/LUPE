# Web OCR Scanner Application

A modern web-based OCR (Optical Character Recognition) application that extracts text from images using your camera or uploaded files. Built with vanilla HTML/JavaScript and powered by Tesseract.js.

## 🚀 Features

- **📷 Camera Capture**: Use your device camera to capture images in real-time
- **📁 File Upload**: Upload images from your device (drag & drop supported)
- **🔍 OCR Processing**: Extract text from images using Tesseract.js
- **📋 Copy to Clipboard**: Easily copy extracted text
- **📱 Mobile Responsive**: Works on desktop and mobile devices
- **🎨 Modern UI**: Beautiful, intuitive interface with smooth animations
- **⚡ Real-time Progress**: Visual feedback during OCR processing

## 📦 Files

1. **`index.html`** - Basic camera-only version
2. **`index-with-upload.html`** - Enhanced version with both camera and file upload
3. **`server.py`** - Simple Python HTTP server for local testing
4. **`vercel.json`** - Vercel deployment configuration
5. **`package.json`** - Project metadata and scripts

## 🛠️ Installation & Usage

### Quick Start (Local Development)

1. **Start the server:**
   ```bash
   python3 server.py
   ```

2. **Open in browser:**
   ```
   http://localhost:8000
   ```
   
3. **Choose your version:**
   - Basic version: `http://localhost:8000/index.html`
   - Enhanced version: `http://localhost:8000/index-with-upload.html`

### 🚀 Deploy to Vercel

#### Option 1: Deploy with Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Follow the prompts** and your app will be live!

#### Option 2: Deploy via GitHub

1. **Push to GitHub** (already done!)

2. **Go to [Vercel](https://vercel.com)**

3. **Import your GitHub repository:**
   - Click "New Project"
   - Import `danxdz/LUPE`
   - Click "Deploy"

4. **Your app will be live at:**
   - `https://your-project-name.vercel.app`

#### Option 3: Deploy with One Click

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/danxdz/LUPE)

### 🌐 Deploy to Other Platforms

#### GitHub Pages
1. Go to Settings → Pages
2. Select source: "Deploy from a branch"
3. Choose "main" branch and "/" (root)
4. Save and wait for deployment

#### Netlify
1. Drag and drop your project folder to [Netlify Drop](https://app.netlify.com/drop)
2. Or connect GitHub and auto-deploy

#### Static Hosting
This app works on any static hosting service since it's pure HTML/JS/CSS:
- AWS S3 + CloudFront
- Google Cloud Storage
- Azure Static Web Apps
- Surge.sh
- Render

### Alternative: Using Any HTTP Server

You can use any HTTP server. For example:

**Using Node.js:**
```bash
npx http-server -p 8000
```

**Using Python (alternative):**
```bash
python3 -m http.server 8000
```

## 📱 How to Use

### Camera Mode
1. Allow camera permissions when prompted
2. Position the text within the frame
3. Click "📸 Capture Image"
4. Wait for OCR processing
5. Copy the extracted text if needed

### Upload Mode (Enhanced Version)
1. Click "📁 Upload Image" tab
2. Either:
   - Click to browse and select an image
   - Drag and drop an image onto the upload area
3. Wait for OCR processing
4. Copy the extracted text

## 🔧 Technical Details

### Technologies Used
- **Tesseract.js v5**: JavaScript OCR library
- **MediaDevices API**: For camera access
- **Canvas API**: For image manipulation
- **File API**: For file uploads
- **Clipboard API**: For copying text

### Browser Requirements
- Modern browser with camera support
- HTTPS or localhost for camera access
- JavaScript enabled

### Supported Image Formats
- JPG/JPEG
- PNG
- GIF
- WebP

## ⚠️ Important Notes

1. **Camera Access**: Requires HTTPS or localhost due to browser security
2. **Performance**: OCR processing time depends on image size and quality
3. **Accuracy**: Best results with clear, well-lit text images
4. **Languages**: Currently configured for English text recognition
5. **Vercel Deployment**: Camera will work on Vercel since it provides HTTPS by default

## 🎯 Tips for Best Results

- **Good Lighting**: Ensure text is well-lit and clearly visible
- **Steady Camera**: Hold device steady when capturing
- **Clear Text**: Works best with printed text rather than handwriting
- **Contrast**: High contrast between text and background improves accuracy
- **Resolution**: Higher resolution images generally yield better results

## 🚀 Features Comparison

| Feature | Basic Version | Enhanced Version |
|---------|--------------|------------------|
| Camera Capture | ✅ | ✅ |
| File Upload | ❌ | ✅ |
| Drag & Drop | ❌ | ✅ |
| Mode Switching | ❌ | ✅ |
| Confidence Display | ❌ | ✅ |

## 📝 Customization

You can customize the OCR settings in the JavaScript code:

```javascript
// Add more languages
const worker = await Tesseract.createWorker(['eng', 'fra', 'deu']);

// Adjust OCR parameters
await worker.setParameters({
    tessedit_char_whitelist: '...',  // Allowed characters
    preserve_interword_spaces: '1',   // Keep spaces
});
```

## 🐛 Troubleshooting

**Camera not working?**
- Check browser permissions
- Ensure using HTTPS or localhost
- Try the upload mode instead

**OCR not accurate?**
- Use clearer images
- Ensure good lighting
- Try adjusting camera angle

**Server not starting?**
- Check Python is installed
- Ensure port 8000 is available
- Try a different port if needed

**Vercel deployment issues?**
- Make sure all files are committed
- Check Vercel dashboard for build logs
- Ensure repository is public or Vercel has access

## 📄 License

This project uses Tesseract.js which is licensed under Apache 2.0.

## 🎉 Ready to Use!

The application is ready to deploy or run locally. For instant deployment, use the Vercel button above!
