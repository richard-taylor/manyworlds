
import manyworlds.server
import manyworlds.inet
import sys

server = manyworlds.server.Server()

server.net = manyworlds.inet.Net(server, 6000)

server.run()

sys.exit(server.status)