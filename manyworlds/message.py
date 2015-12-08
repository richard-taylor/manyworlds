''' message module.
'''
import random
import struct
import time

class Packet():
    '''
    Low-level data packet sent and received by the networking module.
    '''
    MAX_BYTES = 496  # 31 times 128 bits (should not be fragmented)
    
    def __init__(self, address, data):
        self.address = address
        self.data = data

class Message():
    '''
    Higher-level message object encoded into Packet for sending.
    '''
    def __init__(self, number):
        self.number = number

    @classmethod
    def from_bytes(cls, byte_data):
        number = int.from_bytes(byte_data, byteorder='big')
        return cls(number)

    def to_bytes(self):
        return self.number.to_bytes(4, byteorder='big')

class Talker():
    '''
    A machine we are talking to.
    
    It has an address and also a UUID for testing continuity over "sessions" or
    periods of time longer than a few minutes. So that a third party cannot
    pretend to be us to someone else, we present a different UUID to each
    machine that we talk to.
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
        Encode a Message object into a data Packet.
        
        destination is a Talker object.
        message is a Message object.
        returns a Packet object.
        
        The encoding has the following properties:
        
        All data is encrypted. There is no "header" section to the data which
        can be used to identify it as a ManyWorlds packet.
        
        Before the client has negotiated an encryption scheme and key with the
        destination, the default encryption scheme and key is used. This is
        AES-256 with the key below.
        
        ????????????????????????????????????????????????????????????????
        
        Each encoding of a given message is unique. Since the same message may
        be sent several times the encoder adds a timestamp or other random
        string to the data.
        
        Data length is a maximum of Packet.MAX_BYTES. This is chosen to try and
        ensure that all packets are small enough to be transmitted with minimal
        probability of failure.
        
        [Optionally?] each encoding of a given message is of random length,
        subject to encryption scheme block size constraints and the message
        size. For example, the default AES-256 scheme works on data that is a
        multiple of 128 bits long; so a 200 bit message will encode to data that
        is randomly between 32 bytes and the maximum data length.
        '''
        data_bytes = message.to_bytes()
        
        if len(data_bytes) + 0 > Packet.MAX_BYTES:
            pass
            
        # struct.pack struct.unpack timestamp = time.time().to_bytes(
        return Packet(destination.address, data_bytes)

    def decode(self, sender, packet):
        '''
        Dencode a data Packet into a Message object.
        
        sender is a Talker object.
        packet is a Packet object.
        returns a Message object.
        '''
        return Message.from_bytes(packet.data)