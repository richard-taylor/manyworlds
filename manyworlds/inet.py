''' inet module.
'''

import threading
import time

class Reader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tick = 0
        self.running = True
        
    def run(self):
        while (self.running and self.tick < 100):
            print("Reader tick " + str(self.tick))
            self.tick += 1
            time.sleep(1)

    def stop(self):
        self.running = False

class Writer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tick = 0
        self.running = True
        
    def run(self):
        while (self.running and self.tick < 100):
            print("Writer tick " + str(self.tick))
            self.tick += 1
            time.sleep(1)

    def stop(self):
        self.running = False
        
class Net():
    '''
    Implementation of the inet interface using threads and sockets.
    '''
    def __init__(self, client):
        self.reader = Reader()
        self.reader.start()
        self.writer = Writer()
        self.writer.start()

    def close(self):
        self.reader.stop()
        self.writer.stop()