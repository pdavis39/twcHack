import sys
from random import shuffle
from SimpleXMLRPCServer import SimpleXMLRPCServer

class MyFuncs:
    def reverse(self, str) :
        x = list(str);
        x.reverse();
        return ''.join(x);
    def scramble(self, str):
        x = list(str);
        shuffle(x);
        return ''.join(x);

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MyFuncs())
server.serve_forever()