import json
from datetime import datetime
import sys
import traceback

from loguru import logger

import server.const
import server.path
import server.mods
from common import mod_loader


def main():
    try:
        logger.add(
            f"{server.path.SERVER_DATA_PATH}/Logs/{datetime.today().strftime("%Y-%m-%d")}.log",
            rotation="1 day",
            retention="30 days",
            compression="zip",
            colorize=True,
        )

        logger.info(f"{server.const.PACKAGE_FULLNAME}")

        logger.info(f"Loading base_mod...")
        server.mods.data["qc5sbm"] = mod_loader.load_mod(
            f"{server.path.package_path}/server_base_mod"
        )

        try:
            server.mods.data |= mod_loader.load_mods(
                f"{server.path.SERVER_DATA_PATH}/Mods"
            )

            logger.success(f"Mods loaded successfully.")

        except Exception as e:
            logger.error(f"Cannot load mods: {e}. Continuing without mods...")

        finally:
            logger.debug(
                f"Current mod data: \n{json.dumps(server.mods.data, indent=4, ensure_ascii=False)}"
            )
    except Exception as e:
        traceback.print_exc()
        logger.critical(f"Critical error: {e}.")
        sys.exit(1)

    return
