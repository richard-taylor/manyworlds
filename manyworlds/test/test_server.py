
import manyworlds.server
import manyworlds.test.net
import unittest

class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = manyworlds.server.Server()
        self.server.net = manyworlds.test.net.Net()
        
    def test_constructors(self):
        self.assertTrue(self.server != None)
        
    def test_status(self):
        self.assertEqual(self.server.status, 0)
    
    def test_default_net(self):
        s = manyworlds.server.Server()
        self.assertEqual(s.net, None)
    
    def test_run(self):
        self.server.run()
        self.assertEqual(self.server.status, 0)
        
    def test_shutdown(self):
        self.server.shutdown()
        self.assertEqual(self.server.status, 0)
        
if __name__ == '__main__':
    unittest.main()