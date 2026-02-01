import http.server
import socketserver
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

PORT = 1302

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
