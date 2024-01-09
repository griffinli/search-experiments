from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        args = parse.urlsplit(s).query
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = requests.get(f"https://www.googleapis.com/customsearch/v1?key={os.environ['GOOGLE_KEY']}&cx={os.environ['GOOGLE_CX']}&{args}")
        self.wfile.write(message.text.encode())
        return