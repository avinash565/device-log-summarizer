
import unittest
from src.section1_cleaning import clean_sensor_readings


class TestSensorReadings(unittest.TestCase):

    def test_normal_readings(self):
        readings = [10, "20", 30.5, None, -5, "abc", 600]
        expected = [10.0, 20.0, 30.5, 500.0]

        self.assertEqual(
            clean_sensor_readings(readings),
            expected
        )

    def test_empty_list(self):
        self.assertEqual(clean_sensor_readings([]), [])

    def test_all_invalid_values(self):
        readings = [None, -10, "hello", "abc"]
        self.assertEqual(clean_sensor_readings(readings), [])


if __name__ == "__main__":
    unittest.main()
