''' message module.
'''

MAX_PACKET_BYTES = 508

class Packet():
    '''
    Low-level data packet sent and received by the networking module.
    '''
    def __init__(self, address, data):
        self.address = address
        self.data = data

class Message():
    '''
    Higher-level message object encoded into Packet for sending.
    '''
    def __init__(self, number):
        self.number = number
        
class Talker():
    '''
    A machine we are talking to.
    
    It has an address and also a UUID for testing continuity
    over "sessions" or periods of time longer than a few minutes. So that
    a third party cannot pretend to be us to someone else, we present a
    different UUID to each machine that we talk to.
    '''
    def __init__(self, address):
        self.address = address
        self.uuid = None
        self.myid = None
        self.key = None
        
class Crypt():
    '''
    API for encoding and decoding messages.
    
    There is a toy implementation here for testing purposes. It doesn't
    do any strong encryption so don't use it for anything that needs to
    be secure!
    
    Client and Server both have a "crypt" property which they expect
    to have the same methods as this object.
    '''
    def __init__(self):
        pass
        
    def encode(self, destination, message):
        '''
        '''
        # assume message is just a single number for now
        data_bytes = message.number.to_bytes(4, byteorder='big')
        
        return Packet(destination.address, data_bytes)

    def decode(self, sender, packet):
        '''
        '''
        return Message(int.from_bytes(packet.data, byteorder='big'))