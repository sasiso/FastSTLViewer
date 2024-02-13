import http.server
import socketserver
import os
import subprocess
class HTMLOnlyHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        # Override list_directory to filter and show only .html files
        try:
            list = os.listdir(path)
            html_files = [f for f in list if f.endswith('.html')]
            
            # Return HTML content with only .html files
            return '\n'.join(sorted(html_files))
        except OSError:
            self.send_error(404, "No permission to list directory")

    def translate_path(self, path):
        # Override translate_path to handle .html files only
        path = super().translate_path(path)
        if os.path.isdir(path):
            # If it's a directory, add /index.html to the path
            return os.path.join(path, 'index.html')
        elif not path.endswith('.html'):
            # If it's not an .html file, return a 404 error
            self.send_error(404, "File not found")
            return None
        else:
            return path

# Find and set the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

# Specify the port you want to use
port = 8000

# Set up the HTTP server with the custom handler
Handler = HTMLOnlyHandler
httpd = socketserver.TCPServer(("", port), Handler)

print(f"Serving at http://localhost:{port} from {current_directory}")

# Hardcoded paths for browsers
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Try launching Google Chrome
try:
    subprocess.run([chrome_path, f"http://localhost:{port}"])
except FileNotFoundError:
    # If Chrome is not found, try launching Microsoft Edge
    try:
        subprocess.run([edge_path, f"http://localhost:{port}"])
    except FileNotFoundError:
        print("Neither Chrome nor Edge found. Please make sure at least one of them is installed.")

# Start the server
httpd.serve_forever()
