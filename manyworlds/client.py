''' client module.
'''

import manyworlds.message

class Client():
    def __init__(self):
        self.ui = None
        self.net = None
        self.status = 0
        self.clickCount = 0
        
    def button_callback(self):
        print('click')
        self.clickCount += 1
        self.ui.updateClickCount(self.clickCount)
        
        data = self.clickCount.to_bytes(4, byteorder='big')
        message = manyworlds.message.Message(None, ('127.0.0.1', 6000), data)
        self.net.send(message)
    
    def tick(self):
        message = self.net.poll()
        if message != None:
            print('message "' + str(message.data) + '" received from', message.fromAddress)
        
    def run(self):
        # start the networking threads
        self.net.start()
        
        # start the UI
        self.ui.startEventLoop()
        
        # tidy up when the UI event loop ends
        self.shutdown()
        
    def shutdown(self):
        self.net.stop()