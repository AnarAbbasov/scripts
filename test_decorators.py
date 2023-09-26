from sole_decorators import get_log
import intervew

import pytest



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
def test_mypr():
   assert myprinting('clen')=='clen'
   
#test_mypr(myprinting=myprinting)
def test_mypr2():
  assert myprinting('clen')=='clen'
  
def test_interview():
    assert  intervew.divide_by2(4)==2
    