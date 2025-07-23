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

    if not hasattr(module, "init"):
        raise Exception(f"Module not implements module interface (function 'init')")

    return module.init()


def load_mods(mods_dir: str, base_mod={}):
    logger.info(f"Loading modules in directory '{mods_dir}'...")

    data = {"base": base_mod}

    if not os.path.exists(mods_dir) and not os.path.isdir(mods_dir):
        logger.info(f"Directory '{mods_dir}' is not exists. Creating...")
        os.makedirs(mods_dir)

    else:
        listdir = os.listdir(mods_dir)
        if len(listdir) > 0:
            index = 0
            for current_mod in listdir:
                try:
                    logger.info(
                        f"[{++index + 1}/{len(listdir)}] Loading module '{current_mod}'..."
                    )

                    mod_data = load_mod(f"{mods_dir}/{current_mod}")

                    if "namespace" not in mod_data:
                        raise KeyError("Module data not contains namespace")

                    data[mod_data["namespace"]] = mod_data

                except Exception as e:
                    logger.error(
                        f"* Cannot load module '{current_mod}': {e}. Ignoring."
                    )

        else:
            logger.info(f"Modules in '{mods_dir}' not founded.")

    return data
