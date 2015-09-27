import pyecma
import unittest



class ObjectTestCase(unittest.TestCase):

    def test_1(self):
        js = r"""
            a = {mykey1:10,
                 mykey2:20,
                 mykey3:10+20};
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a['mykey1'], 10, 'incorrect object')
        self.assertEqual(app.a['mykey2'], 20, 'incorrect object')
        self.assertEqual(app.a['mykey3'], 30, 'incorrect object')

    def test_1(self):
        js = r"""
            a = {func: function(){return 1+1;},
                 list: [1,2,3]};
        """
        app = pyecma.parse(js)
        self.assertEqual(app.a['func'](), 2, 'incorrect object')
        print(app.a['list'])
        self.assertSequenceEqual(app.a['list'], [1, 2 ,3], 'incorrect object')

