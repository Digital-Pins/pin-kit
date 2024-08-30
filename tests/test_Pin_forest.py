# test_Pin_Forest.py

import unittest
from manager.ceo.Pin_Forest import some_function

class TestPinForest(unittest.TestCase):

    def test_some_function(self):
        result = some_function()
        self.assertEqual(result, expected_value)  # تأكد من تعديل expected_value حسب التوقعات

if __name__ == '__main__':
    unittest.main()
