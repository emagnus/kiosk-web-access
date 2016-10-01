#!/usr/bin/env python
 
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import subprocess

class KioskWebAccessHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path.endswith('default'):
      try:
        f = open('default.url.cfg')
        default_url = f.read()
        self.go_to_url(default_url)

        self.send_response('Default URL (' + default_url + ') successfully loaded.')
      except IOError:
        self.send_error(500, 'Error reading default URL file.')
  
  def do_POST(self):  
    if self.path.endswith('goto'):
        url = self.rfile.read(int(self.headers.getheader('Content-Length')))
        self.go_to_url(url)

        self.send_response('URL (' + url + ') successfully loaded.')

  def go_to_url(url):
    subprocess.call(['./go_to_url.sh', url])

  def send_response(response_text):
    self.send_response(200)
    self.send_header('Content-type','text-html')
    self.end_headers()
    self.wfile.write(response_text)

def run():
  print('Kiosk Web Access HTTP server is starting...')
  server_address = ('', 31337)
  httpd = HTTPServer(server_address, KioskWebAccessHandler)
  print('HTTP server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()