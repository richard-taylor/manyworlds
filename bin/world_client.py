
import manyworlds.client
import manyworlds.inet
import manyworlds.tkui
import sys

client = manyworlds.client.Client()

client.net = manyworlds.inet.Net(client)
client.ui = manyworlds.tkui.UI(client)

client.run()

sys.exit(client.status)