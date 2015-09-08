''' client module.
'''

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
    
    def run(self):
        # start the networking threads
        # start the UI
        self.ui.startEventLoop()
        
        # tidy up when the UI event loop ends
        self.shutdown()
        
    def shutdown(self):
        self.net.close()