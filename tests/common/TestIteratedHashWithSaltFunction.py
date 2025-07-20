import unittest

import src.common.crypto


class TestIteratedHashWithSaltFunction(unittest.TestCase):
    def test(self):
        hex_result = "8f7a984aedd67dd8cba53a77bd0ce6187eee2832a643b81f3f253859d116c8d1"

        password = b"Banan_8255"
        salt = b"sugar"
        iterations = 5000

        self.assertEqual(
            hex_result,
            src.common.crypto.iterated_hash_whit_salt(password, salt, iterations).hex(),
        )
