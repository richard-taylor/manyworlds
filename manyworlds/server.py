''' server module.
'''
import time

import manyworlds.message

class Server():
    def __init__(self):
        self.net = None
        self.keep_running = True
        self.status = 0
        
    def run(self):
        # start the networking threads
        self.net.start()
        
        # run until someone stops us
        try:
            while self.keep_running:
                message = self.net.poll()
                if message != None:
                    print('message "' + str(message.data) + '" received from', message.address)
                    data = bytes('thanks', 'utf-8')
                    reply = manyworlds.message.Message(message.address, data)
                    self.net.send(reply)
                time.sleep(1)
        except KeyboardInterrupt:
            pass
            
        # tidy up
        self.shutdown()
        
    def shutdown(self):
        self.net.stop()