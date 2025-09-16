import subprocess
from langchain.tools import tool

@tool
def run_code(data: dict) -> str:
    """
    Run Python code from a file and return stdout/stderr.
    data = {"path": "script.py"}
    """
    path = data.get("path")
    try:
        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True,
            timeout=10  # prevent infinite loops
        )
        output = result.stdout.strip()
        errors = result.stderr.strip()
        return f"Output:\n{output}\n\nErrors:\n{errors}" if errors else f"Output:\n{output}"
    except Exception as e:
        return f"❌ Error running {path}: {e}"
