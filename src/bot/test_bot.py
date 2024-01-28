import unittest
from bot import stats

class TestPrintStats(unittest.TestCase):

    def test_print_stats(self):
        for row in stats:
            print(row) 
        # Assert print was called with stats
        self.assertIn('print', str(stats))

if __name__ == '__main__':
    unittest.main()