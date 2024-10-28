import unittest
from lottery import draw_lots

class TestDrawLots(unittest.TestCase):
    def test_valid_array(self):
        arr = ["Morticia", "Gomez", "Lurch", "Fester", "Pugsley"]
        result = draw_lots(arr)
        self.assertEqual(len(result), len(arr))
        for key, value in result.items():
            self.assertIn(key, arr)
            self.assertIn(value, arr)
            self.assertNotEqual(key, value)

    def test_array_too_small(self):
        with self.assertRaises(ValueError):
            draw_lots(["Morticia"])

    def test_no_self_pairing(self):
        arr = ["Morticia", "Gomez", "Lurch", "Fester", "Pugsley"]
        result = draw_lots(arr)
        for key, value in result.items():
            self.assertNotEqual(key, value)


    def test_different_results_on_consecutive_runs(self):
        arr = ["Morticia", "Gomez", "Lurch", "Fester", "Pugsley"]
        result1 = draw_lots(arr)
        result2 = draw_lots(arr)
        self.assertNotEqual(result1, result2)
    

if __name__ == '__main__':
    unittest.main()