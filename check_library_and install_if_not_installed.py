def install_required_libraries(required_libraries):
    import importlib
    import subprocess
    """
    Checks if the required libraries are installed and installs them if they are not already installed.

    Args:
        required_libraries (list): A list of strings containing the names of the required libraries.

    Returns:
        None
    """
    for library in required_libraries:
        try:
            importlib.import_module(library)
            print(f"{library} is already installed")
        except ImportError:
            print(f"{library} is not installed. Installing now...")
            subprocess.check_call(['pip', 'install', library])

# This function takes in a list of required libraries as an argument and loops through each library in the list. It then checks if the library is already installed using importlib.import_module(). If it is not installed, it installs it using subprocess.check_call() and the pip install command.

# You can call this function with a list of required libraries as an argument to check and install them as needed.

# In [3]: install_required_libraries(['requests', 'numpy', 'pandas'])
# requests is already installed
# numpy is already installed
# pandas is already installed
