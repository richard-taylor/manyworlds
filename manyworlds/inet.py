''' inet module.
'''

import collections
import socket
import threading
import time

import manyworlds.message

class Reader(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.inQueue = collections.deque()    # thread-safe
        self.running = True
        
    def run(self):
        while (self.running):
            try:
                data, address = self.socket.recvfrom(manyworlds.message.MAX_PACKET_BYTES)
                
                packet = manyworlds.message.Packet(address, data)
                self.inQueue.append(packet)
                
            except socket.timeout:
                pass    # there is no data to read yet
            except ConnectionResetError:
                pass    # on Windows if there is no server running on this machine
    
    def poll(self):
        if len(self.inQueue) > 0:
            return self.inQueue.pop()
        return None

    def stop(self):
        self.running = False

class Writer(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.outQueue = collections.deque()    # thread-safe
        self.running = True
        
    def run(self):
        while (self.running):
            if len(self.outQueue) > 0:
                packet = self.outQueue.pop()
                self.socket.sendto(packet.data, packet.address)
        
    def send(self, packet):
        self.outQueue.append(packet)
            
    def stop(self):
        self.running = False
        
class Net():
    '''
    Implementation of the inet interface using threads and sockets.
    '''
    def __init__(self, listenPort):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # UDP socket
        self.socket.bind(("", listenPort))
        self.socket.settimeout(1)
        
        self.reader = Reader(self.socket)
        self.writer = Writer(self.socket)
    
    def start(self):
        self.reader.start()
        self.writer.start()
    
    def poll(self):
        '''
        Poll to see if there is a message waiting to be read.
        '''
        return self.reader.poll()
        
    def send(self, packet):
        self.writer.send(packet)
        
    def stop(self):
        self.reader.stop()    # ask the threads to terminate
        self.writer.stop()
        
        self.reader.join()    # wait for the threads to terminate
        self.writer.join()
        
        self.socket.close()