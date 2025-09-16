from langchain.tools import tool

@tool
def read_file(path: str) -> str:
    """Read and return the contents of a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@tool
def write_file(data: dict) -> str:
    """Write content to a file. Expects {'path': str, 'content': str}."""
    path = data.get("path")
    content = data.get("content", "")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"✅ File {path} updated"
