import unittest

import src.common.crypto


class TestHashDataFunction(unittest.TestCase):
    def test(self):
        hex_result = "4ab94f915a9ebfa32a0ac1bda7fa5f041c66037078831e8b36c4a497ee242891"

        input = "I love C++."

        self.assertEqual(
            hex_result,
            src.common.crypto.hash_data(input.encode()).hex(),
        )
