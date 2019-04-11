import unittest

from scrap.py import scrap, Person

class tests(unittest.TestCase):
    
    global p
    p = Person('k4ni5h', 'Kanish')
    
    def test1(self):
        scrap('shaddygarg')
        self.assertEqual(p_scrapped[0].name, 'Shaddy Garg')
    
    def test2(self):
        self.assertEqual(p_scrapped[0].city, 'Roorkee')
    
    def test3(self):
        self.assertEqual(p_scrapped[0].fav, 'There are no favourites.')
    
    def test4(self):
        scrap('swapnilnegi.09')
        self.assertEqual(p_scrapped[1].work, ['PAG', 'IMG, IIT Roorkee', 'Google Summer of Code', 'Student'])
    
    def test5(self):
        self.assertEqual(p.name, 'Kanish')
    
    def test6(self):
        with self.assertRaises(Exception):
            print(p.work)
    
    def test7(self):
        self.assertEqual(p.city, 'Roorkee')
    
    def test8(self): 
        per = Person('swapnilnegi.09','Swapnil','[IMG and PAG]','Jodhpur')
        self.assertEqual(per.city, 'Jodhpur')

if __name__ == '__main__':
    unittest.main()
