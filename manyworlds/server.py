''' server module.
'''

class Server():
    def __init__(self):
        self.net = None
        self.status = 0
        
    def run(self):
        # start the networking threads
        
        # tidy up when all the threads end
        self.shutdown()
        
    def shutdown(self):
        self.net.close()