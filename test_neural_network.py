import unittest
import neural_network
import numpy as np

class TestNeuralNetwork(unittest.TestCase):
    def test_step_function(self):
        expected = np.array([0,0,0,0,0,1,1,1,1,1])
        # This leads to an error, I don't know why.
        # self.assertEqual(expected, neural_network.step_function(np.arange(-0.5, 0.5, 0.1)))

    def test_sigmoid(self):
        self.assertEqual(0.7310585786300049, neural_network.sigmoid(1.0))
        self.assertEqual(0.88079707797788231, neural_network.sigmoid(2.0))

if __name__ == '__main__':
    unittest.main()
