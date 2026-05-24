import os
import importlib

def load_plugins():
    plugins = []
    
    # Get the absolute path to the 'widgets' directory relative to this file
    base_path = os.path.dirname(os.path.abspath(__file__))
    widgets_dir = os.path.join(base_path, "widgets")

    if not os.path.exists(widgets_dir):
        print(f"Error: Could not find directory {widgets_dir}")
        return plugins

    for file in os.listdir(widgets_dir):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"widgets.{file[:-3]}"

            try:
                # Force a reload or ensure it's in sys.modules
                module = importlib.import_module(module_name)
                importlib.reload(module)  

                if hasattr(module, "PLUGIN"):
                    plugins.append(module.PLUGIN)
                else:
                    print(f"Module {module_name} has no 'PLUGIN' dict.")

            except Exception as e:
                print(f"Failed loading {module_name}: {e}")

    return plugins