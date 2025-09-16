from core.models import get_llm
from core.state import AssistantState
from langgraph.graph import StateGraph

# Initialize LLM
llm = get_llm()

# -----------------------
# Node definitions
# -----------------------

def codegen_node(state: AssistantState) -> dict:
    """Generate code for the query."""
    result = llm.invoke(state["query"])
    return {"codegen_response": str(result.content)}

def debug_node(state: AssistantState) -> dict:
    """Debug or explain code for the query."""
    result = llm.invoke(state["query"])
    return {"debug_response": str(result.content)}

def explain_node(state: AssistantState) -> dict:
    """Explain code logic."""
    result = llm.invoke(state["query"])
    return {"explain_response": str(result.content)}

def save_python_file(state: AssistantState) -> dict:
    """Extract Python code and save to file."""
    code = state.get("codegen_response", "")
    if code:
        # Extract Python section from Markdown
        if "```python" in code:
            code = code.split("```python")[1].split("```")[0]
        filename = "generated_code.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        return {"file_saved": f"{filename} saved successfully."}
    return {"file_saved": "No Python code found."}

# -----------------------
# Build workflow
# -----------------------

workflow = StateGraph(AssistantState)

# Add nodes
workflow.add_node("router", lambda state: {"query": state["query"]})
workflow.add_node("codegen", codegen_node)
workflow.add_node("debug", debug_node)
workflow.add_node("explain", explain_node)
workflow.add_node("save_file", save_python_file)

# Connect nodes
workflow.add_edge("router", "codegen")
workflow.add_edge("router", "debug")
workflow.add_edge("router", "explain")
workflow.add_edge("codegen", "save_file")

# Entry point
workflow.set_entry_point("router")

# Compile workflow
app = workflow.compile()
