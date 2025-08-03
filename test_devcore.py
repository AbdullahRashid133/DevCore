# test_devcore.py
"""
Tests for DevCore module.
"""

import unittest
from devcore import DevCore

class TestDevCore(unittest.TestCase):
    """Test cases for DevCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DevCore()
        self.assertIsInstance(instance, DevCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DevCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
