import json

from agent import run_agent
from logger import log_result


def load_test_cases(filename="test_cases.json"):

    with open(filename, "r") as file:
        return json.load(file)


def run_test_case(test_case, run_number):

    result = run_agent(test_case)

    result["test_case_id"] = test_case["id"]
    result["topic"] = test_case["topic"]
    result["complexity"] = test_case["complexity"]
    result["run_number"] = run_number

    log_result(result)

    return result


def run_all_tests(number_of_runs=5):

    import os

    # Clear previous experiment logs
    log_file = "results/tool_logs.json"

    if os.path.exists(log_file):
        os.remove(log_file)

    test_cases = load_test_cases()

    results = []

    for run_number in range(
        1,
        number_of_runs + 1
    ):

        print(
            f"Starting run {run_number}..."
        )

        for test_case in test_cases:

            result = run_test_case(
                test_case,
                run_number
            )

            results.append(result)

    return results