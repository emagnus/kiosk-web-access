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

		    #send code 200 response
		    self.send_response(200)

		    #send header first
		    self.send_header('Content-type','text-html')
		    self.end_headers()

		    subprocess.call(['./go_to_url.sh', default_url])

		    #send file content to client
		    self.wfile.write('Default URL (' + default_url + ') successfully loaded.')
		    return
		  except IOError:
      	self.send_error(500, 'Error reading default URL file.')

def run():
  print('Kiosk Web Access HTTP server is starting...')
  server_address = ('', 31337)
  httpd = HTTPServer(server_address, KioskWebAccessHandler)
  print('HTTP server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()