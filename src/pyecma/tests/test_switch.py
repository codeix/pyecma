import math
import pyecma
import unittest



class SwitchTestCase(unittest.TestCase):

    def test_1(self):
        
        js = r"""
            function switchtest(sw){
                var a = '';
                switch(sw){
                    case 1: 
                        a = 'one';
                        break;
                    case 2:
                        a = 'two';
                        break;
                    default:
                        a = 'default';
                }
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.switchtest(1), 'one', 'incorrect switch')
        self.assertEqual(app.switchtest(2), 'two', 'incorrect switch')
        self.assertEqual(app.switchtest(3), 'default', 'incorrect switch')

    def test_2(self):
        
        js = r"""
            function switchtest(sw){
                var a = '';
                switch(sw){
                    case 1: 
                        a = 'one';
                    case 2:
                        a = 'two';
                }
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.switchtest(1), 'two', 'incorrect switch')
        self.assertEqual(app.switchtest(2), 'two', 'incorrect switch')

    def test_3(self):
        
        js = r"""
            function switchtest(sw){
                var a = '';
                switch(sw){
                    default:
                        a = 'default';
                        break;
                    case 1: 
                        a = 'one';
                        break;
                    case 2:
                        a = 'two';
                        break;
                }
                return a;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.switchtest(1), 'one', 'incorrect switch')
        self.assertEqual(app.switchtest(2), 'two', 'incorrect switch')
