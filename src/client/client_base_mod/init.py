from loguru import logger


def init():
    logger.success("Hello from client basic module!")

    return {"title": "QuanCryptor 5 built-in module", "namespace": "qc5cbm"}
