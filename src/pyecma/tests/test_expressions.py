import unittest
import pyecma



class ExpressionsTestCase(unittest.TestCase):
    
    def test_1(self):
        
        js = """
            var a = 1 + 2;
            var b = 1 + 2 * 3;
            var c = (1 + 2) * 3;
            var d = (1 + 2) * (3 + 3);
            var e = (1 + (2 * 4)) * (3 + 3);
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 3, 'incorrect addition')
        self.assertEqual(app.b, 7, 'incorrect multiplication')
        self.assertEqual(app.c, 9, 'incorrect addition inside braces')
        self.assertEqual(app.d, 18, 'incorrect addition inside braces')
        self.assertEqual(app.e, 54, 'incorrect addition inside braces')


    def test_2(self):
        js = """
            var i = 10;
            var a = i++;
            var b = i;
            var c = ++i;
            var d = i--;
            var e = i;
            var f = --i;
            var g = i;
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 10, 'incorrect increment/decrement')
        self.assertEqual(app.b, 11, 'incorrect increment/decrement')
        self.assertEqual(app.c, 12, 'incorrect increment/decrement')
        self.assertEqual(app.d, 12, 'incorrect increment/decrement')
        self.assertEqual(app.e, 11, 'incorrect increment/decrement')
        self.assertEqual(app.f, 10, 'incorrect increment/decrement')
        self.assertEqual(app.g, 10, 'incorrect increment/decrement')


    def test_3(self):
        js = """
            var a = 10;
            a += 10;
            var b = 10;
            b -= 10;
            var c = 10;
            c *= 10;
            var d = 10;
            d /= 10;
            var e = 10;
            e >>= 1;
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 20, 'incorrect assignment')
        self.assertEqual(app.b, 0, 'incorrect assignment')
        self.assertEqual(app.c, 100, 'incorrect assignment')
        self.assertEqual(app.d, 1, 'incorrect assignment')
        self.assertEqual(app.e, 5, 'incorrect assignment')


    def test_4(self):
        js = """
            var a = 1 == 1;
            var b = 2 > 1;
            var c = 1 < 2;
            var d = 1 <= 1;
            var e = 1 >= 1;
            var f = 1==1==1;
            var g = 1==(1==1);
            var h = 1==(1==0);
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, True, 'incorrect comparison')
        self.assertEqual(app.b, True, 'incorrect comparison')
        self.assertEqual(app.c, True, 'incorrect comparison')
        self.assertEqual(app.d, True, 'incorrect comparison')
        self.assertEqual(app.e, True, 'incorrect comparison')
        self.assertEqual(app.f, True, 'incorrect comparison')
        self.assertEqual(app.g, True, 'incorrect comparison')
        self.assertEqual(app.h, False, 'incorrect comparison')

