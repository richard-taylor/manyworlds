''' message module.
'''

MAX_PACKET_BYTES = 508

class Message():
    def __init__(self, address, data):
        self.address = address
        self.data = data
