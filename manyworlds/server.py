''' server module.
'''
import logging
import time

import manyworlds.message

class Server():
    def __init__(self):
        self.net = None
        self.crypt = manyworlds.message.Crypt()     # uses toy encryption, replace with something better
        self.keep_running = True
        self.status = 0
        
    def run(self):
        # start the networking threads
        self.net.start()
        
        # run until someone stops us
        try:
            while self.keep_running:
                packet = self.net.poll()
                if packet != None:
                    sender = manyworlds.message.Talker(packet.address)    # this should come from a service
                    message = self.crypt.decode(sender, packet)
                    
                    logging.info('message "' + str(message.number) + '" received from' + str(packet.address))

                    reply = manyworlds.message.Message(999)
                    packet = self.crypt.encode(sender, reply)
                    self.net.send(packet)
                    
                time.sleep(1)
        except KeyboardInterrupt:
            pass
            
        # tidy up
        self.shutdown()
        
    def shutdown(self):
        self.net.stop()