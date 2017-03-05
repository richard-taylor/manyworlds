''' Headless UI module.
'''

import time

class UI():
    '''
    Headless implementation of the UI interface.
    '''
    
    def __init__(self, client):
        self.client = client
        self.keep_running = True
        
    def startEventLoop(self):
        try:
            while self.keep_running:
                self.client.tick()
                time.sleep(0.1)

        except KeyboardInterrupt:
            pass
