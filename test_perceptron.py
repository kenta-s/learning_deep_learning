import unittest
import perceptron

class TestPerceptron(unittest.TestCase):
    def test_AND(self):
        self.assertEqual(1, perceptron.AND(1,1))
        self.assertEqual(0, perceptron.AND(0,1))
        self.assertEqual(0, perceptron.AND(0,0))

if __name__ == '__main__':
    unittest.main()
