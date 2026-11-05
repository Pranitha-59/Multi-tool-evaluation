from tools import (
    calculator_tool,
    text_length_tool,
    keyword_search_tool,
    random_response_tool
)


def select_tool(query):
    """
    Selects a tool based on the user's natural-language query.
    """

    query = query.lower()

    # Calculator
    if any(word in query for word in [
        "calculate",
        "compute",
        "multiply",
        "divide",
        "add",
        "subtract"
    ]):
        return calculator_tool, "calculator"

    # Text length
    elif any(word in query for word in [
        "characters",
        "character",
        "length",
        "how long is the text"
    ]):
        return text_length_tool, "text_length"

    # Keyword search
    elif any(word in query for word in [
        "contains",
        "keyword",
        "find the word",
        "check whether"
    ]):
        return keyword_search_tool, "keyword_search"

    # AI-like response
    elif any(word in query for word in [
        "artificial intelligence",
        "machine learning",
        "multi-agent",
        "ai"
    ]):
        return random_response_tool, "random_response"

    else:
        raise ValueError(
            "Could not determine the appropriate tool."
        )


def run_agent(test_case):

    query = test_case["query"]

    tool, selected_tool = select_tool(query)

    test_input = test_case["input"]

    if selected_tool == "calculator":
        result = tool(test_input)

    elif selected_tool == "text_length":
        result = tool(test_input)

    elif selected_tool == "keyword_search":
        result = tool(
            test_input["text"],
            test_input["keyword"]
        )

    elif selected_tool == "random_response":
        result = tool(test_input)

    result["selected_tool"] = selected_tool

    result["expected_tool"] = test_case["tool"]

    result["tool_selection_correct"] = (
        selected_tool == test_case["tool"]
    )

    return result