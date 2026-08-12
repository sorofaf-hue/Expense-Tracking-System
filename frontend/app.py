import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_by_category
from analytics_by_months import analytics_by_months

# Page configuration
st.set_page_config(
    page_title="Expense Tracking System",
    page_icon="💰",
    layout="wide"
)

# Header
st.title("💰 Expense Tracking System")
st.caption("Track, manage, and analyze your daily expenses.")

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Add / Update", "📊 Analytics_by_Category", "📅 Analytics_by_Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_by_category()

with tab3:
    analytics_by_months()