from platformdirs import user_log_dir

import client.const
import common.const


log_dir: str = user_log_dir(
    appname=f"{common.const.APP_NAME} {client.const.PACKAGE_NAME}",
    appauthor=common.const.APP_AUTHOR,
    version=client.const.PACKAGE_VERSION,
    ensure_exists=True,
)
