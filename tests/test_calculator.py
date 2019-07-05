from unittest import TestCase
from calculator_project.app.calculator import CalcMachine

class CalculatorTest(TestCase):
    def setUp(self):
        self.calc=CalcMachine()

    def test_calc_div(self):
        self.assertEqual(5,self.calc.div(20,4))

    #def test_calc_div_str(self):
     #   self.assertEqual('5',self.calc.div('20','4'))

    def test_calc_div_str(self):
        self.assertRaises(Exception,self.calc.div,'this','fails')

if "__name__" == "__main__":
   unittest.main() 
