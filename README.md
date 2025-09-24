# EX01 Developing a Simple Webserver
## Date:05/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>WEB</title>
    </head>
    <body>
        <h1 align = "center">DEVICE SPECIFICATION - 25014966</h1>
        <table border="2" align = "center" cellspacing="3"> 
            <tr>
                <th bgcolor="yellow">S.NO</th>
                <th bgcolor="yellow">DEVICE SPECIFICATION</th>
                <th bgcolor="yellow">DESCRIPTION</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>STORAGE</td>
                <td>512</td>
            </tr>
            <tr> 
                <td>2.</td>
                <td>GRAPHICS CARD</td>
                <td>4GB RTX2050</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>PROCESSOR</td>
                <td>AMD RYZEN 7 7453HS</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>WINDOWS</td>
                <td>11</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>MODEL</td>
                <td>11</td>
            </tr>
            <tr>
                <td>5.</td>
                <td>MODEL</td>
                <td>HP I5</td>
            </tr >
        </table>
    </body>
</html>
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot (1).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
