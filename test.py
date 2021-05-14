import asyncio
import socketio
import threading
import sys
import time

sio = socketio.Client()


def callback(data):
    print("Callback")
    print(data)


@sio.event
def connect():
    print('connection established')


@sio.event
def update_game(data):
    callback(data)
    print('message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


def main():
    sio.connect('http://tp-project2021.herokuapp.com')
    sio.wait()
    sio.disconnect()


def run_loop():
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            sio.disconnect()
            #print("bad")


if __name__ == '__main__':
    try:
        thread = threading.Thread(target=run_loop)
        thread.start()
    except Exception as e:
        print("Thread error")
        print(e)
        sio.disconnect()
    i = 1
    while True:
        print(i)
        i += 1
        time.sleep(0.5)