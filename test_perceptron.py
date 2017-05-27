import unittest
import perceptron

class TestPerceptron(unittest.TestCase):
    def test_AND(self):
        self.assertEqual(1, perceptron.AND(1,1))
        self.assertEqual(0, perceptron.AND(0,1))
        self.assertEqual(0, perceptron.AND(0,0))

    def test_NAND(self):
        self.assertEqual(0, perceptron.NAND(1,1))
        self.assertEqual(1, perceptron.NAND(0,1))
        self.assertEqual(1, perceptron.NAND(1,0))
        self.assertEqual(1, perceptron.NAND(0,0))

    def test_OR(self):
        self.assertEqual(1, perceptron.OR(1,1))
        self.assertEqual(1, perceptron.OR(0,1))
        self.assertEqual(1, perceptron.OR(1,0))
        self.assertEqual(0, perceptron.OR(0,0))

if __name__ == '__main__':
    unittest.main()
