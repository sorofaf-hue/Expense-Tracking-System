import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_by_category():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        import plotly.express as px

        fig = px.pie(
            df_sorted,
            names="Category",
            values="Total",
            color_discrete_sequence=[
                "#0d5c75",  # Deep Muted Teal (Rent)
                "#1e40af",  # Deep Rich Blue (Food)
                "#5b21b6",  # Deep Indigo/Violet (Shopping)
                "#9f1239",  # Deep Muted Rose/Red (Entertainment)
                "#c2410c",  # Deep Rust Orange (Other)
                "#854d0e",  # Deep Olive Gold
                "#334155",  # Dark Slate Grey
            ],
        )

        # Pull only the largest slice (Rent)
        pull_list = [0.05 if i == 0 else 0 for i in range(len(df_sorted))]

        fig.update_traces(
            textinfo="percent+label",
            textposition="outside",  # Keeps small slices readable
            pull=pull_list,
            marker=dict(line=dict(color="#0f172a", width=2)),  # Dark border to blend with theme
        )

        # Clean up layout margins so outside labels fit nicely
        fig.update_layout(
            margin=dict(t=30, b=30, l=40, r=40),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        st.plotly_chart(fig, use_container_width=True)
        

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)

