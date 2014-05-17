import pyecma
from pyecma import types

import unittest



class ScopeTestCase(unittest.TestCase):

    def test_1(self):
        
        js = r"""
            a = 1;
            var b = 1;
            
            function sc(){
                a = 2;
                var b = 2;
                var c = 2;
                d = 3;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 1, 'incorrect scope')
        self.assertEqual(app.b, 1, 'incorrect scope')
        self.assertFalse(hasattr(app, 'c'), 'incorrect scope')
        self.assertFalse(hasattr(app, 'd'), 'incorrect scope')
        app.sc()
        self.assertEqual(app.a, 2, 'incorrect scope')
        self.assertEqual(app.b, 1, 'incorrect scope')
        self.assertFalse(hasattr(app, 'c'), 'incorrect scope')
        self.assertTrue(hasattr(app, 'd'), 'incorrect scope')

    def test_2(self):
        
        js = r"""
            function toInt(str){
                return parseInt(str);
            }
        """
        app = pyecma.parse(js)
        self.assertIsInstance(app.toInt('1'), types.Number, 'incorrect builtin')


    def test_3(self):
        
        js = r"""
            a = 1;
            function increment(){
                a++;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 1, 'incorrect builtin')
        app.a = 2
        self.assertEqual(app.a, 2, 'incorrect builtin')
        app.increment()
        self.assertEqual(app.a, 3, 'incorrect builtin')

