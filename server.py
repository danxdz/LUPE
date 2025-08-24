#!/usr/bin/env python3
"""
Simple HTTP server for testing the OCR web application.
This server is needed because camera access requires HTTPS or localhost.
"""

import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for camera access
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"\n🚀 OCR Web App Server Started!")
        print(f"📷 Open your browser and navigate to:")
        print(f"   http://localhost:{PORT}")
        print(f"\n⚠️  Note: Camera access requires either:")
        print(f"   - Using localhost (recommended)")
        print(f"   - Using HTTPS (for remote access)")
        print(f"\n📝 Instructions:")
        print(f"   1. Allow camera permissions when prompted")
        print(f"   2. Point camera at text you want to extract")
        print(f"   3. Click 'Capture Image' button")
        print(f"   4. Wait for OCR processing")
        print(f"   5. Copy extracted text if needed")
        print(f"\nPress Ctrl+C to stop the server\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped successfully")
            sys.exit(0)

if __name__ == "__main__":
    run_server()