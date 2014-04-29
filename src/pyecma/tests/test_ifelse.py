import math
import pyecma
import unittest



class IfElseTestCase(unittest.TestCase):

    def test_1(self):
        
        js = r"""
            function test(val){
                var a = undefined;
                if (val){
                    a = true;
                } else {
                    a = false;
                }
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertTrue(app.test(True), 'incorrect if-else statement')
        self.assertFalse(app.test(False), 'incorrect if-else statement')

    def test_2(self):
        
        js = r"""
            function test(val){
                var a = undefined;
                if (val)
                    a = true;
                else
                    a = false;
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertTrue(app.test(True), 'incorrect if-else statement')
        self.assertFalse(app.test(False), 'incorrect if-else statement')

    def test_2(self):
        
        js = r"""
            function test(val){
                var a = undefined;
                if (val)
                    a = true;
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertTrue(app.test(True), 'incorrect if-else statement')
