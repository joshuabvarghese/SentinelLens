import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "." # Root directory of your project

class MonitoringHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Crucial: This allows the dashboard to read the JSON file
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/dashboard.html'
        return super().do_GET()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), MonitoringHTTPRequestHandler) as httpd:
        print(f"🚀 Dashboard running at http://localhost:{PORT}")
        httpd.serve_forever()