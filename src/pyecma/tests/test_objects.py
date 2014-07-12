import pyecma
import unittest



class ObjectsTestCase(unittest.TestCase):
    
    def test_1(self):
        
        js = r"""
            var a = [1,2,3];
            var b = {'abc':1};
            var c = a[1];
        """

        app = pyecma.parse(js)
        repr(app.a)
        import pdb;pdb.set_trace()


