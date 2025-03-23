import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.event_utils import generate_delayed_random_event_time
import datetime
from unittest.mock import patch


class TestEventUtils(unittest.TestCase):
    def test_generate_delayed_random_event_time(self):
        current_time = datetime.datetime(2023, 10, 1, 12, 0, 0)

        with patch('utils.event_utils.datetime') as mock_datetime:
            mock_datetime.datetime.now.return_value = current_time
            mock_datetime.datetime.strptime = datetime.datetime.strptime
            mock_datetime.timedelta = datetime.timedelta
            original_time = "2023-09-30 12:00:00"
            result = generate_delayed_random_event_time(original_time)
            result_datetime = datetime.datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
            original_datetime = datetime.datetime.strptime(original_time, "%Y-%m-%d %H:%M:%S")
            # Ensure the resulting time is:
            # 1. Less than or equal to the current time
            # 2. Greater than or equal to the original time
            self.assertTrue(original_datetime <= result_datetime <= current_time)


if __name__ == "__main__":
    unittest.main()