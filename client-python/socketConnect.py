import socketio
import threading

SIO = None

def init():
    sio = socketio.Client()

    @sio.event
    def connect():
        sio.emit('adminInit')
        print('connection established')


    @sio.event
    def disconnect():
        print('disconnected from server')


    sio.connect('http://localhost:5000')
    
    wait_thread = threading.Thread(target=sio.wait)
    wait_thread.start()

    return sio

def getSio():
    global SIO

    if SIO is None:
        SIO = init()

    return SIO

def defaultConnect():
    sio = getSio()

def closeConnection():
    sio = getSio()
    sio.disconnect()