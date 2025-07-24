import os
import sys
import json
import traceback
from datetime import datetime

from loguru import logger

import client.const
import client.mods
import client.path
import client.web_gui
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

        logger.info(f"Loading base_mod...")
        client.mods.data["qc5cbm"] = mod_loader.load_mod(
            f"{client.path.package_path}/client_base_mod"
        )

        try:
            client.mods.data |= mod_loader.load_mods(f"{client.path.config_dir}/Mods")

            logger.success(f"Modules loaded successfully.")

        except Exception as e:
            logger.error(f"Cannot load mods: {e}. Continuing without mods...")

        finally:
            logger.debug(
                f"Current module data: \n{json.dumps(client.mods.data, indent=4, ensure_ascii=False)}"
            )

        client.web_gui.start_webview()

    except Exception as e:
        traceback.print_exc()
        logger.critical(
            f"Critical error: {e}."
        )
        sys.exit(1)
