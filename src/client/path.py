import os

from platformdirs import user_log_dir, user_config_dir

import client.const
import common.const


package_path = os.path.abspath(os.path.dirname(__file__))

log_dir: str = user_log_dir(
    appname=f"{common.const.APP_NAME} {client.const.PACKAGE_NAME}",
    appauthor=common.const.APP_AUTHOR,
    version=client.const.PACKAGE_VERSION,
    ensure_exists=True,
)

config_dir: str = user_config_dir(
    appname=f"{common.const.APP_NAME} {client.const.PACKAGE_NAME}",
    appauthor=common.const.APP_AUTHOR,
    version=client.const.PACKAGE_VERSION,
    ensure_exists=True,
)
