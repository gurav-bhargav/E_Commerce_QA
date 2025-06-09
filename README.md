# E_Commerce_QA

This project is an automated testing framework for an E-Commerce application using **Playwright** and **Behave**. It includes workflows that automatically run tests and provide results whenever new scenarios are added and pushed to the repository.

---

## Features
- Automated browser testing using Playwright.
- Behavior-driven development (BDD) with Behave.
- CI/CD integration using GitHub Actions.
- Automatic generation of logs, screenshots, and video recordings for test scenarios.

---

## Project Structure


---

## Prerequisites
1. Install Python (3.9 or later).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
    python -m playwright install
   ```
   
How to Add and Run a New Scenario
1. Create a New Scenario:
Add a new .feature file in the features/scenarios/ directory.
Write your BDD scenario in Gherkin syntax.

2. Implement Step Definitions:
Add or update step definitions in the features/steps/ directory to match your scenario.

3. Push Changes to GitHub:
Commit your changes and push them to the repository:
```bash
git add .
git commit -m "Add new scenario for [feature_name]"
git push origin main
```

4. Workflow Execution:
The GitHub Actions workflow will automatically run the tests for the new scenario.
Results (logs, screenshots, and videos) will be generated in the reports/ directory.
<hr> 

### Workflow Execution:
The GitHub Actions workflow will automatically run the tests for the new scenario.
Results (logs, screenshots, and videos) will be generated in the reports/ directory.


## CI/CD Workflow
The project uses GitHub Actions for continuous integration. The workflow is triggered on every push or pull_request to the main branch.

#### Workflow Steps:
  1. Checkout Code: Clones the repository.
  2. Set Up Python: Installs Python and dependencies.
  3. Install Playwright Browsers: Sets up Playwright.
  4. Run Tests: Executes all scenarios using Behave.
  5. Generate Reports: Saves logs, screenshots, and videos in the reports/ directory.


### Logs and Reports
- Logs: Stored in reports/logs/ with detailed information about each test run.
- Screenshots: Captured for each scenario and saved in reports/screenshots/.
- Videos: Recorded for each test run and saved in reports/videos/.

### Running Tests Locally
To run all scenarios locally, execute:
```bash
python runner.py
```

### Contributing
1. Fork the repository.
2. Create a new branch for your feature:
```bash
git checkout -b feature/new-scenario
```
3. Push your changes and create a pull request.


