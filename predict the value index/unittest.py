import unittest
from unittest.mock import patch, MagicMock
import random
import tkinter as tk
from game_app import GameApp

class TestGameApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = GameApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_binary_search_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = arr[2500]
        index, time_taken = self.app.binary_search(arr, target)
        self.assertEqual(index, 2500)
        self.assertTrue(float(time_taken) > 0)

    def test_binary_search_not_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = 1000001  # Out of range target
        index, time_taken = self.app.binary_search(arr, target)
        self.assertEqual(index, -1)
        self.assertTrue(float(time_taken) > 0)

    def test_jump_search_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = arr[2500]
        index, time_taken = self.app.jump_search(arr, target)
        self.assertEqual(index, 2500)
        self.assertTrue(float(time_taken) > 0)

    def test_jump_search_not_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = 1000001  # Out of range target
        index, time_taken = self.app.jump_search(arr, target)
        self.assertEqual(index, -1)
        self.assertTrue(float(time_taken) > 0)

    def test_exponential_search_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = arr[2500]
        index, time_taken = self.app.exponential_search(arr, target)
        self.assertEqual(index, 2500)
        self.assertTrue(float(time_taken) > 0)

    def test_exponential_search_not_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = 1000001  # Out of range target
        index, time_taken = self.app.exponential_search(arr, target)
        self.assertEqual(index, -1)
        self.assertTrue(float(time_taken) > 0)

    def test_fibonacci_search_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = arr[2500]
        index, time_taken = self.app.fibonacci_search(arr, target)
        self.assertEqual(index, 2500)
        self.assertTrue(float(time_taken) > 0)

    def test_fibonacci_search_not_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = 1000001  # Out of range target
        index, time_taken = self.app.fibonacci_search(arr, target)
        self.assertEqual(index, -1)
        self.assertTrue(float(time_taken) > 0)

    def test_interpolation_search_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = arr[2500]
        index, time_taken = self.app.interpolation_search(arr, target)
        self.assertEqual(index, 2500)
        self.assertTrue(float(time_taken) > 0)

    def test_interpolation_search_not_found(self):
        arr = sorted(random.sample(range(1, 1000001), 5000))
        target = 1000001  # Out of range target
        index, time_taken = self.app.interpolation_search(arr, target)
        self.assertEqual(index, -1)
        self.assertTrue(float(time_taken) > 0)

    @patch('mysql.connector.connect')
    def test_save_result(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        self.app.player_name.set("TestPlayer")
        self.app.target = 12345
        self.app.results = {
            "Binary Search": {"index": 2500, "time": "0.00012345"},
            "Jump Search": {"index": 2500, "time": "0.00012345"},
            "Exponential Search": {"index": 2500, "time": "0.00012345"},
            "Fibonacci Search": {"index": 2500, "time": "0.00012345"},
            "Interpolation Search": {"index": 2500, "time": "0.00012345"},
        }

        self.app.save_result()

        self.assertTrue(mock_cursor.execute.called)
        self.assertTrue(mock_conn.commit.called)

if __name__ == '__main__':
    unittest.main()
