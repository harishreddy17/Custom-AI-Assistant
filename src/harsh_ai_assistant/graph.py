# core/graph.py
import os
import re
from datetime import datetime
from .core.models import get_llm
from .core.state import AssistantState
from langgraph.graph import StateGraph, Annotated

# Initialize LLM
llm = get_llm()

# ---------------- Helpers ---------------- #
def _extract_text(result) -> str:
    if result is None:
        return ""
    if hasattr(result, "content"):
        return str(result.content)
    if isinstance(result, str):
        return result
    try:
        return str(result)
    except Exception:
        return ""

def _slugify(text: str, maxlen: int = 40) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-]", "", text)
    return text[:maxlen].strip("-") or "snippet"

# ---------------- Nodes ---------------- #
def codegen_node(state: AssistantState) -> dict:
    result = llm.invoke(state["query"])
    content = _extract_text(result)
    return {"codegen_response": content, "codegen_query": state["query"]}

def debug_node(state: AssistantState) -> dict:
    result = llm.invoke(state["query"])
    content = _extract_text(result)
    return {"debug_response": content}

def explain_node(state: AssistantState) -> dict:
    result = llm.invoke(state["query"])
    content = _extract_text(result)
    return {"explain_response": content}

def save_python_file(state: AssistantState) -> dict:
    content = state.get("codegen_response", "") or ""
    if not content.strip():
        return {"file_saved": "No codegen output to save.", "saved_filename": ""}

    # Extract Python code
    code = None
    if "```python" in content:
        try:
            code = content.split("```python", 1)[1].split("```", 1)[0].strip()
        except Exception:
            code = None

    if not code:
        lines = content.splitlines()
        candidate = []
        for line in lines:
            if line.strip().startswith(("def ", "import ", "from ", "class ", "if ", "print(", "__name__")) or (line and line.startswith(" ")):
                candidate.append(line)
            elif candidate:
                break
        code = "\n".join(candidate).strip() if candidate else None

    if not code:
        return {"file_saved": "No Python code block found in response.", "saved_filename": ""}

    # Prepare folder
    folder = "generated"
    os.makedirs(folder, exist_ok=True)

    slug = _slugify(state.get("query", "snippet"))
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"{slug}_{timestamp}.py"
    fullpath = os.path.join(folder, filename)

    try:
        with open(fullpath, "w", encoding="utf-8") as f:
            f.write(code + "\n")
        return {"file_saved": f"Saved to {fullpath}", "saved_filename": fullpath}
    except Exception as e:
        return {"file_saved": f"Failed to save file: {e}", "saved_filename": ""}

# ---------------- Build Workflow ---------------- #
workflow = StateGraph(AssistantState)

# Router node
workflow.add_node("router", lambda state: {"query": state["query"]})

# LLM nodes with annotated outputs
workflow.add_node("codegen", codegen_node, outputs={
    "codegen_response": Annotated(),
    "codegen_query": Annotated()
})
workflow.add_node("debug", debug_node, outputs={"debug_response": Annotated()})
workflow.add_node("explain", explain_node, outputs={"explain_response": Annotated()})
workflow.add_node("save_file", save_python_file, outputs={"file_saved": Annotated(), "saved_filename": Annotated()})

# Connect nodes (no state_key)
workflow.add_edge("router", "codegen")
workflow.add_edge("router", "debug")
workflow.add_edge("router", "explain")
workflow.add_edge("codegen", "save_file")

# Set entry point
workflow.set_entry_point("router")
app = workflow.compile()
