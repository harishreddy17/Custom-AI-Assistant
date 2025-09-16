import sys
from core.graph import app

def start_cli():
    print("🤖 Cursor-AI Assistant (Python MVP)")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("> ")
        if query.lower() in {"exit", "quit"}:
            break

        result = app.invoke({"query": query})

        # Pick output to display: file_saved > codegen
        response = (
            result.get("file_saved")
            or result.get("codegen_response")
            or result.get("debug_response")
            or result.get("explain_response")
        )

        if response:
            print(response)
        else:
            print("⚠️ No response returned from nodes")
