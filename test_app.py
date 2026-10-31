import unittest
from app import normalize_name

class TestName(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(normalize_name(" Alice "), "Alice")

if __name__ == "__main__":
    unittest.main()
