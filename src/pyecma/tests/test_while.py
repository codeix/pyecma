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


    def test_3(self):
        
        js = r"""
            var a = 1;
            var b = 1;
            while(true){
                a += 1;
                if (a < 5){
                    b *= a;
                    continue;
                    a += 2000;
                }
                b += a;
                if (a > 10)
                   break;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 11, 'incorrect while')
        self.assertEqual(app.b, 80, 'incorrect while')


    def test_4(self):
        
        js = r"""
            var a = 1;
            var b = 1;
            do {
                a += 1;
                if (a < 5){
                    b *= a;
                    continue;
                    a += 3000;
                }
                b += a;
                if (a > 10)
                   break;
            } while (true);
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 11, 'incorrect while')
        self.assertEqual(app.b, 80, 'incorrect while')
