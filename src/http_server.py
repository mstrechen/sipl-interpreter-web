import os

from http.server import BaseHTTPRequestHandler, HTTPServer

from utility.url import parse_path
import utility as utility
import api.methods as api_methods


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers_success(self, content_type: str = 'text/html; charset=utf-8'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _set_headers_error(self, errno: int = 404):
        self.send_response(errno)
        self.end_headers()


    def do_GET(self):
        root = os.path.join(os.getcwd(), 'static')
        filename, fullpath, filetype, args = parse_path(root, self.path)

        if filetype in utility.url.static_ext_list and os.path.isfile(fullpath):
            self._set_headers_success(utility.url.static_ext_list.get(filetype))
            with open(fullpath, 'rb') as data_stream:
                data = data_stream.read()
                self.wfile.write(data)
        elif filename in api_methods.available_get:
            method = api_methods.available_get.get(filename)
            try:
                res = method(args)
                self._set_headers_success()
                self.wfile.write(bytes(res, "utf8"))
            except Exception as e:
                print("Something went wrong", e)
                self._set_headers_error(500)
        else:
            self._set_headers_error()

    def do_POST(self):
        root = os.path.join(os.getcwd(), 'static')
        filename, fullpath, filetype, args = parse_path(root, self.path)
        print(filename, fullpath, filetype)
        method = api_methods.available_post.get(filename)
        if method is None:
            self._set_headers_error(404)
            return
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body = post_body.decode('utf8')
        try:
            res = method(args, {}, post_body)
            self._set_headers_success()
            self.wfile.write(bytes(res, "utf8"))
        except Exception as e:
            print("Something went wrong", e)
            self._set_headers_error(500)


def run_http_server(port):
    print('starting server on port', port, '...')
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()