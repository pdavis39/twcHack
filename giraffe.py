from xmlrpclib import ServerProxy

server = ServerProxy("http://localhost:8000")
print server.reverse('giraffe')
print server.scramble('giraffe')