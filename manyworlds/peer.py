''' peer module.

There are no clients and servers in ManyWorlds.

Everything is a peer, with its own user-interface, or none.
'''
import logging

import manyworlds.message

class Peer():
    '''
    The UI provides an event loop which must call the tick() method of the
    peer class regularly enough to send and receive messages.
    '''
    
    def __init__(self):
        self.ui = None
        self.net = None
        self.crypt = manyworlds.message.Crypt()     # uses toy encryption, replace with something better
        self.status = 0
        self.clickCount = 0
        
    def button_callback(self):
        print('click')
        self.clickCount += 1
        self.ui.updateClickCount(self.clickCount)
        
        receiver = manyworlds.message.Talker(('127.0.0.1', 6000))   # this should come from the state
        message = manyworlds.message.Message(self.clickCount)
        
        packet = self.crypt.encode(receiver, message)
        self.net.send(packet)
    
    def tick(self):
        packet = self.net.poll()
        if packet != None:
            sender = manyworlds.message.Talker(packet.address)    # this should come from a service
            message = self.crypt.decode(sender, packet)
            logging.info('message "' + str(message.number) + '" received from ' + str(packet.address))
            
            reply = manyworlds.message.Message(999)
            packet = self.crypt.encode(sender, reply)
            self.net.send(packet)
        
    def run(self):
        # start the networking threads
        self.net.start()
        
        # start the UI
        self.ui.startEventLoop()
        
        # tidy up when the UI event loop ends
        self.shutdown()
        
    def shutdown(self):
        self.net.stop()

