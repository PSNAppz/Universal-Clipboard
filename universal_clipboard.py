# universal clipboard for all platforms
# Steps 

# Create a channel and set the clipboard to it
# Wait for a message from the channel
# Set the clipboard to the message


import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

sio.connect('http://localhost:5007')   
sio.wait() 
