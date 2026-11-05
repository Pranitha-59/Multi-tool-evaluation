import json
import os
from collections import defaultdict


def load_results(filename="results/tool_logs.json"):
    with open(filename, "r") as file:
        return json.load(file)


def analyze_results():

    results = load_results()

    total_tests = len(results)

    tool_counts = defaultdict(int)
    error_counts = defaultdict(int)
    execution_times = defaultdict(list)
    outputs = defaultdict(list)

    # Tool selection tracking
    correct_tool_selections = 0
    total_tool_selections = 0

    for result in results:

        tool = result["tool"]

        tool_counts[tool] += 1

        execution_times[tool].append(
            result["execution_time"]
        )

        outputs[result["test_case_id"]].append(
            result["output"]
        )

        if result["error"] is not None:
            error_counts[tool] += 1

        # Check tool selection
        if result.get("tool_selection_correct") is not None:

            total_tool_selections += 1

            if result["tool_selection_correct"]:
                correct_tool_selections += 1

    # Overall success and failure

    total_errors = sum(error_counts.values())

    successful_evaluations = (
        total_tests - total_errors
    )

    failed_evaluations = total_errors

    error_rate = (
        failed_evaluations / total_tests * 100
    )

    # Tool selection accuracy

    if total_tool_selections > 0:

        tool_selection_accuracy = (
            correct_tool_selections
            / total_tool_selections
            * 100
        )

    else:

        tool_selection_accuracy = 0

    # Average execution time

    average_execution_times = {}

    for tool, times in execution_times.items():

        average_execution_times[tool] = (
            sum(times) / len(times)
        )

    # Test case analysis

    test_case_analysis = {}

    for test_case, test_outputs in outputs.items():

        total_runs = len(test_outputs)

        output_counts = defaultdict(int)

        for output in test_outputs:
            output_counts[str(output)] += 1

        unique_outputs = len(output_counts)

        most_common_count = max(
            output_counts.values()
        )

        consistency_percentage = (
            most_common_count
            / total_runs
            * 100
        )

        if unique_outputs == 1:
            status = "Consistent"
        else:
            status = "Variable"

        test_case_analysis[test_case] = {
            "runs": total_runs,
            "unique_outputs": unique_outputs,
            "consistency_percentage": round(
                consistency_percentage,
                2
            ),
            "status": status
        }

    # Complexity analysis

    complexity_outputs = defaultdict(
        lambda: defaultdict(list)
    )

    for result in results:

        complexity = result["complexity"]

        test_case = result["test_case_id"]

        complexity_outputs[
            complexity
        ][test_case].append(
            result["output"]
        )

    complexity_analysis = {}

    for complexity, test_cases in (
        complexity_outputs.items()
    ):

        consistency_values = []

        for test_case, test_outputs in (
            test_cases.items()
        ):

            total_runs = len(test_outputs)

            output_counts = defaultdict(int)

            for output in test_outputs:
                output_counts[str(output)] += 1

            most_common_count = max(
                output_counts.values()
            )

            consistency = (
                most_common_count
                / total_runs
                * 100
            )

            consistency_values.append(
                consistency
            )

        average_consistency = (
            sum(consistency_values)
            / len(consistency_values)
        )

        complexity_analysis[
            complexity
        ] = round(
            average_consistency,
            2
        )

    # Create final report

    report = {
        "total_evaluations": total_tests,

        "successful_evaluations":
            successful_evaluations,

        "failed_evaluations":
            failed_evaluations,

        "error_rate_percentage":
            round(error_rate, 2),

        "tool_selection_accuracy":
            round(
                tool_selection_accuracy,
                2
            ),

        "tool_usage":
            dict(tool_counts),

        "average_execution_time": {
            tool: round(time, 6)
            for tool, time
            in average_execution_times.items()
        },

        "errors":
            dict(error_counts),

        "test_case_analysis":
            test_case_analysis,

        "complexity_analysis":
            complexity_analysis
    }

    # Save report

    os.makedirs(
        "results",
        exist_ok=True
    )

    with open(
        "results/evaluation_report.json",
        "w"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    # Print report

    print("\n===== EVALUATION REPORT =====")

    print(
        f"\nTotal evaluations: "
        f"{total_tests}"
    )

    print(
        f"Successful evaluations: "
        f"{successful_evaluations}"
    )

    print(
        f"Failed evaluations: "
        f"{failed_evaluations}"
    )

    print(
        f"Overall error rate: "
        f"{error_rate:.2f}%"
    )

    print(
        f"\nTool selection accuracy: "
        f"{tool_selection_accuracy:.2f}%"
    )

    print("\nTool usage:")

    for tool, count in tool_counts.items():
        print(
            f"{tool}: {count}"
        )

    print("\nErrors:")

    for tool, count in error_counts.items():
        print(
            f"{tool}: {count}"
        )

    print("\nOutput consistency:")

    for test_case, data in (
        test_case_analysis.items()
    ):

        print(
            f"{test_case}: "
            f"{data['consistency_percentage']}% "
            f"({data['status']})"
        )

    print("\nComplexity analysis:")

    for complexity, value in (
        complexity_analysis.items()
    ):

        print(
            f"{complexity}: "
            f"{value}%"
        )

    print(
        "\nReport saved to "
        "results/evaluation_report.json"
    )


if __name__ == "__main__":
    analyze_results()