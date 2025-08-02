import os
import json
import pathlib
import unittest

import src.common.file_utils


class TestHashDataFunction(unittest.TestCase):
    path = "settings.json"

    def test_when_file_is_not_exists(self):
        self.delete_file()

        default = {"ip": "0.0.0.0", "port": 8255}

        self.assertEqual(default, src.common.file_utils.load_json(self.path, default))

    def test_when_file_is_exists(self):
        default = {"ip": "0.0.0.0", "port": 8256, "debug": False}
        source = {"ip": default["ip"], "port": 8255}

        open(self.path, "w").write(json.dumps(source))

        self.assertEqual(
            {"ip": "0.0.0.0", "port": 8255, "debug": False},
            src.common.file_utils.load_json(self.path, default),
        )

    def delete_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)
