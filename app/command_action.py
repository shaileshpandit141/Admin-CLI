import os
from modules import (
    Structure,
    Run
)
from structures import (
    frontend_structure,
    python_module_structure,
    python_structure,
    flask_structure,
    javascript_structure
)


def kebabCaseToPascalCase(string):
    pascalcase = "admin_cli"
    if string is not None:
        if "-" in string:
            temp = string.split("-")
            if len(temp) >= 2:
                pascalcase = "".join(map(lambda chunk: chunk.capitalize(), temp))
            else:
                pascalcase = string.capitalize()
        else:
            pascalcase = string.capitalize()
    return pascalcase


class CommandAction:
    def __init__(self) -> None:
        pass

    @staticmethod
    def is_exist(app_name: str):
        return os.path.exists(os.path.join(os.getcwd(), app_name))

    @staticmethod
    def create_py_module(module_name: str):
        module_name = kebabCaseToPascalCase(module_name)
        if not CommandAction.is_exist(module_name):
            # Creating app structure using Structure.make function.
            Structure.make(module_name, python_module_structure(module_name=module_name))

            # Success message.
            print(f"Your Python module has been created successfully and its name is `{module_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
        else:
            print("Oops! Your entered module name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
            print("Exit.")

    
    @staticmethod
    def create_js_module(module_name: str):
        module_name = kebabCaseToPascalCase(module_name)
        if not CommandAction.is_exist(module_name):
            # Creating app structure using Structure.make function.
            Structure.make(module_name, javascript_structure(module_name=module_name))

            # Success message.
            print(f"Your Python module has been created successfully and its name is `{module_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
        else:
            print("Oops! Your entered module name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(module_name)
            print("Exit.")

    @staticmethod
    def create_py_app(app_name: str):
        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, python_structure(app_name=app_name))

            # Success message.
            print(f"Your Python App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
        else:
            print(f"Oops! Your entered app name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            print("Exit.")

    @staticmethod
    def create_flask_app(app_name: str):

        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, flask_structure(app_name=app_name))

            # Success message.
            print(f"Your Flask App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
        else:
            print(f"Oops! Your entered flask app name already exists. Please try another name.")

            # Open your app in VS-Code.
            Run.open_with_vscode(app_name)
            print("Exit.")

    @staticmethod
    def create_js_app(app_name: str):

        if not CommandAction.is_exist(app_name):
            # Creating app structure using Structure.make function.
            Structure.make(app_name, frontend_structure(app_name=app_name))

            # Success message.
            print(f"Your Web App has been created successfully and its name is `{app_name}`.")

            # Open your app in VS-Code and Run your app with live-server.
            Run.run_frontend_for_dev(app_name)
        else:
            # Success message.
            print(f"Oops! Your entered app name already exists. Please try another name.")

           # Open your app in VS-Code and Run your app with live-server.
            Run.run_frontend_for_dev(app_name)
