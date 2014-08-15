import pyecma
import unittest



class ObjectsTestCase(unittest.TestCase):


    def test_2(self):
        
        js = r"""
            var a = [1,2,3];
            var b = [1,2,1+2];
            var c = [[1,2],[3,4],[5,6]];
        """

        app = pyecma.parse(js)
        self.assertListEqual(app.a, [[1,2],[3,4],[5,6]], 'incorrect list')

    def test_2(self):
        
        js = r"""
            var array = [1,2,3,4, 4+1];
            var a = array[1];
            var b = array[1+1];
            var d = [1,3,4][1];
            var func = function(){
                return 4;
            }
            var c = array[func()];
            // yes this is possible in ecma script
            var spez = [1,2,3][0,2];
        """

        app = pyecma.parse(js)
        self.assertEqual(app.a, 2, 'incorrect list')
        self.assertEqual(app.b, 3, 'incorrect list')
        self.assertEqual(app.c, 5, 'incorrect list')
        self.assertEqual(app.d, 3, 'incorrect list')
        self.assertEqual(app.spez, 3, 'incorrect list')

    def test_3(self):
        
        js = r"""
            var f1 = [[11, 22], [33, 44], [55, 66]][0][0];
            var f2 = [[11, 22], [33, 44], [55, 66]][0][1];
            var f3 = [[11, 22], [33, 44], [55, 66]][1][0];
            var f4 = [[11, 22], [33, 44], [55, 66]][1][1];
            var f5 = [[11, 22], [33, 44], [55, 66]][2][0];
            var f6 = [[11, 22], [33, 44], [55, 66]][2][1];
        """

        app = pyecma.parse(js)
        self.assertEqual(app.f1, 11, 'incorrect list')
        self.assertEqual(app.f2, 22, 'incorrect list')
        self.assertEqual(app.f3, 33, 'incorrect list')
        self.assertEqual(app.f4, 44, 'incorrect list')
        self.assertEqual(app.f5, 55, 'incorrect list')
        self.assertEqual(app.f6, 66, 'incorrect list')

    def test_4(self):
        
        js = r"""
            var a = [[11, 22][1], [33, 44][0]][0];
            var b = [2, [4, 3, [4, [3, [3][0]]]][2][1]][1][1];
        """

        app = pyecma.parse(js)
        self.assertEqual(app.a, 22, 'incorrect list')
        self.assertEqual(app.b, 3, 'incorrect list')

