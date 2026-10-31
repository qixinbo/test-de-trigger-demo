from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

def normalize_name(name):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return " ".join(name.strip().split())

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/normalize":
            query = parse_qs(parsed.query, keep_blank_values=True)
            name = query.get("name", [""])[0]
            payload = json.dumps({"name": normalize_name(name)}, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(payload)
            return
        self.send_response(200 if parsed.path == "/health" else 404)
        self.end_headers()
        self.wfile.write(b"healthy")

if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
