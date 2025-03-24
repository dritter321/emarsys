import unittest
from datetime import datetime
from calculate_due_date import calculate_due_date


class TestCalculateDueDate(unittest.TestCase):
    def test_due_date_in_same_day(self):
        submit_time = datetime(2025, 3, 4, 10, 12)
        turnaround_time = 4
        expected = datetime(2025, 3, 4, 14, 12)
        self.assertEqual(calculate_due_date(submit_time, turnaround_time), expected)

    def test_due_date_next_day(self):
        submit_time = datetime(2025, 3, 4, 14, 56)  # Tuesday
        turnaround_time = 6
        expected = datetime(2025, 3, 5, 12, 56)  # Wednesday
        self.assertEqual(calculate_due_date(submit_time, turnaround_time), expected)

    def test_skip_weekend(self):
        submit_time = datetime(2025, 3, 7, 15, 32)  # Friday
        turnaround_time = 4
        expected = datetime(2025, 3, 10, 11, 32)  # Monday
        self.assertEqual(calculate_due_date(submit_time, turnaround_time), expected)


if __name__ == "__main__":
    unittest.main()