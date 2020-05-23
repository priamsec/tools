from http.server import HTTPServer,SimpleHTTPRequestHandler
from socketserver import BaseServer
import ssl

httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, keyfile='/etc/ssl/private/server.key', certfile='/etc/ssl/certs/server.crt', server_side=True)
httpd.serve_forever()
