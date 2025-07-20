import os
import sys
import traceback
from datetime import datetime

from loguru import logger

import client.const
import client.mods
import client.path
from common import mod_loader


def main():
    try:
        logger.add(
            f"{client.path.log_dir}/{datetime.today().strftime("%Y-%m-%d")}.log",
            rotation="1 day",
            retention="7 days",
            compression="zip",
            colorize=True,
        )

        logger.info(f"{client.const.PACKAGE_FULLNAME}")

        client.mods.data = mod_loader.load_mods("./mods", {})

    except Exception as e:
        traceback.print_exc()
        logger.critical(f"{e}")
        sys.exit(1)
