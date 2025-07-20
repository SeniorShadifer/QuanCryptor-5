import webview
from loguru import logger
from webview import Window

import client.const
import client.path


window: Window


class Api:
    def log_info(self, data):
        logger.info(data)

    def log_debug(self, data):
        logger.debug(data)

    def log_error(self, data):
        logger.error(data)

    def log_warning(self, data):
        logger.warning(data)

    def log_success(self, data):
        logger.success(data)


def start_webview():
    logger.info(f"Loading WebGUI...")

    window = webview.create_window(
        title=client.const.PACKAGE_FULLNAME,
        url=f"{client.path.package_path}/web_gui/index.html",
        js_api=Api(),
    )

    webview.start()
