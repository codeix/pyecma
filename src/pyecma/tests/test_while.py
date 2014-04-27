import math
import pyecma
import unittest



class WhileTestCase(unittest.TestCase):

    def test_1(self):
        
        js = r"""
            function factorial(counter){
                var result = 1;
                do {
                    result *= counter;
                    counter -= 1;
                } while (counter > 0);
                return result;
            }
        """
        app = pyecma.parse(js)
        for i in range(1, 20):
            self.assertEqual(app.factorial(i), math.factorial(i), 'incorrect while')

    def test_2(self):
        
        js = r"""
            var a = 1;
            while(a < 10){
                if (a > 5)
                    break;
                a++;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 6, 'incorrect while')

    def test_2(self):
        
        js = r"""
            var a = 1;
            while(a < 10)
                a++;
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 10, 'incorrect while')
