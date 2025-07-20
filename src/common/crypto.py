from cryptography.hazmat.primitives import hashes


def hash_data(data: bytes | str) -> bytes:
    if isinstance(data, str):
        data = data.encode()

    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize()
