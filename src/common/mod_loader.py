import os
import json
import importlib.util

from loguru import logger


def load_mod(mod_dir: str):
    if not os.path.exists(mod_dir) and os.path.isdir(mod_dir):
        raise FileNotFoundError(
            f"Cannot load mod '{mod_dir}': directory '{mod_dir}' is not exists"
        )

    INIT_PATH = f"{mod_dir}/init.py"
    if not os.path.exists(f"{mod_dir}/init.py"):
        raise FileNotFoundError(
            f"Cannot load mod '{mod_dir}': '{INIT_PATH}' is not exists"
        )

    spec = importlib.util.spec_from_file_location("init", f"{mod_dir}/init.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "init") or not hasattr(module, "name"):
        raise Exception(
            f"Module not implements module interface (functions 'init' and 'name')"
        )

    return module.init(), module.name()


def load_mods(mods_dir: str, base_mod={}):
    logger.info(f"Loading modules in directory '{mods_dir}'...")

    if not os.path.exists(mods_dir) and not os.path.isdir(mods_dir):
        raise FileNotFoundError(
            f"Cannot load modules in '{mods_dir}': directory is not exists"
        )

    data = {"base": base_mod}
    for current_mod in os.listdir(mods_dir):
        try:
            logger.info(f"* Loading module '{current_mod}'...")

            mod_data, name = load_mod(f"{mods_dir}/{current_mod}")
            data[name] = mod_data

        except Exception as e:
            logger.error(f"* Cannot load module '{current_mod}': {e}. Ignoring.")

    return data
