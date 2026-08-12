# Expense Management System

## Project Overview

The Expense Management System is a Python-based application for recording, managing, and analyzing daily expenses. It uses a Streamlit frontend for the user interface, a FastAPI backend for handling API requests, and MySQL for storing expense data.

## Features

- Add and update daily expenses
- Select an expense date and retrieve existing records
- Record expense amount, category, and notes
- Categorize expenses as Rent, Food, Shopping, Entertainment, or Other
- Analyze expenses over a selected date range
- Calculate total spending and percentage breakdown by category
- Display analytics using a bar chart and table
- Log database operations
- Test database helper functions with Pytest

## Technologies Used

- **Python**
- **Streamlit** — frontend interface
- **FastAPI** — backend REST API
- **MySQL** — database
- **Pandas** — analytics data processing
- **Pydantic** — request/data validation
- **Requests** — communication between frontend and backend
- **Uvicorn** — FastAPI server
- **Pytest** — testing

## System Workflow

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
MySQL Database
  ↓
FastAPI Backend
  ↓
Streamlit Frontend
  ↓
User
```

### Expense Entry / Update

```text
Select Date
    ↓
Retrieve existing expenses
    ↓
Enter or update Amount, Category and Notes
    ↓
Submit
    ↓
Send data to FastAPI
    ↓
Update MySQL database
    ↓
Display success/error message
```

### Analytics

```text
Select Start Date and End Date
    ↓
Request analytics from FastAPI
    ↓
Calculate expense totals by category
    ↓
Calculate category percentages
    ↓
Process results with Pandas
    ↓
Display bar chart and table
```

## Project Structure

```text
5_project_two_expense_management/
│
├── backend/
│   ├── db_helper.py
│   ├── logging_setup.py
│   └── server.py
│
├── database/
│   └── expense_db_creation.sql
│
├── frontend/
│   ├── add_update_ui.py
│   ├── analytics_ui.py
│   └── app.py
│
├── tests/
│   ├── backend/
│   │   └── test_db_helper.py
│   └── conftest.py
│
├── requirements.txt
└── README.md
```

## Database

The project uses a MySQL database named `expense_manager`.

The main `expenses` table contains:

| Column | Description |
|---|---|
| `id` | Unique expense ID |
| `expense_date` | Date of the expense |
| `amount` | Expense amount |
| `category` | Expense category |
| `notes` | Additional information about the expense |

The database creation script is available in:

```text
database/expense_db_creation.sql
```

## API Endpoints

### Get Expenses

```text
GET /expenses/{expense_date}
```

Retrieves expenses for a specific date.

### Add / Update Expenses

```text
POST /expenses/{expense_date}
```

Replaces the expenses for the selected date with the submitted expense records.

### Get Analytics

```text
POST /analytics/
```

Accepts a start date and end date and returns expense totals and percentage breakdowns by category.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd 5_project_two_expense_management
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up MySQL

Create the database and table using:

```text
database/expense_db_creation.sql
```

Before running the backend, make sure the MySQL connection details in `backend/db_helper.py` match your local MySQL configuration.

> **Security note:** For a real deployment, database credentials should be stored in environment variables rather than directly in the source code.

## Running the Application

### Start the FastAPI Backend

Open a terminal in the `backend` directory:

```bash
cd backend
uvicorn server:app --reload
```

The API will run at:

```text
http://localhost:8000
```

### Start the Streamlit Frontend

Open another terminal from the project root:

```bash
streamlit run frontend/app.py
```

The Streamlit application will open in your browser.

## Testing

The project uses Pytest for testing database helper functions.

From the project root:

```bash
pytest
```

The current test suite includes tests for:

- Retrieving expenses for a valid date
- Retrieving expenses for a date with no records
- Retrieving an empty analytics summary for an invalid date range

## Future Improvements

Possible improvements include:

- Moving database credentials to environment variables
- Adding user authentication
- Adding more analytics and visualizations
- Supporting more expense categories
- Adding monthly and yearly reports
- Improving error handling and validation
- Expanding the automated test suite

## Documentation

Additional project documentation or a project report can be added to the repository and linked here.

## Author

**Fortune Sorofa**

