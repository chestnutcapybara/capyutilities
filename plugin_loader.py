import os
import sys
import importlib
import logging

def load_plugins():
    plugins = []
    seen = set()

    base_path = os.path.dirname(os.path.abspath(__file__))
    widgets_dir = os.path.join(base_path, "widgets")

    if not os.path.exists(widgets_dir):
        print(f"Error: Could not find directory {widgets_dir}")
        return plugins

    def load_module(module_name):
        try:
            if module_name in sys.modules:
                module = importlib.reload(sys.modules[module_name])
            else:
                module = importlib.import_module(module_name)

            if hasattr(module, "PLUGIN"):
                plugin = module.PLUGIN

                # Prevent duplicates by name
                name = plugin.get("name")
                if not name:
                    print(f"Plugin in {module_name} missing 'name'")
                    return

                if name in seen:
                    logging.warning(f"Duplicate plugin ignored: {name}")
                    return

                seen.add(name)
                plugins.append(plugin)

            else:
                print(f"Module {module_name} has no 'PLUGIN' dict.")

        except Exception as e:
            print(f"Failed loading {module_name}: {e}")

    for item in os.listdir(widgets_dir):
        item_path = os.path.join(widgets_dir, item)

        # -----------------------
        # Case 1: Single file plugin
        # -----------------------
        if item.endswith(".py") and item != "__init__.py":
            module_name = f"widgets.{item[:-3]}"
            load_module(module_name)

        # -----------------------
        # Case 2: Folder plugin
        # -----------------------
        elif os.path.isdir(item_path):
            plugin_file = os.path.join(item_path, "plugin.py")

            if not os.path.exists(plugin_file):
                continue

            module_name = f"widgets.{item}.plugin"
            load_module(module_name)

    return plugins