import unittest
import sys
# sys.path.append('./')
from analyze_csv import *

class test_analyze_csv(unittest.TestCase):

    def setUp(self):
        self.epochTime = 1600763816518
        self.file_with_data = "./Bill/csv_data/L2A_Sendewicz.csv"
        self.file_no_data = "./Bill/csv_data/file_with_no_data.csv"

    def test_read_csv_with_data(self):
        self.assertTrue(read_csv(self.file_no_data).empty)

    def test_convert_epoch_to_human_readable(self):
        self.assertEqual(convert_epoch_to_human_readable(self.epochTime), "2020-09-22 08:36:56.518000")

    def test_get_year(self):
        self.assertEqual(get_year(self.epochTime), "2020")

    def test_get_month(self):
        self.assertEqual(get_month(self.epochTime), "09")

    def test_get_day(self):
        self.assertEqual(get_day(self.epochTime), "22")

    def test_get_hour(self):
        self.assertEqual(get_hour(self.epochTime), "08")

    def test_get_minutes(self):
        self.assertEqual(get_minutes(self.epochTime), "36")

    def test_get_seconds(self):
        self.assertEqual(get_seconds(self.epochTime), "56")

    def test_get_milliseconds(self):
        self.assertEqual(get_milliseconds(self.epochTime), "518000")


if __name__ == '__main__':
    unittest.main()
