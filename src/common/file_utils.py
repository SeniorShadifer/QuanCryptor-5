import os
import json


def load_json(path: str, default: dict = {}) -> dict:
    """
    Load JSON data from file or write default values there if it's not exists.

    Arguments:
        path (str): Path to .json file. If the file does not exist, it will be created.
        default (Any): Default values of .json keys. The default values are written to the file if it does not exist.

    Returns:
        dict: If the file does not exist, function will return value of argument `default`. If file is exist, its content will merged with value of `default`.
    """

    if os.path.exists(path) and os.path.isfile(path):
        with open(path, "r") as fin:
            file_content = fin.read()

        try:
            data = json.loads(file_content)

        except json.JSONDecodeError:
            with open(path, "w") as fout:
                fout.write(json.dumps(default))

            return default

        data = default | data

        with open(path, "w") as fout:
            fout.write(json.dumps(data, ensure_ascii=False, indent=4))

        return data

    else:
        dirname = os.path.dirname(path)

        if dirname != "":
            os.makedirs(dirname, exist_ok=True)

        with open(path, "w") as fout:
            fout.write(json.dumps(default))

        return default
