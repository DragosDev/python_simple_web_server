# Simple Web Server In Python
A simple web server to access your files from a directory

# What is doing this code:
This a server in Python using the http.server, socketserver and os modules to serve file from a local folder called myfiles. The server is running on localhost on port 8080 , feel free to change as you want.

```python
import http.server
import socketserver
import os

def run_server(port=8080, web_dir='myfiles'):
    os.chdir(web_dir)

    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)

    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
    
```
# How is working this code:

We are importing the required modules:

<strong>http.server</strong> - with this module we are the classes to implement the web server to serve the static file such as HTML, CSS and JS or images etc.

<strong>socketserver</strong> - with this module or toolbox we are setting up our server. In simple terms you can think that you will have a vending machine to serve your customers but you will not need to worry about how to build the machine, how to place the products inside or handle the money.

You have two different types of servers TCP and UDP which are connected through sockets or virtual pipes to deliver the requests to your clients.

<strong>os</strong> - this module is helping you to interact with your operating system for example giving paths , renaming, deleting files etc.

2. Defining the run_server function

<strong>port= 8080</strong> - this is the parameter to define the port where our server will run

web_dir='web' - this is the path of the folder where our files will be stored, you can give the full path if your folder is having a different location from where your Python program will run.

os.chdir(webdir) - this is the parameter where we are asking the program to change the current working directory to the web directory.

Handler = http.server.SimpleHTTPRequestHandler - here we are asking the program to serve the files from the current directory in our case web to map the directory structure to HTTP requests. This acts like a way of sharing your files through a special window.

httpd = socketserver.TCPServer(("", port), Handler) - with this line we are telling to our server to give us the files on a specified port and in a specific way. The Handler parameter is helping the server to share our files with us.

print(f"Serving on port {port}") - is printing a message for us together with the port number

httpd.serve_forever() - this a parameter where we are telling to our server to run without stop until we are stopping it.
