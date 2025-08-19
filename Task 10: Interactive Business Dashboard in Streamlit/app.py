import streamlit as st
import pandas as pd

# For plotting
import matplotlib.pyplot as plt

# Step 1: Load, clean, and prepare the dataset
@st.cache_data  # Cache so dataset is not loaded every time on interaction
def load_data():
    # Load the CSV file (assume it's uploaded to Colab or provide the path)
    df = pd.read_csv('Global_Superstore.csv', encoding='ISO-8859-1')  # Encoding to handle special characters
    
    # Convert 'Order Date' to datetime for time-based analysis
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    
    # Additional cleaning steps:
    # 1. Check and handle missing values
    # Global Superstore often has missing Postal Codes, fill with 'Unknown'
    df['Postal Code'] = df['Postal Code'].fillna('Unknown')
    # Check for other missing values (display in app if needed, but for now, assume minimal)
    if df.isnull().any().any():
        st.warning("Dataset had some missing values, handled where possible.")
    
    # 2. Remove duplicates if any (based on Order ID, which should be unique)
    df = df.drop_duplicates(subset=['Order ID'])
    
    # 3. Handle invalid data: e.g., negative Sales might be errors, but in this dataset, negative Profit is common (losses)
    # For simplicity, remove rows with negative Sales (if any, rare)
    df = df[df['Sales'] >= 0]
    
    # 4. Standardize strings: Trim whitespace in categorical columns
    categorical_cols = ['Region', 'Category', 'Sub-Category', 'Segment', 'Customer Name']
    for col in categorical_cols:
        df[col] = df[col].str.strip()
    
    # 5. Round numerical columns for better display
    df['Sales'] = df['Sales'].round(2)
    df['Profit'] = df['Profit'].round(2)
    
    return df

df = load_data()

# Step 2: Sidebar filters (added Segment filter for segment-wise analysis)
st.sidebar.header("Filters")

# Unique values for filters
regions = df['Region'].unique().tolist()
categories = df['Category'].unique().tolist()
sub_categories = df['Sub-Category'].unique().tolist()
segments = df['Segment'].unique().tolist()  # New: Add Segment options (Consumer, Corporate, Home Office)

# Filter widgets (multiselect with default to all for full view)
selected_region = st.sidebar.multiselect("Select Region", options=regions, default=regions)
selected_category = st.sidebar.multiselect("Select Category", options=categories, default=categories)
selected_subcategory = st.sidebar.multiselect("Select Sub-Category", options=sub_categories, default=sub_categories)
selected_segment = st.sidebar.multiselect("Select Segment", options=segments, default=segments)  # New: Segment filter

# Step 3: Apply filters on the dataframe (added Segment filter)
filtered_df = df[
    (df['Region'].isin(selected_region)) &
    (df['Category'].isin(selected_category)) &
    (df['Sub-Category'].isin(selected_subcategory)) &
    (df['Segment'].isin(selected_segment))  # New: Include Segment in filtering
]

# Step 4: KPIs Calculation (same as before, but now filtered by Segment too)
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

# Top 5 customers by sales
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

# New: Segment-wise calculations for performance analysis
sales_by_segment = filtered_df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
profit_by_segment = filtered_df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)

# Step 5: Display KPIs (using metrics and charts as per instructions)
st.title("🌍 Global Superstore Business Dashboard")
st.markdown("### Key Performance Indicators (KPIs)")

# Display Total Sales and Total Profit as metrics (enhanced with charts below)
col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

# New: Chart for Total Sales breakdown (e.g., by Category) to make it "using charts"
st.markdown("### Sales Breakdown by Category (Chart for Total Sales KPI)")
sales_by_category = filtered_df.groupby('Category')['Sales'].sum()
st.bar_chart(sales_by_category)
st.markdown("**Insight:** This chart shows how sales are distributed across categories, helping identify top performers.")

# New: Chart for Total Profit breakdown (e.g., by Category)
st.markdown("### Profit Breakdown by Category (Chart for Total Profit KPI)")
profit_by_category = filtered_df.groupby('Category')['Profit'].sum()
st.bar_chart(profit_by_category)
st.markdown("**Insight:** Notice if any category is driving losses (negative profit).")

# Display Top 5 Customers by Sales (already a chart)
st.markdown("### Top 5 Customers by Sales")
st.bar_chart(top_customers)
st.markdown("**Insight:** Focus marketing efforts on these high-value customers.")

# Step 6: Segment-wise performance charts (new section for objective)
st.markdown("### Segment-Wise Performance Analysis")
col3, col4 = st.columns(2)

# Sales by Segment chart
col3.markdown("#### Sales by Segment")
col3.bar_chart(sales_by_segment)
col3.markdown("**Insight:** Consumer segment often leads in sales volume.")

# Profit by Segment chart
col4.markdown("#### Profit by Segment")
col4.bar_chart(profit_by_segment)
col4.markdown("**Insight:** Check if Corporate segment yields higher margins.")

# Optional: Sales trend over time (monthly) - kept as is, good for storytelling
st.markdown("### Sales Trend Over Time")
sales_by_month = filtered_df.resample('M', on='Order Date')['Sales'].sum()
plt.figure(figsize=(10, 4))
plt.plot(sales_by_month.index, sales_by_month.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
st.pyplot(plt)
st.markdown("**Insight:** Look for seasonal patterns or growth trends.")
