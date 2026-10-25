# test_chainglen.py
"""
Tests for ChainGlen module.
"""

import unittest
from chainglen import ChainGlen

class TestChainGlen(unittest.TestCase):
    """Test cases for ChainGlen class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainGlen()
        self.assertIsInstance(instance, ChainGlen)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainGlen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
