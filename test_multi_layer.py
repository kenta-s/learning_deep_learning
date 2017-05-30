import unittest
from multi_layer import MultiLayer

class TestMultiLayer(unittest.TestCase):

    def setUp(self):
        self.multi_layer = MultiLayer()

    def test_forward(self):
        self.assertEqual(110.00000000000001, self.multi_layer.forward(100, 1.1))
        self.assertEqual(300, self.multi_layer.forward(150, 2))

    def test_backward(self):
        self.multi_layer.x = 300
        self.multi_layer.y = 2
        self.assertEqual((2.2, 330.0), self.multi_layer.backward(1.1))

if __name__ == '__main__':
    unittest.main()
