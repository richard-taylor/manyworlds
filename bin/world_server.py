
import manyworlds.server
import manyworlds.inet
import sys

server = manyworlds.server.Server()

server.net = manyworlds.inet.Net(server)

server.run()

sys.exit(server.status)