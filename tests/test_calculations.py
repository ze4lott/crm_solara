import unittest
from solar_crm.calculations import solar_calculation

class SolarCalculationTests(unittest.TestCase):
    def test_positive_consumption_generates_panels(self):
        result = solar_calculation(10000, 2.5, 600, 5.0, 0.8, 80)
        self.assertGreater(result["paneles"], 0)
        self.assertGreater(result["potencia_instalada"], 0)
        self.assertGreater(result["generacion_anual"], 0)

    def test_zero_consumption_is_safe(self):
        result = solar_calculation(0, 2.5, 600, 5.0, 0.8, 80)
        self.assertEqual(result["paneles"], 0)
        self.assertEqual(result["cobertura_real"], 0)
        self.assertEqual(result["payback"], 0)

    def test_invalid_inputs_are_bounded(self):
        result = solar_calculation(-100, -2, 0, 0, 5, 300)
        self.assertEqual(result["paneles"], 0)
        self.assertGreaterEqual(result["inversion"], 0)

if __name__ == "__main__":
    unittest.main()
