import unittest
from add_layer import AddLayer

class TestMultiLayer(unittest.TestCase):
    def setUp(self):
        self.add_layer = AddLayer()

    def test_forward(self):
        self.assertEqual(5, self.add_layer.forward(2, 3))
        self.assertEqual(13.5, self.add_layer.forward(6, 7.5))

    def test_backward(self):
        self.assertEqual((1.1, 1.1), self.add_layer.backward(1.1))
        self.assertEqual((300, 300), self.add_layer.backward(300))

if __name__ == '__main__':
    unittest.main()
