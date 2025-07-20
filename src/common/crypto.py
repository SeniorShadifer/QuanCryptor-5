from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def hash_data(data: bytes) -> bytes:
    """
    Simplified use of cryptography hashing tools.
    Hashes data with single-iteration SHA-256 without salt.

    Args:
        data (bytes): Data for hashing.

    Returns:
        bytes: SHA-256 hash of `data`.
    """

    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize()


def iterated_hash_whit_salt(
    data: bytes, salt: bytes, iterations: int, length: int = 32
):
    """
    Simplified use of cryptography password deriving tools.
    Hashes data with PBKDF2HMAC and SHA-256.

    Args:
        data (bytes): Secret data for hashing. It can be password, which need to be converted to key or checksum.
        salt (bytes): Additional non-secret data, which make hashing stronger. Usually, it's just random bytes.
        iterations (int): Count of hashing rounds. Usually it equals 100_000-200_000.
        length(int): Length of result.

    Returns:
        bytes: PBKDF2HMAC and SHA-256 hash of data.
    """

    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend(),
    ).derive(data)
