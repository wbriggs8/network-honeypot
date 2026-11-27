import socket
# think of a socket as an endpoint for sending and receiving bytes
HOST = "127.0.0.1"
PORT = 2222
# opens 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # binds the host and port to the server
    server.bind(HOST, PORT)
    # tells the server to listen on port 2222, maybe set a timed queue? decision for later
    server.listen()
    server.accept() # need to work on

# question for myself, what kind of behavior do I need the server/socket to handle?

