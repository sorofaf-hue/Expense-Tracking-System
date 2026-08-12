import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_by_months():
    st.title("Expense Breakdown By Months")

    monthly_budget = st.number_input(
        "Monthly Budget",
        min_value=0.0,
        value=20000.0,
        step=100.0
    )

    response = requests.get(f"{API_URL}/analytics_by_month/")

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df = df.sort_values("month_number")

        df["remaining"] = monthly_budget - df["total"]

        df["budget_used"] = (
            (df["total"] / monthly_budget) * 100
            if monthly_budget > 0
            else 0
        )

        total_spent = df["total"].sum()
        average_monthly_spending = df["total"].mean()

        total_budget = monthly_budget * len(df)
        total_remaining = total_budget - total_spent

        overall_budget_used = (
        (total_spent / total_budget) * 100
        if total_budget > 0
        else 0
        )

        st.subheader("💰 Overall Budget Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Monthly Budget", f"₹{monthly_budget:,.2f}")

        with col2:
            st.metric("Total Spent", f"₹{total_spent:,.2f}")

        with col3:
            st.metric("Average Monthly Spending", f"₹{average_monthly_spending:,.2f}")

        st.subheader("Budget Overview")

        for _, row in df.iterrows():
            st.write(f"### {row['month_name']}")

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric("Budget", f"₹{monthly_budget:,.2f}")

            with col2:
                st.metric("Spent", f"₹{row['total']:,.2f}")

            with col3:
                st.metric("Remaining", f"₹{row['remaining']:,.2f}")

            with col4:
                st.metric("Total Remaining", f"₹{total_remaining:,.2f}")

            with col5:
                st.metric("Overall Budget Used", f"{overall_budget_used:.2f}%")

            st.write(f"Budget Used: {row['budget_used']:.2f}%")

            progress = min(row["budget_used"] / 100, 1.0)
            st.progress(progress)

            if row["remaining"] < 0:
                st.error(
                    f"⚠️ Budget exceeded by ₹{abs(row['remaining']):,.2f}"
                )
            else:
                st.success(
                    f"₹{row['remaining']:,.2f} remaining"
                )

            st.divider()

        st.bar_chart(
            data=df.set_index("month_name")["total"]
        )

        df = df.rename(columns={
            "month_number": "Month Number",
            "month_name": "Month",
            "total": "Total Expense"
        })

        # Create a separate DataFrame for the table
        df_table = df.copy()

        df_table["Total Expense"] = df_table["Total Expense"].map("{:.2f}".format)
        df_table["remaining"] = df_table["remaining"].map("{:.2f}".format)
        df_table["budget_used"] = df_table["budget_used"].map("{:.2f}".format)

        st.table(df_table)

    else:
        st.error("Failed to retrieve monthly analytics")