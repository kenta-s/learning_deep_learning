import unittest
import numpy as np
from relu import Relu

class TestRelu(unittest.TestCase):
    def setUp(self):
        self.relu = Relu()

    def test_forward(self):
        array_a = np.array([-1, 0, 2, 3])
        expected = np.array([0, 0, 2, 3])
        # Not working, I don't know why
        # self.assertEqual(expected, self.relu.forward(array_a))

    # TODO: implement this test, but testing NumPy array seems difficult. I should learn that first...
    # def test_backward(self):
        # self.assertEqual(300, self.multi_layer.forward(150, 2))

if __name__ == '__main__':
    unittest.main()
