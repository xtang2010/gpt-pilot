from helpers.cli import execute_command


def install_hook(project):
    """
    Command to run to complete the project scaffolding setup.

    :param project: the project object
    """
    execute_command(project, "pip install")


PYTHON3 = {
    "path": "python",
    "description": "Python3 project with local venv",
    "summary": "\n".join([
        "* Initial setup with Python for fast development",
        "* Basic project structure for Python development",
        "* Minimal configuration to get started with Python",
    ]),
    "install_hook": install_hook,
    "files": {
        "__init__.py": "initialization file for the package.",
        "main.py": "Main entry point for the project, if the project is an excuatable program. For project which creates library, this may not necessary",
        "requirements.txt": "file listing dependencies required by the project",
        "setup.py": "file used to install the package, if the package can be distributing",
        "README.md": "file containing information about the project",
        "LICENSE": "license of the project if necessary",
        "tests/__init__.py": "Empty file, tests directory contain unittest cases for the project",
        ".env": "Environment setting",
        ".venv": "Directory for virtual Python Environment",
    }
}

