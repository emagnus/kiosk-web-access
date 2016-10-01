#!/usr/bin/env python
 
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class KioskWebAccessHandler(BaseHTTPRequestHandler):

  # GET requests
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
        f.close()
        self.send_response(303)
        self.send_header('Location', default_url)
        self.end_headers()
      except IOError:
        self.send_error(500, 'Error reading default URL file.')

    if self.path.endswith('help'):
      try:
        f = open('help.html')
        help_content = f.read()
        try:
          f = os.popen("/sbin/ifconfig wlan0 | grep 'inet\ addr' | cut -d: -f2 | cut -d' ' -f1")
          wlan0 = f.read();
          f = os.popen("/sbin/ifconfig eth0 | grep 'inet\ addr' | cut -d: -f2 | cut -d' ' -f1")
          eth0 = f.read();
          help_content = help_content.replace('wlan0', wlan0)
          help_content = help_content.replace('eth0', eth0)
        except IOError:
          print('Fant ingen nettverksadresser')
        self.send_ok_response(help_content)
      except IOError:
        self.send_error(500, 'Error reading help-file.')


  # POST requests
  def do_POST(self):  
    if self.path.endswith('goto'):
      given_url = self.rfile.read(int(self.headers.getheader('Content-Length')))
      self.go_to_url(given_url)

      self.send_ok_response('URL (' + given_url + ') successfully loaded.')
    
    if self.path.endswith('default'):
      given_url = self.rfile.read(int(self.headers.getheader('Content-Length')))
      try:
        f = open('default.url.cfg')
        f.truncate()
        f.write(given_url)
        f.close()
        
        self.send_ok_response('Default URL was successfully updated to ' + given_url)
      except IOError:
        self.send_error(500, 'Error writing default URL file.')

  def go_to_url(self, url):
    subprocess.call(['./go_to_url.sh', url])

  def send_ok_response(self, response_text):
    self.send_response(200)
    self.send_header('Content-type','text/html')
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