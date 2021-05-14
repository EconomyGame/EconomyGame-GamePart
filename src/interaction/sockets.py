import socketio
import threading


def empty(*args, **kwargs):
    pass


sio = socketio.Client()
callback_func = empty


@sio.event
def connect():
    print('connection established')


@sio.event
def update_game(data):
    callback_func(data)
    print('message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


def run_loop(callback):
    global callback_func
    callback_func = callback
    while True:
        try:
            sio.connect('http://tp-project2021.herokuapp.com')
            sio.wait()
        except Exception as e:
            print(e)
            sio.disconnect()


def start_thread(callback):
    thread = threading.Thread(target=run_loop, args=(callback,))
    thread.start()
