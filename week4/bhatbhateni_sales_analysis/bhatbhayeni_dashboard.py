"""
BSCS - Bhatbhateni Sales Streamlit Dashboard
Professional interactive analytics dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Bhatbhateni Sales Analytics",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS FOR PROFESSIONAL STYLING
# ============================================================
st.markdown("""
<style>
    /* Main title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: center;
        padding: 1rem 0;
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    
    .metric-card h3 {
        font-size: 1.8rem;
        margin: 0;
        font-weight: 700;
    }
    
    .metric-card p {
        font-size: 0.9rem;
        margin: 5px 0 0 0;
        opacity: 0.9;
    }
    
    /* Different color variants */
    .metric-card.green {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    .metric-card.orange {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    .metric-card.blue {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    .metric-card.purple {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #333;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #2c3e50;
        padding: 0.5rem 0;
        border-bottom: 2px solid #3498db;
        margin-bottom: 1rem;
    }
    
    /* Filter info box */
    .filter-info {
        background-color: #e8f4f8;
        padding: 12px 16px;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 10px 0;
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Better table styling */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_currency(value):
    """Format number as Nepali currency"""
    if pd.isna(value):
        return "Rs. 0"
    return f"Rs. {value:,.2f}"

def format_number(value):
    """Format number with commas"""
    if pd.isna(value):
        return "0"
    return f"{int(value):,}"

def set_chart_style(ax, title, xlabel="", ylabel=""):
    """Apply consistent styling to matplotlib charts"""
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20, color='#2c3e50')
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=11, color='#555')
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=11, color='#555')
    ax.tick_params(axis='both', labelsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

# ============================================================
# LOAD CLEANED DATA
# ============================================================
@st.cache_data
def load_data():
    """Load cleaned sales data from CSV file"""
    file_path = r"C:\Users\Dell\Documents\Prg200\PRG200\week4\bhatbhateni_sales_analysis\bhatbhateni_sales_cleaned.csv"
    df = pd.read_csv(file_path)
    
    # Convert Date back to datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Create Month-Year for easier filtering
    df["MonthYear"] = df["Date"].dt.to_period("M").astype(str)
    
    # Create proper day names
    day_name_map = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"
    }
    df["DayName"] = df["DayOfWeek"].map(day_name_map)
    
    return df

df = load_data()

# ============================================================
# SIDEBAR FILTERS - PROFESSIONAL STYLING
# ============================================================
with st.sidebar:
    st.markdown("## Dashboard Controls")
    st.markdown("---")
    
    # City filter
    available_cities = ["All Cities"] + sorted(df["City"].unique().tolist())
    selected_city = st.selectbox("City", available_cities, index=0)
    
    # Branch filter based on selected city
    if selected_city != "All Cities":
        available_branches = ["All Branches"] + sorted(df[df["City"] == selected_city]["Branch"].unique().tolist())
    else:
        available_branches = ["All Branches"] + sorted(df["Branch"].unique().tolist())
    selected_branch = st.selectbox("Branch", available_branches, index=0)
    
    # Product Category filter
    available_categories = ["All Categories"] + sorted(df["ProductCategory"].unique().tolist())
    selected_category = st.selectbox("Product Category", available_categories, index=0)
    
    # Payment Method filter
    available_payments = ["All Methods"] + sorted(df["PaymentMethod"].unique().tolist())
    selected_payment = st.selectbox("Payment Method", available_payments, index=0)
    
    st.markdown("---")
    
    # Date range filter
    st.markdown("**Date Range**")
    min_date = df["Date"].min().date()
    max_date = df["Date"].max().date()
    date_range = st.date_input(
        "Select dates",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("*Tip: Use filters to explore specific data segments.*")

# ============================================================
# APPLY FILTERS
# ============================================================
filtered_df = df.copy()

if selected_city != "All Cities":
    filtered_df = filtered_df[filtered_df["City"] == selected_city]

if selected_branch != "All Branches":
    filtered_df = filtered_df[filtered_df["Branch"] == selected_branch]

if selected_category != "All Categories":
    filtered_df = filtered_df[filtered_df["ProductCategory"] == selected_category]

if selected_payment != "All Methods":
    filtered_df = filtered_df[filtered_df["PaymentMethod"] == selected_payment]

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        (filtered_df["Date"].dt.date >= start_date) &
        (filtered_df["Date"].dt.date <= end_date)
    ]

# ============================================================
# MAIN HEADER
# ============================================================
st.markdown('<div class="main-title">Bhatbhateni Super Store</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Interactive Sales Analytics Dashboard</div>', unsafe_allow_html=True)

# Show active filters
filter_text = []
if selected_city != "All Cities":
    filter_text.append(f"City: {selected_city}")
if selected_branch != "All Branches":
    filter_text.append(f"Branch: {selected_branch}")
if selected_category != "All Categories":
    filter_text.append(f"Category: {selected_category}")
if selected_payment != "All Methods":
    filter_text.append(f"Payment: {selected_payment}")

if filter_text:
    st.markdown(f'<div class="filter-info"><strong>Active Filters:</strong> {" | ".join(filter_text)}</div>', unsafe_allow_html=True)

# ============================================================
# PROFESSIONAL KPI CARDS
# ============================================================
st.markdown("---")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    total_revenue = filtered_df["TotalAmount"].sum()
    st.metric("Total Revenue", f"Rs. {total_revenue/1000000:.2f}M")

with kpi2:
    avg_transaction = filtered_df["TotalAmount"].mean()
    st.metric("Avg Transaction", f"Rs. {avg_transaction:,.0f}")

with kpi3:
    unique_customers = filtered_df["CustomerID"].nunique()
    st.metric("Unique Customers", f"{unique_customers:,}")

with kpi4:
    total_items = filtered_df["Quantity"].sum()
    st.metric("Units Sold", f"{total_items:,}")

st.markdown("---")

# ============================================================
# TABS FOR DIFFERENT VIEWS
# ============================================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview",
    "Trends",
    "Locations",
    "Products",
    "Customers",
    "Payments"
])

# ============================================================
# TAB 1: OVERVIEW - PROFESSIONAL LAYOUT
# ============================================================
with tab1:
    st.header("Executive Overview")
    
    # Row 1: Category and Payment side by side
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.markdown("**Revenue by Category**")
        category_revenue = filtered_df.groupby("ProductCategory")["TotalAmount"].sum().sort_values(ascending=True)
        
        if not category_revenue.empty:
            fig, ax = plt.subplots(figsize=(10, 5))
            colors = plt.cm.Set3(np.linspace(0, 1, len(category_revenue)))
            category_revenue.plot(kind="barh", ax=ax, color=colors, edgecolor='black', linewidth=0.5)
            ax.set_xlabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Revenue by Product Category", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='y', labelsize=9)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='x', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")
    
    with col_right:
        st.markdown("**Payment Methods**")
        payment_counts = filtered_df["PaymentMethod"].value_counts()
        
        if not payment_counts.empty:
            # Horizontal bar chart instead of pie to avoid overlap
            fig, ax = plt.subplots(figsize=(8, 5))
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
            payment_counts.plot(kind="barh", ax=ax, color=colors[:len(payment_counts)], edgecolor='black', linewidth=0.5)
            ax.set_xlabel("Number of Transactions", fontsize=10, color='#555')
            ax.set_title("Popularity of Payment Methods", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='y', labelsize=9)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='x', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")
    
    st.markdown("---")
    
    # Row 2: City and Branch
    col_city, col_branch = st.columns(2)
    
    with col_city:
        st.markdown("**Revenue by City**")
        city_revenue = filtered_df.groupby("City")["TotalAmount"].sum().sort_values(ascending=False)
        
        if not city_revenue.empty:
            fig, ax = plt.subplots(figsize=(8, 5))
            colors = plt.cm.viridis(np.linspace(0, 0.8, len(city_revenue)))
            city_revenue.plot(kind="bar", ax=ax, color=colors, edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Total Revenue by City", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")
    
    with col_branch:
        st.markdown("**Revenue by Branch**")
        branch_revenue = filtered_df.groupby("Branch")["TotalAmount"].sum().sort_values(ascending=False)
        
        if not branch_revenue.empty:
            fig, ax = plt.subplots(figsize=(8, 5))
            colors = plt.cm.plasma(np.linspace(0.2, 0.8, len(branch_revenue)))
            branch_revenue.plot(kind="bar", ax=ax, color=colors, edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Total Revenue by Branch", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")

# ============================================================
# TAB 2: SALES TRENDS
# ============================================================
with tab2:
    st.header("Sales Trend Analysis")
    
    # Monthly Revenue Trend
    st.markdown("### Monthly Revenue Trend (2025)")
    monthly_revenue = filtered_df.groupby("MonthYear")["TotalAmount"].sum().reset_index()
    
    if not monthly_revenue.empty:
        st.line_chart(monthly_revenue.set_index("MonthYear")["TotalAmount"], use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")
    
    st.markdown("---")
    
    # Day of week and Weekend analysis
    col_dow1, col_dow2 = st.columns(2)
    
    with col_dow1:
        st.markdown("### Revenue by Day of Week")
        daily_revenue = filtered_df.groupby("DayName")["TotalAmount"].sum()
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        daily_revenue = daily_revenue.reindex([d for d in day_order if d in daily_revenue.index])
        
        if not daily_revenue.empty:
            fig, ax = plt.subplots(figsize=(10, 5))
            colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#99CCFF', '#FFB366']
            daily_revenue.plot(kind="bar", ax=ax, color=colors[:len(daily_revenue)], edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Revenue by Day of Week", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")
    
    with col_dow2:
        st.markdown("### Weekend vs Weekday")
        filtered_df["IsWeekend"] = filtered_df["DayOfWeek"].isin([5, 6])
        weekend_data = filtered_df.groupby("IsWeekend")["TotalAmount"].agg(["sum", "count", "mean"])
        weekend_data.index = ["Weekday", "Weekend"]
        
        if not weekend_data.empty:
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))
            
            # Total revenue comparison
            weekend_data["sum"].plot(kind="bar", ax=axes[0], color=["#3498db", "#e74c3c"], edgecolor='black', linewidth=0.5)
            axes[0].set_title("Total Revenue", fontsize=12, fontweight='bold', color='#2c3e50')
            axes[0].set_ylabel("Rs.", fontsize=10)
            axes[0].tick_params(axis="x", rotation=0)
            axes[0].spines['top'].set_visible(False)
            axes[0].spines['right'].set_visible(False)
            axes[0].grid(axis='y', alpha=0.3, linestyle='--')
            
            # Average transaction comparison
            weekend_data["mean"].plot(kind="bar", ax=axes[1], color=["#2ecc71", "#f39c12"], edgecolor='black', linewidth=0.5)
            axes[1].set_title("Avg Transaction Value", fontsize=12, fontweight='bold', color='#2c3e50')
            axes[1].set_ylabel("Rs.", fontsize=10)
            axes[1].tick_params(axis="x", rotation=0)
            axes[1].spines['top'].set_visible(False)
            axes[1].spines['right'].set_visible(False)
            axes[1].grid(axis='y', alpha=0.3, linestyle='--')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.warning("No data available")
    
    # Transaction volume
    st.markdown("### Transaction Volume by Month")
    monthly_count = filtered_df.groupby("MonthYear")["TransactionID"].count().reset_index()
    if not monthly_count.empty:
        st.bar_chart(monthly_count.set_index("MonthYear")["TransactionID"], use_container_width=True)

# ============================================================
# TAB 3: BRANCH & CITY PERFORMANCE
# ============================================================
with tab3:
    st.header("Branch & City Performance")
    
    # Top performers
    if not filtered_df.empty:
        top_branch = filtered_df.groupby("Branch")["TotalAmount"].sum().idxmax()
        top_city = filtered_df.groupby("City")["TotalAmount"].sum().idxmax()
        top_branch_revenue = filtered_df.groupby("Branch")["TotalAmount"].sum().max()
        top_city_revenue = filtered_df.groupby("City")["TotalAmount"].sum().max()
    else:
        top_branch = top_city = "N/A"
        top_branch_revenue = top_city_revenue = 0
    
    m1, m2 = st.columns(2)
    with m1:
        st.info(f"**Top Branch:** {top_branch} | Revenue: Rs. {top_branch_revenue:,.2f}")
    with m2:
        st.info(f"**Top City:** {top_city} | Revenue: Rs. {top_city_revenue:,.2f}")
    
    st.markdown("---")
    
    # Branch comparison
    st.markdown("### Branch Performance Comparison")
    if not filtered_df.empty:
        branch_stats = filtered_df.groupby("Branch").agg({
            "TotalAmount": ["sum", "mean", "count"]
        }).round(2)
        branch_stats.columns = ["Total Revenue", "Avg Transaction", "Transactions"]
        branch_stats = branch_stats.sort_values("Total Revenue", ascending=False)
        
        # Format for display
        branch_display = branch_stats.copy()
        branch_display["Total Revenue"] = branch_display["Total Revenue"].apply(lambda x: f"Rs. {x:,.2f}")
        branch_display["Avg Transaction"] = branch_display["Avg Transaction"].apply(lambda x: f"Rs. {x:,.2f}")
        branch_display["Transactions"] = branch_display["Transactions"].apply(lambda x: f"{int(x):,}")
        
        st.dataframe(branch_display, use_container_width=True)
        
        # Branch revenue bar chart
        fig, ax = plt.subplots(figsize=(10, 5))
        branch_stats["Total Revenue"].plot(kind="bar", ax=ax, color="#2ecc71", edgecolor='black', linewidth=0.5)
        ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
        ax.set_title("Total Revenue by Branch", fontsize=13, fontweight='bold', pad=15)
        ax.tick_params(axis='x', rotation=45)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    else:
        st.warning("No data available")
    
    # City performance
    st.markdown("### City Performance")
    if not filtered_df.empty:
        city_stats = filtered_df.groupby("City").agg({
            "TotalAmount": ["sum", "mean", "count"]
        }).round(2)
        city_stats.columns = ["Total Revenue", "Avg Transaction", "Transactions"]
        city_stats = city_stats.sort_values("Total Revenue", ascending=False)
        
        col_city1, col_city2 = st.columns(2)
        with col_city1:
            city_display = city_stats.copy()
            city_display["Total Revenue"] = city_display["Total Revenue"].apply(lambda x: f"Rs. {x:,.2f}")
            city_display["Avg Transaction"] = city_display["Avg Transaction"].apply(lambda x: f"Rs. {x:,.2f}")
            city_display["Transactions"] = city_display["Transactions"].apply(lambda x: f"{int(x):,}")
            st.dataframe(city_display, use_container_width=True)
        
        with col_city2:
            fig, ax = plt.subplots(figsize=(8, 4))
            city_stats["Total Revenue"].plot(kind="bar", ax=ax, color="#3498db", edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Revenue by City", fontsize=13, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

# ============================================================
# TAB 4: PRODUCT INSIGHTS
# ============================================================
with tab4:
    st.header("Product Analysis")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("### Revenue by Category")
        cat_revenue = filtered_df.groupby("ProductCategory")["TotalAmount"].sum().sort_values(ascending=False)
        if not cat_revenue.empty:
            st.bar_chart(cat_revenue, use_container_width=True)
        else:
            st.warning("No data available")
    
    with col_p2:
        st.markdown("### Transactions by Category")
        cat_transactions = filtered_df.groupby("ProductCategory")["TransactionID"].count().sort_values(ascending=False)
        if not cat_transactions.empty:
            st.bar_chart(cat_transactions, use_container_width=True)
        else:
            st.warning("No data available")
    
    st.markdown("---")
    
    # Top products
    col_top1, col_top2 = st.columns(2)
    
    with col_top1:
        st.markdown("### Top 10 Products by Quantity")
        product_qty = filtered_df.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(10)
        if not product_qty.empty:
            product_qty_df = product_qty.reset_index()
            product_qty_df.columns = ["Product", "Quantity"]
            st.dataframe(product_qty_df, use_container_width=True, hide_index=True)
        else:
            st.warning("No data available")
    
    with col_top2:
        st.markdown("### Top 10 Products by Revenue")
        product_rev = filtered_df.groupby("ProductName")["TotalAmount"].sum().sort_values(ascending=False).head(10)
        if not product_rev.empty:
            product_rev_df = product_rev.reset_index()
            product_rev_df.columns = ["Product", "Revenue"]
            product_rev_df["Revenue"] = product_rev_df["Revenue"].apply(lambda x: f"Rs. {x:,.2f}")
            st.dataframe(product_rev_df, use_container_width=True, hide_index=True)
        else:
            st.warning("No data available")
    
    # All products summary
    st.markdown("### Complete Product Summary")
    if not filtered_df.empty:
        product_summary = filtered_df.groupby("ProductName").agg({
            "Quantity": "sum",
            "TotalAmount": "sum",
            "TransactionID": "count"
        }).round(2)
        product_summary.columns = ["Total Quantity", "Total Revenue", "Transactions"]
        product_summary = product_summary.sort_values("Total Revenue", ascending=False)
        
        # Format currency
        product_summary["Total Revenue"] = product_summary["Total Revenue"].apply(lambda x: f"Rs. {x:,.2f}")
        product_summary["Transactions"] = product_summary["Transactions"].apply(lambda x: f"{int(x):,}")
        
        st.dataframe(product_summary, use_container_width=True)

# ============================================================
# TAB 5: CUSTOMER ANALYSIS
# ============================================================
with tab5:
    st.header("Customer Analysis")
    
    # Top customers
    st.markdown("### Top 10 Customers by Total Spend")
    customer_spend = filtered_df.groupby(["CustomerID", "CustomerName"])["TotalAmount"].sum().sort_values(ascending=False).head(10)
    if not customer_spend.empty:
        customer_spend_df = customer_spend.reset_index()
        customer_spend_df.columns = ["Customer ID", "Name", "Total Spend"]
        customer_spend_df["Total Spend"] = customer_spend_df["Total Spend"].apply(lambda x: f"Rs. {x:,.2f}")
        st.dataframe(customer_spend_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No data available")
    
    # Repeat vs One-time
    st.markdown("### Customer Loyalty Analysis")
    transaction_counts = filtered_df.groupby("CustomerID")["TransactionID"].nunique()
    repeat_customers = (transaction_counts > 1).sum()
    one_time_customers = (transaction_counts == 1).sum()
    total_customers = len(transaction_counts)
    repeat_rate = (repeat_customers / total_customers) * 100 if total_customers > 0 else 0
    
    col_cust1, col_cust2, col_cust3 = st.columns(3)
    with col_cust1:
        st.metric("Repeat Customers", f"{repeat_customers:,}")
    with col_cust2:
        st.metric("One-Time Shoppers", f"{one_time_customers:,}")
    with col_cust3:
        st.metric("Repeat Rate", f"{repeat_rate:.1f}%")
    
    st.markdown("---")
    
    # Customer spend distribution
    st.markdown("### Customer Spend Distribution")
    if not filtered_df.empty:
        customer_spend_all = filtered_df.groupby("CustomerID")["TotalAmount"].sum()
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(customer_spend_all, bins=20, color="#3498db", edgecolor='black', linewidth=0.5, alpha=0.8)
        ax.set_xlabel("Total Spend (Rs.)", fontsize=10, color='#555')
        ax.set_ylabel("Number of Customers", fontsize=10, color='#555')
        ax.set_title("Distribution of Customer Total Spend", fontsize=13, fontweight='bold', pad=15)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    else:
        st.warning("No data available")
    
    # Average lifetime value
    avg_ltv = filtered_df["TotalAmount"].sum() / filtered_df["CustomerID"].nunique() if filtered_df["CustomerID"].nunique() > 0 else 0
    st.metric("Average Customer Lifetime Value", f"Rs. {avg_ltv:,.2f}")

# ============================================================
# TAB 6: PAYMENT METHODS
# ============================================================
with tab6:
    st.header("Payment Method Analysis")
    
    # Payment method KPIs
    if not filtered_df.empty:
        payment_summary = filtered_df.groupby("PaymentMethod").agg({
            "TotalAmount": ["sum", "mean", "count"]
        }).round(2)
        payment_summary.columns = ["Total Revenue", "Avg Transaction", "Transactions"]
        payment_summary = payment_summary.sort_values("Total Revenue", ascending=False)
        
        # Format for display
        payment_display = payment_summary.copy()
        payment_display["Total Revenue"] = payment_display["Total Revenue"].apply(lambda x: f"Rs. {x:,.2f}")
        payment_display["Avg Transaction"] = payment_display["Avg Transaction"].apply(lambda x: f"Rs. {x:,.2f}")
        payment_display["Transactions"] = payment_display["Transactions"].apply(lambda x: f"{int(x):,}")
        
        st.dataframe(payment_display, use_container_width=True)
        
        col_pay1, col_pay2 = st.columns(2)
        
        with col_pay1:
            st.markdown("### Revenue by Payment Method")
            fig, ax = plt.subplots(figsize=(8, 5))
            payment_summary["Total Revenue"].plot(kind="bar", ax=ax, color="#9b59b6", edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Revenue (Rs.)", fontsize=10, color='#555')
            ax.set_title("Total Revenue by Payment Method", fontsize=12, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        with col_pay2:
            st.markdown("### Transaction Count by Payment Method")
            fig, ax = plt.subplots(figsize=(8, 5))
            payment_summary["Transactions"].plot(kind="bar", ax=ax, color="#e67e22", edgecolor='black', linewidth=0.5)
            ax.set_ylabel("Number of Transactions", fontsize=10, color='#555')
            ax.set_title("Popularity of Payment Methods", fontsize=12, fontweight='bold', pad=15)
            ax.tick_params(axis='x', rotation=45)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        # Payment by branch heatmap
        st.markdown("### Payment Method Usage by Branch (%)")
        payment_by_branch = pd.crosstab(filtered_df["Branch"], filtered_df["PaymentMethod"], normalize="index") * 100
        payment_by_branch = payment_by_branch.round(1)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(payment_by_branch, annot=True, fmt=".1f", cmap="YlGnBu", ax=ax, 
                    cbar_kws={'label': 'Percentage %'})
        ax.set_title("Payment Method Distribution by Branch (%)", fontsize=13, fontweight='bold', pad=20)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
    else:
        st.warning("No data available")

# ============================================================
# DATA QUALITY SECTION
# ============================================================
st.markdown("---")
with st.expander("📋 Data Quality Report"):
    st.markdown("### Dataset Information")
    
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Original Rows", f"{18_812:,}")
    with col_info2:
        st.metric("Clean Rows", f"{len(df):,}")
    with col_info3:
        st.metric("Duplicates Removed", "724")
    
    col_info4, col_info5, col_info6 = st.columns(3)
    with col_info4:
        st.metric("Missing Values Fixed", "1,546")
    with col_info5:
        st.metric("Columns", f"{len(df.columns)}")
    with col_info6:
        st.metric("Data Quality Score", "99.1%")
    
    st.markdown("---")
    st.markdown("**Data Cleaning Steps Applied:**")
    st.markdown("""
    1. Removed 724 fully duplicate rows
    2. Filled 543 missing CustomerName with "Unknown Customer"
    3. Imputed 371 missing UnitPrice using TotalAmount/Quantity or category median
    4. Filled 468 missing PaymentMethod with "Unknown"
    5. Smart-filled 271 missing ProductCategory using ProductName mapping
    6. Recalculated TotalAmount to ensure consistency
    7. Extracted Date features (Year, Month, Day, DayOfWeek, City)
    """)

# ============================================================
# RAW DATA VIEW
# ============================================================
st.markdown("---")
with st.expander("View Raw Data"):
    st.markdown("### Filtered Sales Data")
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    # Download button
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name=f"bhatbhateni_sales_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; padding: 20px;'>"
    "BSCS Dashboard | Built with Streamlit | Data Source: Bhatbhateni Sales Dataset"
    "</div>",
    unsafe_allow_html=True
)
