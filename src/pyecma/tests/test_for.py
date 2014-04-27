import pyecma
import unittest



class ForTestCase(unittest.TestCase):

    def test_1(self):
        js = r"""
            var a = 0;
            for (var i = 0; i < 10; i++){
                if (a > 5)
                    break;
                a++;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 6, 'incorrect for loop')

    def test_2(self):
        
        js = r"""
            var a = 1;
            for (;;){
                if (a >= 10)
                    break;
                a++;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 10, 'incorrect for loop')

    def test_3(self):
        
        js = r"""
            var a = 1;
            for (;a < 10;){
                a++;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 10, 'incorrect for loop')

    def test_4(self):
        
        js = r"""
            var a = 1;
            for (;;a++){
                if (a >= 10)
                    break;
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 10, 'incorrect for loop')

    def test_5(self):
        js = r"""
            var a = 10;
            for (var i = 0; i < 10; i++)
                a++;
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 20, 'incorrect for loop')
    
    def test_6(self):
        js = r"""
            var a = 0;
            for(var i = 0; i< 10; i++){
                for(var j = 0; j< 10; j++){
                    if (j>5)
                        break;
                    a++;
                }
            }
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a, 60, 'incorrect for loop')
    
    

