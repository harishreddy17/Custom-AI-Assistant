import subprocess
from langchain.tools import tool

@tool
def run_tests(data: dict = None) -> str:
    """
    Run pytest in the project and return results.
    data = {"path": "tests/"} (optional)
    """
    path = data.get("path", ".") if data else "."
    try:
        result = subprocess.run(
            ["pytest", path, "-q", "--maxfail=3", "--disable-warnings"],
            capture_output=True,
            text=True,
            timeout=20
        )
        output = result.stdout.strip()
        errors = result.stderr.strip()
        return f"✅ Tests Result:\n{output}\n\nErrors:\n{errors}" if errors else f"✅ Tests Result:\n{output}"
    except Exception as e:
        return f"❌ Error running tests in {path}: {e}"
