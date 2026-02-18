import os
import shutil
import subprocess

def run_shell(command, content=None):
    """Running Any Command in Terminal"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout if result.returncode == 0 else result.stderr
        return output if output.strip() else "Success (No output)"
    except Exception as e:
        return f"Error executing command: {str(e)}"

def create_file(path, content=""):
    """Create a File With Specific Content!"""
    try:
        with open(path, "w") as f:
            f.write(content)
        return f"File '{path}' succes created, Bro!"
    except Exception as e:
        return f"File Creation Failed: {str(e)}"

def make_dir(path, content=None):
    """Created New Folder"""
    try:
        os.makedirs(path, exist_ok=True)
        return f"Folder '{path}' siap digunakan!"
    except Exception as e:
        return f"Folder Creation Failed: {str(e)}"

def delete_path(path, content=None):
    """Permanently Delete Files"""
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            return f"Path '{path}' File Not Found."
        return f"{path}'The file has been deleted"
    except Exception as e:
        return f"Failed to Delete: {str(e)}"
DISPATCHER = {
    "create_file": create_file,
    "make_dir": make_dir,
    "delete": delete_path,
    "run_command": run_shell
}

