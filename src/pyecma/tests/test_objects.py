import pyecma
import unittest



class ObjectsTestCase(unittest.TestCase):
    
    def test_1(self):
        
        js = r"""
            var a = [1,2,3];
            var b = {'abc':1};
        """
        import pdb;pdb.set_trace()

        app = pyecma.parse(js)
        self.assertEqual(app.a, 3, 'incorrect addition')


