import unittest
import intervew



class Mytests(unittest.TestCase):
    def testequal(self):
        self.assertEqual(1,1)
    def testlist(self):
        self.assertIsInstance(intervew.getlist(),list)
        
    def anothertest(self):
        self.assertEqual(1,2)
        
        
       