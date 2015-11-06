
import manyworlds.client
import manyworlds.inet
import manyworlds.tkui

import argparse
import sys

# parse the command-line

parser = argparse.ArgumentParser(description='ManyWorlds client')
parser.add_argument('-p', '--port', 
    help='port number to listen on (default %(default)s)',
    default=6001, type=int)

args = parser.parse_args()

# apply command-line parameters to the client

client = manyworlds.client.Client()

client.net = manyworlds.inet.Net(args.port)
client.ui = manyworlds.tkui.UI(client)

client.run()

sys.exit(client.status)