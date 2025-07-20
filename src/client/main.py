import os
import sys
import traceback
from datetime import datetime

from loguru import logger

import client.const
import client.mods
import client.path
import client.web_ui
from common import mod_loader


def main():
    try:
        current_log_file_path = (
            f"{client.path.log_dir}/{datetime.today().strftime("%Y-%m-%d")}.log"
        )
        logger.add(
            f"{client.path.log_dir}/{datetime.today().strftime("%Y-%m-%d")}.log",
            rotation="1 day",
            retention="7 days",
            compression="zip",
            colorize=True,
        )

        logger.info(f"{client.const.PACKAGE_FULLNAME}")

        try:
            client.mods.data = mod_loader.load_mods(
                f"{client.path.config_dir}/mods", client.mods.base
            )

        except Exception as e:
            logger.error(f"Cannot load mods: {e}. Continuing without mods...")

        client.web_ui.start_webview()

    except Exception as e:
        traceback.print_exc()
        logger.critical(
            f"Critical error: {e}. Output saved to '{current_log_file_path}'."
        )
        sys.exit(1)
