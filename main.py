# Cristian
from unittest import TestCase
from fibonacci import Fibonacci


class FibonacciShould(TestCase):
    def test_return_0_when_0(self):
        fibonacci = Fibonacci()
        output = fibonacci.execute(0)
        self.assertEqual(output, 0)
