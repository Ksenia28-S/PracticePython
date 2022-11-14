# Тесты к калькулятору комплексных чисел

```python
import unittest


from calculator import Complex


class TestComplex(unittest.TestCase):
    
    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)
        self.assertTrue(first.__eq__(second))
        
    def test_equal_img(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertNotEqual(first, second) 
        
    def test_add1(self):
        first = Complex(3, 6)
        second = Complex(2, 3)        
        self.assertEqual(Complex.__add__(first, second), Complex(5, 9))
        
    def test_add2(self):
        first = Complex(5, 0)
        second = Complex(0, 7)        
        self.assertEqual(Complex.__add__(first, second), Complex(5, 7))       
    
    def test_subtract1(self):
        first = Complex(3, 6)
        second = Complex(5, 3)        
        self.assertEqual(Complex.__subtract__(first, second), Complex(-2, 3))
        
    def test_subtract2(self):
        first = Complex(8, 1)
        second = Complex(5, 3)        
        self.assertEqual(Complex.__subtract__(first, second), Complex(3, -2))
        
    def test_multiply1(self):
        first = Complex(2, 3)
        second = Complex(4, 2)        
        self.assertEqual(Complex.__multiply__(first, second), Complex(2, 16))
        
    def test_multiply2(self):
        first = Complex(0, 3)
        second = Complex(5, 1)        
        self.assertEqual(Complex.__multiply__(first, second), Complex(-3, 15))
        
    def test_modul1(self):
        first = Complex(3, 4)        
        self.assertEqual(Complex.__modul__(first), 5)
        
    def test_modul2(self):
        first = Complex(0, 7)        
        self.assertEqual(Complex.__modul__(first), 7)
        
    def test_divide1(self):
        first = Complex(2, 3)
        second = Complex(4, 2)        
        self.assertEqual(Complex.__divide__(first, second), Complex(0.7, 0.4))    
        
    def test_divide2(self):
        first = Complex(1, 0)
        second = Complex(0, 5)        
        self.assertEqual(Complex.__divide__(first, second), Complex(0, -0.2))   

if __name__ == "__main__":
    unittest.main()
```
