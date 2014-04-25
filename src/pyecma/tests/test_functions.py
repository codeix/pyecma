import pyecma
import unittest
from fractions import gcd
from math import factorial



class FunctionsTestCase(unittest.TestCase):

    def test_echo(self):
        js = r"""
        function echo (arg){
            return arg ;
        }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.echo('Hello'), 'Hello', 'incorrect function echo')
        self.assertEqual(app.echo('World'), 'World', 'incorrect function echo')
        self.assertEqual(app.echo(42), 42, 'incorrect function echo')
        self.assertEqual(app.echo(True), True, 'incorrect function echo')


    def test_gcd(self):
        
        js = r"""
            function abs(value){
                if (value < 0)
                    return value * -1;
                return value;
            }
            
            function gcd(e, f) {
                while (abs(e - f) > 0) {
                    if ( e < f )
                         f = f - e;
                    else
                         e = e - f;
                }
                return e;
            }
        """
        app = pyecma.parse(js)
        for i in range(1, 30):
            for j in range(1, 30):
                self.assertEqual(app.gcd(i, j), gcd(i, j), 'incorrect function gcd')


    def test_recursive(self):
        js = r"""
            function factorial (fac){
              if(fac > 1)
                  return fac * factorial(fac-1);
              else
                return fac;
            }
        """
        app = pyecma.parse(js)
        for i in range(1, 20):
            self.assertEqual(app.factorial(i), factorial(i), 'incorrect recursive function')
