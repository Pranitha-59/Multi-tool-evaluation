import json
import os
from datetime import datetime


def log_result(result, filename="results/tool_logs.json"):
    """
    Saves one tool execution result to a JSON file.
    """

    os.makedirs("results", exist_ok=True)

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": result["tool"],
        "input": result["input"],
        "output": result["output"],
        "execution_time": result["execution_time"],
        "error": result["error"],
        "test_case_id": result.get("test_case_id"),
        "topic": result.get("topic"),
        "complexity": result.get("complexity"),
        "run_number": result.get("run_number"),

        "selected_tool": result.get(
            "selected_tool"
        ),

        "expected_tool": result.get(
            "expected_tool"
        ),

        "tool_selection_correct": result.get(
            "tool_selection_correct"
        )
    }

    if os.path.exists(filename):

        with open(filename, "r") as file:
            logs = json.load(file)

    else:
        logs = []

    logs.append(log_entry)

    with open(filename, "w") as file:

        json.dump(
            logs,
            file,
            indent=4
        )

    return log_entry