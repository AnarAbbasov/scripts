from sole_decorators import get_log
import intervew

import unittest



@get_log
def myprinting(text):
    print (text)
    return text
    


#myprinting('clen')

#
#class TryTesting(TestCase):
#    def test_always_passes(self):
#        self.assertTrue(True)
#
#
#
#    def test_mypt(self):
#        self.assertEqual(myprinting('clen'),'clen')
#        
#    def test_mypt_otput(self):
#        
#@pytest.fixture
#def test_mypr():
#   assert myprinting('clen')=='clen'
#   
#test_mypr(myprinting=myprinting)
#def test_mypr2():
#  assert myprinting('clen')=='clen'
#  
#def test_interview():
#    assert  intervew.divide_by2(4)==2
#
#def test_map():
#     assert isinstance(intervew.getlist(),list)



class mebeltest(unittest.TestCase):
       def rtyTest(self):
         rectangle = intervew.divide_by2(6)
         self.assertEqual(rectangle, 3, "incorrect result")
      
      
      
       
     

#class mytest(unittest.TestCase):
#  
#  def runTest(self):
#       rectangle = intervew.divide_by2(6)
#       self.assertEqual(rectangle, 3, "incorrect result")
#       
#        
#  def rtyTest(self):
#        rectangle = intervew.divide_by2(6)
#        self.assertEqual(rectangle, 3, "incorrect result")


#unittest.main()






      
        
        
        
  
  