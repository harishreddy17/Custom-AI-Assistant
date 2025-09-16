from typing import TypedDict

class AssistantState(TypedDict, total=False):
    query: str
    codegen_response: str
    debug_response: str
    explain_response: str
    file_saved: str
    execution_output: str
