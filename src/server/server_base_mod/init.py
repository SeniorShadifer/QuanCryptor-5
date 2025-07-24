from loguru import logger


def init():
    logger.success(f"Hello from server basic module!")

    return {"title": "QuanCryptor 5 server built-in module", "namespace": "qc5sbm"}
