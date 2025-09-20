# filesystem.py
import os
from datetime import datetime

def sanitize_filename(text: str) -> str:
    return text.lower().replace(" ", "-").replace("?", "").replace(":", "").replace("/", "-")

def save_outputs(query: str, result: dict):
    """
    Save outputs from the assistant into ./generated/<query_timestamp>/ files.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    folder_name = f"{sanitize_filename(query)[:40]}_{timestamp}"
    folder_path = os.path.join("generated", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    saved_files = {}

    # Save codegen
    if result.get("codegen_response"):
        fname = os.path.join(folder_path, "codegen.py")
        with open(fname, "w", encoding="utf-8") as f:
            f.write(result["codegen_response"])
        saved_files["codegen"] = fname

    # Save debug
    if result.get("debug_response"):
        fname = os.path.join(folder_path, "debug.py")
        with open(fname, "w", encoding="utf-8") as f:
            f.write(result["debug_response"])
        saved_files["debug"] = fname

    # Save explain
    if result.get("explain_response"):
        fname = os.path.join(folder_path, "explain.md")
        with open(fname, "w", encoding="utf-8") as f:
            f.write(result["explain_response"])
        saved_files["explain"] = fname

    return folder_path, saved_files
