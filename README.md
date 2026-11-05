
# Multi-Tool Evaluation and Logging Framework

A Python-based framework for evaluating tool execution, logging, error handling, and output consistency across repeated experiments.

## Project Overview

This project demonstrates how a multi-tool system can be evaluated using structured test cases and repeated executions.

A rule-based agent selects tools based on natural-language queries. The framework records execution details and analyzes tool-selection accuracy, execution errors, response consistency, and execution time.

The project is designed as a prototype for understanding evaluation techniques relevant to AI-assisted and multi-tool systems.

## Features

- Rule-based tool selection using natural-language queries
- Four tools: calculator, text length, keyword search, and simulated random response
- Automated execution of predefined test cases
- Repeated experiments to observe output variation
- JSON logging of tool inputs, outputs, execution times, and errors
- Tool-selection accuracy analysis
- Error-rate and output-consistency analysis
- Complexity-level analysis
- Visualization using Matplotlib

## Technologies Used

- Python
- JSON
- Matplotlib
- Python standard libraries: AST, operator, datetime, collections, random, time, and os

## Project Structure

```text
Multi-tool-evaluation/
├── agent.py
├── tools.py
├── logger.py
├── evaluator.py
├── analysis.py
├── visualize.py
├── main.py
├── test_cases.json
├── requirements.txt
├── .gitignore
└── results/
    ├── tool_logs.json
    ├── evaluation_report.json
    └── consistency_by_test_case.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Pranitha-59/Multi-tool-evaluation.git
cd Multi-tool-evaluation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Project

Execute the experiments:

```bash
python main.py
```

Generate the evaluation report:

```bash
python analysis.py
```

Generate the visualization:

```bash
python visualize.py
```

Results are saved in the `results/` directory.

## Evaluation Setup

The current prototype includes:

- 15 predefined test cases
- 5 executions per test case
- 75 total tool executions
- Easy, medium, and hard test-case labels
- Three intentionally invalid test cases to evaluate error handling

## Example Results

In a sample experiment:

| Metric | Result |
|---|---|
| Total executions | 75 |
| Successful tool executions | 60 |
| Intentional error executions | 15 |
| Observed error rate | 20% |
| Tool-selection accuracy | 100% |

The tool-selection accuracy was measured only on the predefined queries and does not establish general routing performance.

The simulated random-response tool produces variable outputs, so consistency measurements may differ between runs.

## Architecture

```text
Natural-Language Query
         |
         v
   Rule-Based Agent
         |
         v
    Selected Tool
         |
         v
   Tool Execution
         |
         v
     JSON Logger
         |
         v
  Evaluation Analysis
         |
         v
  Report + Visualization
```

## Limitations

- Tool selection uses simple keyword-based rules rather than a trained AI model.
- The random-response tool simulates nondeterministic behavior; it is not a real LLM.
- The evaluation dataset is small and predefined.
- The difficulty labels are manually assigned and are not independently validated.
- The current consistency metric measures the frequency of the most common output, not semantic correctness.
- Intentional input errors are included in the reported error rate.
- The framework does not yet support real multi-agent orchestration or LLM-as-a-judge evaluation.

## Future Improvements

- Integrate real LLM-based tools
- Add more diverse test cases
- Implement automatic evaluation of response quality
- Introduce LLM-as-a-judge experiments
- Improve tool-routing and error-recovery strategies
- Compare repeated evaluations across different models

## Project Status

Functional educational prototype. Core execution, logging, analysis, and visualization are implemented.
