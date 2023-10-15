import http.server
import socketserver

class ICSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith(".ics"):
            return "text/calendar"
        return super().guess_type(path)

if __name__ == "__main__":
    PORT = 8000
    Handler = ICSHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
