
import manyworlds.client
import manyworlds.test.ui
import manyworlds.test.net
import unittest

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = manyworlds.client.Client()
        self.client.ui = manyworlds.test.ui.UI()
        self.client.net = manyworlds.test.net.Net()
        
    def test_constructors(self):
        self.assertTrue(self.client != None)
        
    def test_status(self):
        self.assertEqual(self.client.status, 0)
    
    def test_default_ui(self):
        c = manyworlds.client.Client()
        self.assertEqual(c.ui, None)
        
    def test_default_net(self):
        c = manyworlds.client.Client()
        self.assertEqual(c.net, None)
    
    def test_button_callback(self):
        self.assertEqual(self.client.clickCount, 0)
        
        self.client.button_callback()
        self.assertEqual(self.client.clickCount, 1)
        self.client.button_callback()
        self.assertEqual(self.client.clickCount, 2)
    
    def test_run(self):
        self.client.run()
        self.assertEqual(self.client.status, 0)
        
    def test_shutdown(self):
        self.client.shutdown()
        self.assertEqual(self.client.status, 0)
        
if __name__ == '__main__':
    unittest.main()