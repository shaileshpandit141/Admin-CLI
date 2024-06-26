from os import makedirs, getcwd
from os.path import exists, join


# Define a Directory class.
class Directory:
    def __init__(self, app_name: str) -> None:
        self.root_dir = join(getcwd(), app_name)

        # Creating root app directory
        if not self.exists(self.get_absolute_path(self.root_dir)):
            makedirs(self.root_dir)
    
    def get_absolute_path(self, relative_path_name: str) -> str:
        return join(self.root_dir, relative_path_name)

    def create(self, file_path: str) -> None:
        if not self.exists(self.get_absolute_path(file_path)):
            makedirs(self.get_absolute_path(file_path))

    def exists(self, file_path: str) -> bool:
        is_exit = exists(self.get_absolute_path(file_path))
        return is_exit


