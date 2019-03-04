"""Simple HTTP Server extension to implement PUT requests.

This module builds on BaseHTTPServer by implementing PUT requests.

"""

__version__ = "0.1"

import os
import sys
import os.path
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class PutHTTPServer(SimpleHTTPRequestHandler):
    """Simple HTTP request handler with PUT command.

    This saves files to the current directory.

    """

    server_version = "PutHTTP/" + __version__

    def do_PUT(self):
        """Server a PUT request."""
        filename = self.path.lstrip('/')

        no_errors = True

        # Used to track whether to send a 201 response
        file_is_new = True

        # Send a 200 response if we overwrite the file
        if os.path.isfile(filename):
            file_is_new = False

        try:
            # Read file from the request
            content_length = int(self.headers.getheader('Content-Length'))
            content = self.rfile.read(content_length)

            # Write file to current directory
            with open(filename, 'w') as destfile:
                destfile.write(content)

        except Exception as e:
            no_errors = False
            print(str(e))
            self.send_error(500, 'Internal Server Error')
            self.end_headers()

        finally:
            if no_errors:
                if file_is_new:
                    self.send_response(201)
                else:
                    self.send_response(200)

                self.end_headers()

def test(HandlerClass = PutHTTPServer,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)

if __name__ == '__main__':
    test()
