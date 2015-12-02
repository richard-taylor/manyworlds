
import argparse
import logging
import sys

import manyworlds.server
import manyworlds.inet

# parse the command-line

parser = argparse.ArgumentParser(description='ManyWorlds server')
parser.add_argument('-p', '--port', 
    help='port number to listen on (default %(default)s)',
    default=6000, type=int)

args = parser.parse_args()

# turn on logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

# apply command-line parameters to the server

server = manyworlds.server.Server()

server.net = manyworlds.inet.Net(args.port)

server.run()

sys.exit(server.status)