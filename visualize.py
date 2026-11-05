import json
import matplotlib.pyplot as plt


def load_report(filename="results/evaluation_report.json"):

    with open(filename, "r") as file:
        return json.load(file)


def create_consistency_chart():

    report = load_report()

    test_cases = report["test_case_analysis"]

    names = list(test_cases.keys())

    consistency = [
        test_cases[name]["consistency_percentage"]
        for name in names
    ]

    plt.figure(figsize=(10, 5))

    plt.bar(names, consistency)

    plt.xlabel("Test Case")
    plt.ylabel("Consistency (%)")
    plt.title("Output Consistency by Test Case")

    plt.ylim(0, 100)

    plt.tight_layout()

    plt.savefig(
        "results/consistency_by_test_case.png"
    )

    plt.show()

    print(
        "Chart saved to "
        "results/consistency_by_test_case.png"
    )


if __name__ == "__main__":
    create_consistency_chart()