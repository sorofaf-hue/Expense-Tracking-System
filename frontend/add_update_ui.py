import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    date_str = selected_date.strftime("%Y-%m-%d")
    
    try:
        response = requests.get(f"{API_URL}/expenses/{date_str}", timeout=2)
        if response.status_code == 200:
            existing_expenses = response.json()
           
        else:
            st.error("Failed to retrieve expenses")
            existing_expenses = []
    except requests.exceptions.RequestException:
        st.error("Backend server is not running or unreachable.")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses) and isinstance(existing_expenses[i], dict):
                amount = float(existing_expenses[i].get('amount', 0.0))
                category = existing_expenses[i].get('category', "Shopping")
                notes = existing_expenses[i].get('notes', "")
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            try:
                cat_index = categories.index(category)
            except ValueError:
                cat_index = 0

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{date_str}_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=cat_index,
                                             key=f"category_{date_str}_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{date_str}_{i}", label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            try:
                response = requests.post(f"{API_URL}/expenses/{date_str}", json=filtered_expenses, timeout=2)
                if response.status_code == 200:
                    st.success("Expenses updated successfully!")
                else:
                    st.error("Failed to update expenses.")
            except requests.exceptions.RequestException:
                st.error("Connection error while posting data to backend.")

if __name__ == "__main__":
    add_update_tab()