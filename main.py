from evaluator import run_all_tests


def main():

    results = run_all_tests()

    print("Evaluation completed.")
    print(f"Total test cases executed: {len(results)}")
    print("Results saved in results/tool_logs.json")


if __name__ == "__main__":
    main()