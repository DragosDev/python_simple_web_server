import http.server
import socketserver
import os

def run_server(port=8080, web_dir='web'):
    os.chdir(web_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)

    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
