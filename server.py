from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 5000
FILE = "calculator.html"

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == f"/{FILE}":
            try:
                with open(FILE, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(f.read())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Server Error: {e}".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    server = HTTPServer(("", PORT), MyHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
