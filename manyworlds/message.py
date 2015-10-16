''' message module.
'''

class Message():
    def __init__(self, fromAddress, toAddress, data):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.data = data
