import pyecma
import unittest



class ExpressionsTestCase(unittest.TestCase):
    
    def test_1(self):
        
        js = r"""
            var a = 1 + 2;
            var b = 1 + 2 * 3;
            var c = (1 + 2) * 3;
            var d = (1 + 2) * (3 + 3);
            var e = (1 + 2 * 4) * ((2 + 1) * 2);
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 3, 'incorrect addition')
        self.assertEqual(app.b, 7, 'incorrect multiplication')
        self.assertEqual(app.c, 9, 'incorrect addition inside braces')
        self.assertEqual(app.d, 18, 'incorrect addition inside braces')
        self.assertEqual(app.e, 54, 'incorrect addition inside braces')


    def test_2(self):
        js = r"""
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
        js = r"""
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
        js = r"""
            var a = 1 == 1;
            var b = 2 > 1;
            var c = 1 < 2;
            var d = 1 <= 1;
            var e = 1 >= 1;
            var f = 1==1==1;
            var g = 1==(1==1);
            var h = 1==(1==0);
            var i = 1 != 1;
            var j = 2 > 2;
            var k = 2 < 2;
            var l = 2 <= 1;
            var m = 1 >= 2;
        """
        app = pyecma.parse(js)
        self.assertTrue(app.a, 'incorrect comparison')
        self.assertTrue(app.b, 'incorrect comparison')
        self.assertTrue(app.c, 'incorrect comparison')
        self.assertTrue(app.d, 'incorrect comparison')
        self.assertTrue(app.e, 'incorrect comparison')
        self.assertTrue(app.f, 'incorrect comparison')
        self.assertTrue(app.g, 'incorrect comparison')
        self.assertFalse(app.h, 'incorrect comparison')
        self.assertFalse(app.i, 'incorrect comparison')
        self.assertFalse(app.j, 'incorrect comparison')
        self.assertFalse(app.k, 'incorrect comparison')
        self.assertFalse(app.l, 'incorrect comparison')
        self.assertFalse(app.m, 'incorrect comparison')


    def test_5(self):
        js = r"""
            var a = 'Hello World';
            var b = "Hello World";
            var c = 'it\'s works :-)';
            var d = 'Hello' + ' World';
            var e = 'Hello';
            var e += ' World';
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 'Hello World', 'incorrect comparison')
        self.assertEqual(app.b, 'Hello World', 'incorrect comparison')
        self.assertEqual(app.c, "it's works :-)", 'incorrect comparison')
        self.assertEqual(app.e, 'Hello World', 'incorrect comparison')


    def test_6(self):
        self.assertEqual(pyecma.eval('1 + 1'), 2, 'incorrect comparison')
        self.assertEqual(pyecma.eval('1 + 2 * 3'), 7, 'incorrect comparison')


    def test_7(self):
        js = r"""
            var a = 'Hello World';
            // var a = "inline comment";
            /*
                multiline
                commments
                here
            */
            var b = 'code is continue here';
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 'Hello World', 'incorrect comparison')
        self.assertEqual(app.b, 'code is continue here', 'incorrect comparison')

