import ast 
import operator 
import time
import random

def safe_calculate(expression):
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](
                evaluate(node.left),
                evaluate(node.right)
            )

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -evaluate(node.operand)

        raise ValueError("Unsupported mathematical expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


def calculator_tool(expression):
    """
    Performs a mathematical calculation.
    """
    start_time = time.time()

    try:
        result = safe_calculate(expression)
        error = None
    except Exception as e:
        result = None
        error = str(e)

    execution_time = time.time() - start_time

    return {
        "tool": "calculator",
        "input": expression,
        "output": result,
        "execution_time": execution_time,
        "error": error
    }


def text_length_tool(text):
    """
    Returns the number of characters in a text.
    """
    start_time = time.time()

    try:
        result = len(text)
        error = None
    except Exception as e:
        result = None
        error = str(e)

    execution_time = time.time() - start_time

    return {
        "tool": "text_length",
        "input": text,
        "output": result,
        "execution_time": execution_time,
        "error": error
    }


def keyword_search_tool(text, keyword):
    """
    Checks whether a keyword exists in a given text.
    """
    start_time = time.time()

    try:
        result = keyword.lower() in text.lower()
        error = None
    except Exception as e:
        result = None
        error = str(e)

    execution_time = time.time() - start_time

    return {
        "tool": "keyword_search",
        "input": {
            "text": text,
            "keyword": keyword
        },
        "output": result,
        "execution_time": execution_time,
        "error": error
    }
def random_response_tool(question):
    """
    Simulates a non-deterministic AI-like response.
    The same question may produce different outputs.
    """
    start_time = time.time()

    responses = [
        "Response A",
        "Response B",
        "Response C"
    ]

    result = random.choice(responses)
    error = None

    execution_time = time.time() - start_time

    return {
        "tool": "random_response",
        "input": question,
        "output": result,
        "execution_time": execution_time,
        "error": error
    }