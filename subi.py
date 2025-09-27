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

"""
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