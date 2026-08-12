# 💰 Expense Tracking System

A full-stack expense tracking application built with **Streamlit**, **FastAPI**, and **MySQL**. The system allows users to record and update daily expenses, then analyze spending by category and month through an interactive web interface.

## ✨ Features

- Add and update daily expenses
- Select a date and retrieve existing expenses
- Record:
  - Amount
  - Category
  - Notes
- Expense categories:
  - Rent
  - Food
  - Shopping
  - Entertainment
  - Other
- Analyze expenses over a selected date range
- View spending breakdown by category
- Interactive pie chart and category table
- View monthly spending
- Set a monthly budget
- Calculate:
  - Monthly budget
  - Total spent
  - Average monthly spending
  - Remaining budget
  - Budget used percentage
- Visual monthly spending chart
- Budget exceeded/remaining status messages
- FastAPI REST API connecting the frontend to MySQL
- Database operation logging
- Automated tests with Pytest

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Streamlit** | Web application frontend |
| **FastAPI** | Backend REST API |
| **MySQL** | Database |
| **Pandas** | Data processing and analytics |
| **Pydantic** | API data validation |
| **Requests** | Frontend-to-backend communication |
| **Uvicorn** | FastAPI development server |
| **Pytest** | Automated testing |

---

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │   Streamlit UI      │
                │     Frontend        │
                └──────────┬──────────┘
                           │
                           │ HTTP Requests
                           ▼
                ┌─────────────────────┐
                │     FastAPI         │
                │      Backend        │
                └──────────┬──────────┘
                           │
                           │ SQL Queries
                           ▼
                ┌─────────────────────┐
                │       MySQL         │
                │      Database       │
                └─────────────────────┘
```

---

## 📂 Project Structure

```text
5_project_two_expense_management/
│
├── backend/
│   ├── db_helper.py
│   ├── logging_setup.py
│   ├── server.py
│   └── server.log
│
├── database/
│   └── expense_db_creation.sql
│
├── frontend/
│   ├── add_update_ui.py
│   ├── analytics_by_category.py
│   ├── analytics_by_months.py
│   └── app.py
│
├── screenshots/
│   ├── Add_or_Upadate_Tab.png
│   ├── Analystics_by_ Category_Tab.png
│   ├── Bar_Chart_and _Table.png
│   ├── Category_Table.png
│   ├── Expense Entry & Table.png
│   ├── Month_of_August.png
│   ├── Month_of_September.png
│   ├── Ovaerall_Summary.png
│   └── Pie_Chart_Category.png
│
├── tests/
│   ├── backend/
│   │   └── test_db_helper.py
│   └── conftest.py
│
├── requirements.txt
└── README.md
```

> The repository also contains an `exercise_solution/` directory from the original project materials. The application described in this README uses the main `backend/`, `frontend/`, `database/`, and `tests/` directories.

---

## 🗄️ Database

The application uses a MySQL database named:

```text
expense_manager
```

The database creation script is located at:

```text
database/expense_db_creation.sql
```

The main `expenses` table stores:

| Column | Description |
|---|---|
| `id` | Unique expense ID |
| `expense_date` | Date of the expense |
| `amount` | Expense amount |
| `category` | Expense category |
| `notes` | Additional information |

---

## 🔌 API Endpoints

### Get Expenses

```http
GET /expenses/{expense_date}
```

Retrieves expenses recorded for a specific date.

### Add / Update Expenses

```http
POST /expenses/{expense_date}
```

Updates the expenses for the selected date.

### Category Analytics

```http
POST /analytics/
```

Returns total spending and percentage breakdown by expense category for a selected date range.

### Monthly Analytics

```http
GET /analytics_by_month/
```

Returns total spending grouped by month.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd 5_project_two_expense_management
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL

Create the database and `expenses` table using:

```text
database/expense_db_creation.sql
```

Then configure the MySQL connection in:

```text
backend/db_helper.py
```

**Important:** Do not upload database passwords or other secrets to GitHub. Use environment variables or a local configuration file that is excluded through `.gitignore`.

---

## ▶️ Running the Application

The application requires **two terminals**.

### Terminal 1 — Start the FastAPI backend

From the project root:

```bash
cd backend
uvicorn server:app --reload
```

The API will run at:

```text
http://localhost:8000
```

### Terminal 2 — Start the Streamlit frontend

From the project root:

```bash
streamlit run frontend/app.py
```

Streamlit will provide a local URL that can be opened in your browser.

---

## 📊 Application Screenshots

### Add / Update Expenses

![Add or Update Tab](screenshots/Add_or_Upadate_Tab.png)

### Expense Entry and Table

![Expense Entry and Table](screenshots/Expense%20Entry%20%26%20Table.png)

### Category Analytics

![Analytics by Category](screenshots/Analystics_by_%20Category_Tab.png)

### Category Pie Chart

![Category Pie Chart](screenshots/Pie_Chart_Category.png)

### Category Table

![Category Table](screenshots/Category_Table.png)

### Monthly Analytics

![August](screenshots/Month_of_August.png)

![September](screenshots/Month_of_September.png)

### Overall Budget Summary

![Overall Summary](screenshots/Ovaerall_Summary.png)

### Monthly Bar Chart and Table

![Bar Chart and Table](screenshots/Bar_Chart_and%20_Table.png)

---

## 🧪 Testing

The project uses **Pytest** for automated testing.

Run the tests from the project root:

```bash
pytest
```

The current test suite checks functionality including:

- Retrieving expenses for a valid date
- Handling dates with no expense records
- Handling an analytics query with no matching records

---

## 🔄 Application Workflow

### Adding or Updating an Expense

```text
Select Date
     ↓
Retrieve Existing Expenses
     ↓
Enter / Update Amount, Category and Notes
     ↓
Submit
     ↓
Streamlit sends request to FastAPI
     ↓
FastAPI updates MySQL
     ↓
Success / Error message displayed
```

### Category Analytics

```text
Select Start Date and End Date
     ↓
Request data from FastAPI
     ↓
Calculate spending by category
     ↓
Calculate percentages
     ↓
Process data with Pandas
     ↓
Display charts and tables
```

### Monthly Budget Analysis

```text
Retrieve monthly spending
     ↓
Enter Monthly Budget
     ↓
Calculate spending and remaining budget
     ↓
Calculate budget usage percentage
     ↓
Display monthly budget status
     ↓
Display monthly spending chart and table
```

---

## 🚀 Future Improvements

Potential improvements for future versions include:

- Move database credentials to environment variables
- Add user authentication
- Add more expense categories
- Add yearly analytics
- Add expense search and filtering
- Expand automated test coverage
- Add data export functionality
- Deploy the application online

---

## 👤 Author

**Fortune Sorofa**

