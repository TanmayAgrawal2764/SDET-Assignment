# SDET Assignment @Pibit.ai

## Introduction
This assignment demonstrates my ability to write and execute tests in Python, automate testing processes, and identify and handle edge cases.
Here Part1Sol1.py and Part1Sol2.py are the testing solutions of Part1.py task while Part2Sol1.py is the testing solution of Part2.py task.

## Setup Instructions
1. **Unit Tests using unittest:**
   - Ensure you have Python installed.
   - Install `unittest` if not already installed by command `pip install unittest`.
   - Run the unit tests using: `python -m unittest Part1Sol1.py` or by simply running the test file using python.

2. **Unit Tests using pytest:**
   - Ensure you have Python installed.
   - Install `pytest` if not already installed  by command `pip install pytest`.
   - Run the unit tests using: `pytest Part1Sol2.py` or by using command: `py.test`(if used, make sure the to rename the file which starts with prefix `test`).

3. **Selenium Tests:**
   - Ensure you have `selenium` installed: `pip install selenium`.
   - Install the Chrome WebDriver and ensure it is in your PATH.
   - Important:- Update the path to your HTML file in the script in line 10.
   - Run the Selenium tests using: `python Part2Sol1.py` or by simply running the test script using python.

## Approach and Thought Process
- For unit tests using unittest, I focused on covering typical cases, edge cases, and invalid inputs.
- For unit tests using pytest, I focused on covering typical cases, edge cases, and invalid inputs.
- For Selenium automation, I ensured the script could handle various scenarios like successful and failed logins, and empty field handling.

## Assumptions and Decisions
- Used both unittest and pytest for Part 1 task.
- Used unittest module for selenium login page test.
- Assumed the HTML structure provided remains unchanged.
- Assumed that post submission of html form, a successful or unsuccessful or empty field message is displayed as per the situation.
- Used Chrome WebDriver for automation.

## Tools Used
- Python
- unittest
- pytest
- Selenium

## Contact
For any queries, please contact me at tanmayagrawal2764@gmail.com.