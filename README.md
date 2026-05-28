# Expense and Placements Analyzer

A Python-based mini project that helps users manage daily expenses and track placement applications using **Pandas**, **CSV File Handling**, and core Python concepts.

This project demonstrates:

* File handling using CSV files
* Data analysis using Pandas
* Menu-driven programming
* CRUD operations
* Report generation

---

# Features

## Expense Management

* Add expense
* View expenses
* Delete expense
* Analyze expenses
* Category-wise spending
* Highest spending in each category

## Placement Management

* Add placement applications
* View placements
* Placement status analysis

## Report Generation

* Generates a text-based report containing:

  * Total spending
  * Average spending
  * Total applications
  * Category-wise expense summary

---

# Technologies Used

* Python
* Pandas
* CSV File Handling

---

# Project Structure

```plaintext
project/
│
├── app.py
├── expenses.csv
├── placements.csv
├── README.md
│
├── reports/
│   └── report.txt
```

---

# Important Setup Instructions

## 1. Install Pandas

Run this command in terminal:

```bash
pip install pandas
```

---

## 2. Create Reports Folder

Before generating reports, create a folder named:

```plaintext
reports
```

Inside your project directory.

Final structure should look like:

```plaintext
project/
│
├── reports/
```

If the folder is not created, report generation may fail.

Because Python refuses to magically create folders unless specifically instructed. Very principled behavior for a language that lets people name variables things like `banana123`.

---

# How to Run the Project

Open terminal inside the project folder and run:

```bash
python app.py
```

---

# Menu Options

```plaintext
1. Add Expense
2. View Expense
3. Delete Expense
4. Analyze Expense
5. Add Placements
6. View Placements
7. Generate Report
8. Exit
```

---

# Sample Expense Data

```csv
Date,Amount,Category,Description
2026-05-20,250,Food,Burger
```

---

# Sample Placement Data

```csv
Company,Role,Status,Deadline
Amazon,SDE Intern,Interview,2026-06-01
```

---

# Concepts Used

* Functions
* Loops
* Conditional Statements
* Exception Handling
* Pandas DataFrames
* CSV Reading/Writing
* GroupBy Operations
* File Handling

---

# Future Improvements

* Graph visualization using Matplotlib
* GUI using Tkinter or Streamlit
* Budget alerts
* Login system
* Database integration

---

# Author

Saiteja

GitHub: Saitejas22
