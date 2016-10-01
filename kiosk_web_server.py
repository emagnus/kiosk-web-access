#!/usr/bin/env python
 
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class KioskWebAccessHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path.endswith('default'):
      try:
        f = open('default.url.cfg')
        default_url = f.read()
        self.go_to_url(default_url)

        self.send_ok_response('Default URL (' + default_url + ') successfully loaded.')
      except IOError:
        self.send_error(500, 'Error reading default URL file.')

    if self.path.endswith('autostart'):
      try:
        f = open('default.url.cfg')
        default_url = f.read()
        self.send_response(303)
        self.send_header('Location', default_url)
        self.end_headers()
      except IOError:
        self.send_error(500, 'Error reading default URL file.')


  def do_POST(self):  
    if self.path.endswith('goto'):
        given_url = self.rfile.read(int(self.headers.getheader('Content-Length')))
        self.go_to_url(given_url)

        self.send_ok_response('URL (' + given_url + ') successfully loaded.')

  def go_to_url(self, url):
    subprocess.call(['./go_to_url.sh', url])

  def send_ok_response(self, response_text):
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