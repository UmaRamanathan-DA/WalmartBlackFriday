import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Walmart Black Friday Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Enhanced theme with gradients and modern styling */
    .main-header {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border: none;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Enhanced dataframes */
    .dataframe {
        border-radius: 0.5rem;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Chart containers */
    .stPlotlyChart {
        border-radius: 0.5rem;
        padding: 1rem;
        background: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Success/Warning/Error messages */
    .stAlert {
        border-radius: 0.5rem;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        border-radius: 0.5rem;
        border: none;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load and preprocess the Walmart dataset"""
    try:
        # Try to load the data
        df = pd.read_csv('Dataset/walmart_data.csv')
        
        # Basic preprocessing
        df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})
        
        # Convert age bins to more readable format
        age_mapping = {
            '0-17': '0-17',
            '18-25': '18-25', 
            '26-35': '26-35',
            '36-45': '36-45',
            '46-50': '46-50',
            '51-55': '51-55',
            '55+': '55+'
        }
        df['Age'] = df['Age'].replace(age_mapping)
        
        return df
    except FileNotFoundError:
        st.error("Dataset not found! Please ensure 'walmart_data.csv' is in the Dataset folder.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">Walmart Black Friday Analysis</h1>', unsafe_allow_html=True)
    st.markdown("### Comprehensive Analysis of Customer Purchase Behavior by Gender and Other Factors")
    
    # Load data
    df = load_data()
    
    if df is None:
        st.info("Please upload the Walmart_data.csv file to the Dataset folder to begin analysis.")
        return
    
    # Sidebar for navigation
    st.sidebar.title("Analysis Sections")
    
    # Navigation links
    st.sidebar.markdown("### Navigation")
    
    # Use session state to track current section
    if 'current_section' not in st.session_state:
        st.session_state.current_section = "Overview"
    
    # Navigation buttons
    if st.sidebar.button("Overview", use_container_width=True):
        st.session_state.current_section = "Overview"
    
    if st.sidebar.button("Data Quality", use_container_width=True):
        st.session_state.current_section = "Data Quality"
    
    if st.sidebar.button("Gender Analysis", use_container_width=True):
        st.session_state.current_section = "Gender Analysis"
    
    if st.sidebar.button("Age Analysis", use_container_width=True):
        st.session_state.current_section = "Age Analysis"
    
    if st.sidebar.button("City Analysis", use_container_width=True):
        st.session_state.current_section = "City Analysis"
    
    if st.sidebar.button("Occupation Analysis", use_container_width=True):
        st.session_state.current_section = "Occupation Analysis"
    
    if st.sidebar.button("Statistical Analysis", use_container_width=True):
        st.session_state.current_section = "Statistical Analysis"
    
    if st.sidebar.button("Recommendations", use_container_width=True):
        st.session_state.current_section = "Recommendations"
    
    # Display basic info
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Dataset Info")
    st.sidebar.write(f"Total Records: {len(df):,}")
    st.sidebar.write(f"Male Customers: {len(df[df['Gender']=='Male']):,}")
    st.sidebar.write(f"Female Customers: {len(df[df['Gender']=='Female']):,}")
    
    # Main content based on selection
    if st.session_state.current_section == "Overview":
        show_overview(df)
    elif st.session_state.current_section == "Data Quality":
        show_data_quality(df)
    elif st.session_state.current_section == "Gender Analysis":
        show_gender_analysis(df)
    elif st.session_state.current_section == "Age Analysis":
        show_age_analysis(df)
    elif st.session_state.current_section == "City Analysis":
        show_city_analysis(df)
    elif st.session_state.current_section == "Occupation Analysis":
        show_occupation_analysis(df)
    elif st.session_state.current_section == "Statistical Analysis":
        show_statistical_analysis(df)
    elif st.session_state.current_section == "Recommendations":
        show_recommendations(df)

def show_data_quality(df):
    """Analyze data quality including null values and outliers"""
    st.header("Data Quality Analysis")
    st.markdown("### Detecting Null Values & Outliers")
    
    # Null values analysis
    with st.expander("Null Values Analysis", expanded=True):
        # Check for null values
        null_counts = df.isnull().sum()
        null_percentages = (null_counts / len(df)) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Null Value Counts")
            null_df = pd.DataFrame({
                'Column': null_counts.index,
                'Null Count': null_counts.values,
                'Null Percentage': null_percentages.values
            })
            st.dataframe(null_df[null_df['Null Count'] > 0] if null_df['Null Count'].sum() > 0 else pd.DataFrame({'Message': ['No null values found!']}))
        
        with col2:
            st.subheader("Null Values Summary")
            total_null = null_counts.sum()
            total_cells = len(df) * len(df.columns)
            null_percentage = (total_null / total_cells) * 100
            
            st.metric("Total Null Values", f"{total_null:,}")
            st.metric("Null Percentage", f"{null_percentage:.2f}%")
            
            if total_null == 0:
                st.success("**Excellent!** No null values detected in the dataset.")
            elif null_percentage < 5:
                st.info("**Good!** Less than 5% null values detected.")
            elif null_percentage < 10:
                st.warning("**Moderate!** 5-10% null values detected.")
            else:
                st.error("**Critical!** More than 10% null values detected.")
    
    # Data types and basic info
    with st.expander("📋 Data Types & Basic Info", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Data Types")
            dtype_df = pd.DataFrame({
                'Column': df.dtypes.index,
                'Data Type': df.dtypes.values
            })
            st.dataframe(dtype_df)
        
        with col2:
            st.subheader("Dataset Shape")
            st.write(f"**Rows:** {df.shape[0]:,}")
            st.write(f"**Columns:** {df.shape[1]}")
            st.write(f"**Memory Usage:** {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    # Descriptive statistics
    with st.expander("Descriptive Statistics", expanded=True):
        st.subheader("Statistical Summary")
        
        # Get descriptive statistics
        desc_stats = df.describe()
        
        # Calculate additional statistics for numerical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        
        if len(numerical_cols) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Basic Statistics:**")
                st.dataframe(desc_stats)
            
            with col2:
                st.write("**Additional Statistics:**")
                additional_stats = pd.DataFrame({
                    'Column': numerical_cols,
                    'Mean': [df[col].mean() for col in numerical_cols],
                    'Median': [df[col].median() for col in numerical_cols],
                    'Mean-Median Diff': [abs(df[col].mean() - df[col].median()) for col in numerical_cols],
                    'Skewness': [df[col].skew() for col in numerical_cols],
                    'Kurtosis': [df[col].kurtosis() for col in numerical_cols]
                })
                st.dataframe(additional_stats.round(4))
                
                # Check for skewness
                st.write("**Skewness Interpretation:**")
                for col in numerical_cols:
                    skew = df[col].skew()
                    if abs(skew) < 0.5:
                        st.write(f"• {col}: Normal distribution (skew = {skew:.3f})")
                    elif abs(skew) < 1:
                        st.write(f"• {col}: Moderately skewed (skew = {skew:.3f})")
                    else:
                        st.write(f"• {col}: Highly skewed (skew = {skew:.3f})")
    
    # Outlier detection
    with st.expander("🔍 Outlier Detection", expanded=True):
        st.subheader("Outlier Analysis")
        
        if len(numerical_cols) > 0:
            # IQR method for outlier detection
            outlier_summary = []
            
            for col in numerical_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
                outlier_count = len(outliers)
                outlier_percentage = (outlier_count / len(df)) * 100
                
                outlier_summary.append({
                    'Column': col,
                    'Q1': Q1,
                    'Q3': Q3,
                    'IQR': IQR,
                    'Lower Bound': lower_bound,
                    'Upper Bound': upper_bound,
                    'Outlier Count': outlier_count,
                    'Outlier Percentage': outlier_percentage
                })
            
            outlier_df = pd.DataFrame(outlier_summary)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Outlier Summary:**")
                st.dataframe(outlier_df.round(4))
            
            with col2:
                st.write("**Outlier Assessment:**")
                for _, row in outlier_df.iterrows():
                    if row['Outlier Percentage'] < 1:
                        st.success(f"{row['Column']}: Low outliers ({row['Outlier Percentage']:.2f}%)")
                    elif row['Outlier Percentage'] < 5:
                        st.warning(f"{row['Column']}: Moderate outliers ({row['Outlier Percentage']:.2f}%)")
                    else:
                        st.error(f"{row['Column']}: High outliers ({row['Outlier Percentage']:.2f}%)")
    
    # Box plots for outlier visualization
    with st.expander("Box Plots for Outlier Visualization", expanded=True):
        st.subheader("Outlier Visualization")
        
        if len(numerical_cols) > 0:
            # Create box plots for each numerical column
            for col in numerical_cols:
                fig = px.box(df, y=col, title=f"Box Plot: {col}")
                st.plotly_chart(fig, use_container_width=True)
    
    # Data quality recommendations
    with st.expander("💡 Data Quality Recommendations", expanded=False):
        st.subheader("🔧 Recommendations")
        
        # Check for issues and provide recommendations
        issues_found = []
        
        # Check for null values
        if df.isnull().sum().sum() > 0:
            issues_found.append("• **Null Values:** Consider imputation or removal strategies")
        
        # Check for outliers
        if len(numerical_cols) > 0:
            high_outlier_cols = []
            for col in numerical_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)][col]
                if len(outliers) / len(df) > 0.05:
                    high_outlier_cols.append(col)
            
            if high_outlier_cols:
                issues_found.append(f"• **Outliers:** High outlier percentage in {', '.join(high_outlier_cols)}")
        
        # Check for data type issues
        if len(df.select_dtypes(include=['object'])) > 0:
            issues_found.append("• **Data Types:** Consider converting object columns to appropriate types")
        
        if issues_found:
            st.warning("**Issues Found:**")
            for issue in issues_found:
                st.write(issue)
        else:
            st.success("**Excellent data quality!** No major issues detected.")
        
        st.write("**General Recommendations:**")
        st.write("• Always validate data before analysis")
        st.write("• Consider outlier treatment based on business context")
        st.write("• Document any data cleaning steps performed")
        st.write("• Monitor data quality in production systems")

def show_overview(df):
    """Display overview of the dataset"""
    st.header("Dataset Overview")
    
    # About Walmart
    with st.expander("About Walmart", expanded=True):
        st.markdown("""
        **About Walmart**
        
        Walmart is an American multinational retail corporation that operates a chain of supercenters, discount departmental stores, and grocery stores from the United States. Walmart has more than 100 million customers worldwide.
        """)
    
    # Business Problem
    with st.expander("Business Problem", expanded=True):
        st.markdown("""
        **Business Problem**
        
        The Management team at Walmart Inc. wants to analyze the customer purchase behavior (specifically, purchase amount) against the customer's gender and the various other factors to help the business make better decisions. They want to understand if the spending habits differ between male and female customers: Do women spend more on Black Friday than men? (Assume 50 million customers are male and 50 million are female).
        """)
    
    # Dataset Information
    with st.expander("Dataset Information", expanded=True):
        st.markdown("""
        **Dataset**
        
        The company collected the transactional data of customers who purchased products from the Walmart Stores during Black Friday. The dataset has the following features:
        
        | Feature | Description |
        |---------|-------------|
        | User_ID | User ID |
        | Product_ID | Product ID |
        | Gender | Sex of User |
        | Age | Age in bins |
        | Occupation | Occupation (Masked) |
        | City_Category | Category of the City (A,B,C) |
        | StayInCurrentCityYears | Number of years stay in current city |
        | Marital_Status | Marital Status |
        | ProductCategory | Product Category (Masked) |
        | Purchase | Purchase Amount |
        """)
    
    # Key metrics
    with st.expander("Key Metrics", expanded=True):
        st.metric("Total Purchase Amount", f"${df['Purchase'].sum():,.0f}")
        st.metric("Average Purchase", f"${df['Purchase'].mean():.2f}")
        st.metric("Total Customers", f"{df['User_ID'].nunique():,}")
        st.metric("Total Products", f"{df['Product_ID'].nunique():,}")
    
    # Data preview
    with st.expander("Data Preview", expanded=False):
        st.dataframe(df.head(10))
    
    # Purchase distribution
    with st.expander("Purchase Distribution Analysis", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.histogram(df, x='Purchase', nbins=50, 
                              title="Purchase Amount Distribution",
                              labels={'Purchase': 'Purchase Amount ($)', 'count': 'Frequency'})
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.box(df, x='Gender', y='Purchase', 
                         title="Purchase Amount by Gender",
                         labels={'Purchase': 'Purchase Amount ($)', 'Gender': 'Gender'})
            st.plotly_chart(fig, use_container_width=True)

def show_gender_analysis(df):
    """Analyze purchase behavior by gender"""
    st.header("Gender Analysis")
    st.markdown("### Do women spend more on Black Friday than men?")
    
    # Gender statistics
    with st.expander("Gender Purchase Statistics", expanded=True):
        gender_stats = df.groupby('Gender')['Purchase'].agg(['mean', 'sum', 'count']).round(2)
        gender_stats.columns = ['Average Purchase ($)', 'Total Purchase ($)', 'Number of Purchases']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(gender_stats)
            
            # Calculate percentage difference
            male_avg = df[df['Gender']=='Male']['Purchase'].mean()
            female_avg = df[df['Gender']=='Female']['Purchase'].mean()
            diff_percent = ((female_avg - male_avg) / male_avg) * 100
            
            st.metric("Gender Difference", f"{diff_percent:.1f}%", 
                     delta="Female vs Male Average")
        
        with col2:
            # Gender distribution pie chart
            gender_counts = df['Gender'].value_counts()
            fig = px.pie(values=gender_counts.values, names=gender_counts.index,
                         title="Gender Distribution")
            st.plotly_chart(fig, use_container_width=True)
    
    # Detailed gender analysis
    with st.expander("Purchase Patterns by Gender", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Purchase amount distribution by gender
            fig = px.histogram(df, x='Purchase', color='Gender', 
                              title="Purchase Distribution by Gender",
                              labels={'Purchase': 'Purchase Amount ($)', 'count': 'Frequency'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Box plot with outliers
            fig = px.box(df, x='Gender', y='Purchase', 
                         title="Purchase Amount Distribution by Gender",
                         labels={'Purchase': 'Purchase Amount ($)', 'Gender': 'Gender'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Gender analysis by other factors
    with st.expander("Gender Analysis by Other Factors", expanded=False):
        # Age and Gender
        age_gender = df.groupby(['Age', 'Gender'])['Purchase'].mean().reset_index()
        fig = px.bar(age_gender, x='Age', y='Purchase', color='Gender',
                     title="Average Purchase by Age and Gender",
                     labels={'Purchase': 'Average Purchase ($)', 'Age': 'Age Group'})
        st.plotly_chart(fig, use_container_width=True)
        
        # City Category and Gender
        city_gender = df.groupby(['City_Category', 'Gender'])['Purchase'].mean().reset_index()
        fig = px.bar(city_gender, x='City_Category', y='Purchase', color='Gender',
                     title="Average Purchase by City Category and Gender",
                     labels={'Purchase': 'Average Purchase ($)', 'City_Category': 'City Category'})
        st.plotly_chart(fig, use_container_width=True)

def show_age_analysis(df):
    """Analyze purchase behavior by age"""
    st.header("Age Analysis")
    
    # Age statistics
    with st.expander("Age Group Purchase Statistics", expanded=True):
        age_stats = df.groupby('Age')['Purchase'].agg(['mean', 'sum', 'count']).round(2)
        age_stats.columns = ['Average Purchase ($)', 'Total Purchase ($)', 'Number of Purchases']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(age_stats)
        
        with col2:
            # Age distribution
            age_counts = df['Age'].value_counts()
            fig = px.pie(values=age_counts.values, names=age_counts.index,
                         title="Age Distribution")
            st.plotly_chart(fig, use_container_width=True)
    
    # Age analysis charts
    with st.expander("Purchase Patterns by Age", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Average purchase by age
            age_avg = df.groupby('Age')['Purchase'].mean().reset_index()
            fig = px.bar(age_avg, x='Age', y='Purchase',
                         title="Average Purchase by Age Group",
                         labels={'Purchase': 'Average Purchase ($)', 'Age': 'Age Group'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Box plot by age
            fig = px.box(df, x='Age', y='Purchase',
                         title="Purchase Distribution by Age Group",
                         labels={'Purchase': 'Purchase Amount ($)', 'Age': 'Age Group'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Age and Gender heatmap
    with st.expander("🔥 Age vs Gender Heatmap", expanded=False):
        age_gender_pivot = df.groupby(['Age', 'Gender'])['Purchase'].mean().unstack()
        fig = px.imshow(age_gender_pivot, 
                         title="Average Purchase Heatmap: Age vs Gender",
                         labels=dict(x="Gender", y="Age Group", color="Average Purchase ($)"))
        st.plotly_chart(fig, use_container_width=True)

def show_city_analysis(df):
    """Analyze purchase behavior by city category"""
    st.header("City Analysis")
    
    # City statistics
    with st.expander("City Category Purchase Statistics", expanded=True):
        city_stats = df.groupby('City_Category')['Purchase'].agg(['mean', 'sum', 'count']).round(2)
        city_stats.columns = ['Average Purchase ($)', 'Total Purchase ($)', 'Number of Purchases']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(city_stats)
        
        with col2:
            # City distribution
            city_counts = df['City_Category'].value_counts()
            fig = px.pie(values=city_counts.values, names=city_counts.index,
                         title="City Category Distribution")
            st.plotly_chart(fig, use_container_width=True)
    
    # City analysis charts
    with st.expander("Purchase Patterns by City", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Average purchase by city
            city_avg = df.groupby('City_Category')['Purchase'].mean().reset_index()
            fig = px.bar(city_avg, x='City_Category', y='Purchase',
                         title="Average Purchase by City Category",
                         labels={'Purchase': 'Average Purchase ($)', 'City_Category': 'City Category'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Box plot by city
            fig = px.box(df, x='City_Category', y='Purchase',
                         title="Purchase Distribution by City Category",
                         labels={'Purchase': 'Purchase Amount ($)', 'City_Category': 'City Category'})
            st.plotly_chart(fig, use_container_width=True)
    
    # City and Gender analysis
    with st.expander("City vs Gender Analysis", expanded=False):
        city_gender_pivot = df.groupby(['City_Category', 'Gender'])['Purchase'].mean().unstack()
        fig = px.bar(city_gender_pivot, 
                      title="Average Purchase by City Category and Gender",
                      labels={'value': 'Average Purchase ($)', 'City_Category': 'City Category'})
        st.plotly_chart(fig, use_container_width=True)

def show_occupation_analysis(df):
    """Analyze purchase behavior by occupation"""
    st.header("Occupation Analysis")
    
    # Top 10 occupations by average purchase
    with st.expander("Top 10 Occupations by Average Purchase", expanded=True):
        occupation_stats = df.groupby('Occupation')['Purchase'].agg(['mean', 'sum', 'count']).round(2)
        occupation_stats.columns = ['Average Purchase ($)', 'Total Purchase ($)', 'Number of Purchases']
        occupation_stats = occupation_stats.sort_values('Average Purchase ($)', ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.dataframe(occupation_stats.head(10))
        
        with col2:
            # Occupation distribution (top 10)
            top_occupations = df['Occupation'].value_counts().head(10)
            fig = px.bar(x=top_occupations.index, y=top_occupations.values,
                         title="Top 10 Occupations by Purchase Count",
                         labels={'x': 'Occupation', 'y': 'Number of Purchases'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Occupation analysis charts
    with st.expander("Purchase Patterns by Occupation", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Average purchase by top occupations
            top_occ_avg = df[df['Occupation'].isin(occupation_stats.head(10).index)].groupby('Occupation')['Purchase'].mean().reset_index()
            fig = px.bar(top_occ_avg, x='Occupation', y='Purchase',
                         title="Average Purchase by Top 10 Occupations",
                         labels={'Purchase': 'Average Purchase ($)', 'Occupation': 'Occupation'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Box plot for top occupations
            top_occ_data = df[df['Occupation'].isin(occupation_stats.head(10).index)]
            fig = px.box(top_occ_data, x='Occupation', y='Purchase',
                         title="Purchase Distribution by Top 10 Occupations",
                         labels={'Purchase': 'Purchase Amount ($)', 'Occupation': 'Occupation'})
            st.plotly_chart(fig, use_container_width=True)

def show_statistical_analysis(df):
    """Comprehensive statistical analysis with hypothesis testing, confidence intervals, CLT, and business insights"""
    st.header("Statistical Analysis")
    st.markdown("### Hypothesis Testing, Confidence Intervals, Central Limit Theorem & Business Insights")
    
    # Hypothesis Testing: Gender Differences
    with st.expander("Hypothesis Testing: Gender Differences in Purchase Behavior", expanded=True):
        st.subheader("Test Methodology")
        st.markdown("""
        **What we're testing:** Whether there's a statistically significant difference in purchase amounts between male and female customers.
        
        **Test Type:** Independent Two-Sample T-Test
        
        **Features being compared:**
        - **Independent Variable:** Gender (Male vs Female)
        - **Dependent Variable:** Purchase Amount (continuous variable)
        - **Sample:** All Black Friday transactions from the dataset
        
        **How the test works:**
        1. **Null Hypothesis (H₀):** μ_male = μ_female (no difference in mean purchase amounts)
        2. **Alternative Hypothesis (H₁):** μ_male ≠ μ_female (there is a difference)
        3. **Significance Level:** α = 0.05 (5% chance of Type I error)
        4. **Test Statistic:** T-statistic comparing the two sample means
        5. **Decision Rule:** Reject H₀ if p-value < 0.05
        """)
        
        # Separate data by gender
        male_purchases = df[df['Gender']=='Male']['Purchase']
        female_purchases = df[df['Gender']=='Female']['Purchase']
        
        # T-test for gender differences
        t_test_result = stats.ttest_ind(male_purchases, female_purchases)
        t_stat = t_test_result[0]
        p_value = t_test_result[1]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Test Results")
            st.write(f"**T-statistic:** {t_stat:.4f}")
            st.write(f"**P-value:** {p_value:.6f}")
            st.write(f"**Significance level:** α = 0.05")
            
            if p_value < 0.05:
                st.success("**Result: Statistically Significant Difference**")
                st.write("**Inference:** We reject the null hypothesis. There is sufficient evidence to conclude that purchase amounts differ significantly between males and females.")
            else:
                st.warning("**Result: No Statistically Significant Difference**")
                st.write("**Inference:** We fail to reject the null hypothesis. There is insufficient evidence to conclude that purchase amounts differ between males and females.")
        
        with col2:
            st.subheader("Descriptive Statistics")
            stats_df = pd.DataFrame({
                'Gender': ['Male', 'Female'],
                'Count': [len(male_purchases), len(female_purchases)],
                'Mean': [male_purchases.mean(), female_purchases.mean()],
                'Std': [male_purchases.std(), female_purchases.std()],
                'Min': [male_purchases.min(), female_purchases.min()],
                'Max': [male_purchases.max(), female_purchases.max()]
            })
            st.dataframe(stats_df.round(2))
    
    # Gender Analysis with Confidence Intervals and CLT Simulation
    with st.expander("Gender Analysis with Confidence Intervals and CLT Simulation", expanded=True):
        st.subheader("Male vs Female Spending Analysis")
        
        # Calculate sample statistics
        male_mean = male_purchases.mean()
        female_mean = female_purchases.mean()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Sample Statistics:**")
            st.write(f"Male Average: ${male_mean:,.2f}")
            st.write(f"Female Average: ${female_mean:,.2f}")
            st.write(f"Difference: ${female_mean - male_mean:,.2f}")
            
            # Calculate confidence intervals for different levels
            confidence_levels = [0.90, 0.95, 0.99]
            
            st.write("**Confidence Intervals:**")
            for conf_level in confidence_levels:
                male_ci = stats.t.interval(conf_level, len(male_purchases)-1, 
                                         loc=male_mean, scale=stats.sem(male_purchases))
                female_ci = stats.t.interval(conf_level, len(female_purchases)-1, 
                                           loc=female_mean, scale=stats.sem(female_purchases))
                
                st.write(f"**{conf_level*100}% CI:**")
                st.write(f"Male: (${male_ci[0]:,.2f}, ${male_ci[1]:,.2f})")
                st.write(f"Female: (${female_ci[0]:,.2f}, ${female_ci[1]:,.2f})")
        
        with col2:
            # Check for overlap in confidence intervals
            male_ci_95 = stats.t.interval(0.95, len(male_purchases)-1, 
                                        loc=male_mean, scale=stats.sem(male_purchases))
            female_ci_95 = stats.t.interval(0.95, len(female_purchases)-1, 
                                          loc=female_mean, scale=stats.sem(female_purchases))
            
            # Check overlap
            overlap = not (male_ci_95[1] < female_ci_95[0] or female_ci_95[1] < male_ci_95[0])
            
            st.write("**95% Confidence Interval Overlap Analysis:**")
            if overlap:
                st.warning("**Overlapping Intervals:** Cannot conclude significant difference")
            else:
                st.success("**Non-overlapping Intervals:** Significant difference detected")
            
            # Business impact calculation
            total_customers = 100_000_000  # 50M each
            potential_revenue = abs(female_mean - male_mean) * (total_customers / 2)
            st.write(f"**Potential Revenue Impact:** ${potential_revenue:,.0f}")
        
        # CLT Visualization
        st.subheader("Central Limit Theorem Simulation")
        sample_sizes = [10, 30, 50, 100, 200, 500]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Male Customer CLT Analysis:**")
            male_means = []
            for n in sample_sizes:
                sample_means = []
                for _ in range(1000):  # 1000 simulations
                    sample = np.random.choice(male_purchases, size=n, replace=True)
                    sample_means.append(sample.mean())
                male_means.append(sample_means)
                st.write(f"Sample size {n}: Mean = ${np.mean(sample_means):,.2f}, Std = ${np.std(sample_means):,.2f}")
        
        with col2:
            st.write("**Female Customer CLT Analysis:**")
            female_means = []
            for n in sample_sizes:
                sample_means = []
                for _ in range(1000):  # 1000 simulations
                    sample = np.random.choice(female_purchases, size=n, replace=True)
                    sample_means.append(sample.mean())
                female_means.append(sample_means)
                st.write(f"Sample size {n}: Mean = ${np.mean(sample_means):,.2f}, Std = ${np.std(sample_means):,.2f}")
        
        # CLT Visualization
        fig = make_subplots(rows=2, cols=3, subplot_titles=[f'Sample Size {n}' for n in sample_sizes])
        
        for i, n in enumerate(sample_sizes):
            row = (i // 3) + 1
            col = (i % 3) + 1
            
            fig.add_trace(
                go.Histogram(x=male_means[i], name=f'Male (n={n})', opacity=0.7),
                row=row, col=col
            )
            
            fig.add_trace(
                go.Histogram(x=female_means[i], name=f'Female (n={n})', opacity=0.7),
                row=row, col=col
            )
        
        fig.update_layout(height=600, title_text="CLT: Distribution of Sample Means")
        st.plotly_chart(fig, use_container_width=True)
    
    # Marital Status Analysis
    with st.expander("Marital Status Analysis", expanded=True):
        st.subheader("Married vs Unmarried Spending Patterns")
        
        # Separate data by marital status
        married_purchases = df[df['Marital_Status']==1]['Purchase']
        unmarried_purchases = df[df['Marital_Status']==0]['Purchase']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Marital Status Statistics:**")
            st.write(f"Married Average: ${married_purchases.mean():,.2f}")
            st.write(f"Unmarried Average: ${unmarried_purchases.mean():,.2f}")
            st.write(f"Difference: ${married_purchases.mean() - unmarried_purchases.mean():,.2f}")
            
            # Confidence intervals
            married_ci = stats.t.interval(0.95, len(married_purchases)-1, 
                                        loc=married_purchases.mean(), 
                                        scale=stats.sem(married_purchases))
            unmarried_ci = stats.t.interval(0.95, len(unmarried_purchases)-1, 
                                          loc=unmarried_purchases.mean(), 
                                          scale=stats.sem(unmarried_purchases))
            
            st.write("**95% Confidence Intervals:**")
            st.write(f"Married: (${married_ci[0]:,.2f}, ${married_ci[1]:,.2f})")
            st.write(f"Unmarried: (${unmarried_ci[0]:,.2f}, ${unmarried_ci[1]:,.2f})")
        
        with col2:
            # Marital status distribution
            marital_counts = df['Marital_Status'].value_counts()
            fig = px.pie(values=marital_counts.values, names=['Unmarried', 'Married'],
                        title="Marital Status Distribution")
            st.plotly_chart(fig, use_container_width=True)
    
    # Age Analysis with Life Stages
    with st.expander("Age Analysis by Life Stages", expanded=True):
        st.subheader("Age Group Analysis with Confidence Intervals")
        
        # Create age bins based on life stages
        age_bins = {
            '0-17': 'Teenagers',
            '18-25': 'Young Adults',
            '26-35': 'Early Career',
            '36-45': 'Mid Career',
            '46-50': 'Established',
            '51-55': 'Senior',
            '55+': 'Mature'
        }
        
        # Analyze each age group
        age_analysis = []
        
        for age_range, life_stage in age_bins.items():
            age_data = df[df['Age'] == age_range]['Purchase']
            if len(age_data) > 0:
                mean_spend = age_data.mean()
                ci_95 = stats.t.interval(0.95, len(age_data)-1, 
                                       loc=mean_spend, scale=stats.sem(age_data))
                
                age_analysis.append({
                    'Age Range': age_range,
                    'Life Stage': life_stage,
                    'Count': len(age_data),
                    'Mean Spend': mean_spend,
                    'CI Lower': ci_95[0],
                    'CI Upper': ci_95[1]
                })
        
        age_df = pd.DataFrame(age_analysis)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Age Group Analysis:**")
            st.dataframe(age_df.round(2))
        
        with col2:
            # Age group spending visualization
            fig = px.bar(age_df, x='Life Stage', y='Mean Spend',
                        title="Average Spending by Life Stage",
                        labels={'Mean Spend': 'Average Purchase ($)', 'Life Stage': 'Life Stage'})
            st.plotly_chart(fig, use_container_width=True)
    
    # Business Recommendations
    with st.expander("Business Recommendations & Action Items", expanded=True):
        st.subheader("Strategic Recommendations for Walmart")
        
        # Gender-based recommendations
        st.write("**Gender-Based Strategies:**")
        if female_purchases.mean() > male_purchases.mean():
            st.success("**Target Female Customers:** Higher spending potential")
            st.write("• Develop female-focused product categories")
            st.write("• Create women-specific marketing campaigns")
            st.write("• Optimize inventory for female preferences")
        else:
            st.info("**Target Male Customers:** Higher spending potential")
            st.write("• Develop male-focused product categories")
            st.write("• Create men-specific marketing campaigns")
            st.write("• Optimize inventory for male preferences")
        
        # Marital status recommendations
        st.write("**Marital Status Strategies:**")
        if married_purchases.mean() > unmarried_purchases.mean():
            st.success("**Target Married Customers:** Higher spending potential")
            st.write("• Family-oriented product bundles")
            st.write("• Household-focused promotions")
            st.write("• Family shopping events")
        else:
            st.info("**Target Unmarried Customers:** Higher spending potential")
            st.write("• Individual-focused products")
            st.write("• Lifestyle-oriented marketing")
            st.write("• Personal shopping experiences")
        
        # Age-based recommendations
        st.write("**Age-Based Strategies:**")
        best_age_group = age_df.loc[age_df['Mean Spend'].idxmax()]
        st.success(f"**Target {best_age_group['Life Stage']} (${best_age_group['Mean Spend']:,.2f} avg):**")
        st.write(f"• Develop products for {best_age_group['Life Stage'].lower()} demographic")
        st.write(f"• Create marketing campaigns targeting {best_age_group['Age Range']} age group")
        st.write(f"• Optimize store layout for {best_age_group['Life Stage'].lower()} preferences")
        
        # Revenue optimization
        st.write("**Revenue Optimization:**")
        st.write("• Implement dynamic pricing based on customer segments")
        st.write("• Develop personalized product recommendations")
        st.write("• Create targeted loyalty programs")
        st.write("• Optimize Black Friday strategies for high-spending segments")
        
        # Inventory management
        st.write("**Inventory Management:**")
        st.write("• Stock products preferred by high-spending demographics")
        st.write("• Adjust inventory levels based on customer segment preferences")
        st.write("• Develop category-specific strategies")
        
        # Marketing strategies
        st.write("**Marketing Strategies:**")
        st.write("• Segment-based email marketing campaigns")
        st.write("• Personalized promotional offers")
        st.write("• Social media targeting by demographic")
        st.write("• Influencer partnerships for specific segments")

def show_recommendations(df):
    """Display comprehensive recommendations based on analysis findings."""
    st.header("Recommendations")
    st.markdown("### Strategic Recommendations for Walmart Based on Data Analysis")
    
    # Gender-based recommendations
    with st.expander("Gender-Based Strategies", expanded=True):
        st.subheader("Target Customer Segmentation by Gender")
        
        male_avg = df[df['Gender']=='Male']['Purchase'].mean()
        female_avg = df[df['Gender']=='Female']['Purchase'].mean()
        
        if female_avg > male_avg:
            st.success("**Primary Target: Female Customers**")
            st.write(f"**Justification:** Women spend ${female_avg - male_avg:.2f} more on average than men")
            
            st.write("**Strategic Actions:**")
            st.write("1. **Product Development:** Expand female-focused product categories")
            st.write("   - Increase inventory of products preferred by women")
            st.write("   - Develop exclusive female-oriented product lines")
            st.write("   - Partner with female-focused brands")
            
            st.write("2. **Marketing Campaigns:** Create women-specific marketing strategies")
            st.write("   - Develop targeted email campaigns for female customers")
            st.write("   - Create social media content appealing to women")
            st.write("   - Design Black Friday promotions specifically for female shoppers")
            
            st.write("3. **Store Layout Optimization:**")
            st.write("   - Position female-preferred products prominently")
            st.write("   - Create dedicated sections for women's products")
            st.write("   - Optimize store navigation for female shopping patterns")
        else:
            st.info("**Primary Target: Male Customers**")
            st.write(f"**Justification:** Men spend ${male_avg - female_avg:.2f} more on average than women")
            
            st.write("**Strategic Actions:**")
            st.write("1. **Product Development:** Expand male-focused product categories")
            st.write("2. **Marketing Campaigns:** Create men-specific marketing strategies")
            st.write("3. **Store Layout Optimization:** Optimize for male shopping patterns")
    
    # Marital status recommendations
    with st.expander("Marital Status Strategies", expanded=True):
        st.subheader("Family vs Individual Customer Targeting")
        
        married_avg = df[df['Marital_Status']==1]['Purchase'].mean()
        unmarried_avg = df[df['Marital_Status']==0]['Purchase'].mean()
        
        if married_avg > unmarried_avg:
            st.success("**Primary Target: Married Customers**")
            st.write(f"**Justification:** Married customers spend ${married_avg - unmarried_avg:.2f} more on average")
            
            st.write("**Strategic Actions:**")
            st.write("1. **Family-Oriented Product Bundles:**")
            st.write("   - Create family package deals")
            st.write("   - Develop household essentials bundles")
            st.write("   - Offer family discount programs")
            
            st.write("2. **Household-Focused Promotions:**")
            st.write("   - Target promotions for family needs")
            st.write("   - Create family shopping events")
            st.write("   - Develop loyalty programs for families")
            
            st.write("3. **Store Experience:**")
            st.write("   - Design family-friendly store layouts")
            st.write("   - Provide family shopping assistance")
            st.write("   - Create family-oriented shopping experiences")
        else:
            st.info("**Primary Target: Unmarried Customers**")
            st.write(f"**Justification:** Unmarried customers spend ${unmarried_avg - married_avg:.2f} more on average")
            
            st.write("**Strategic Actions:**")
            st.write("1. **Individual-Focused Products:**")
            st.write("   - Develop single-person household products")
            st.write("   - Create lifestyle-oriented product lines")
            st.write("   - Offer individual-focused promotions")
            
            st.write("2. **Lifestyle Marketing:**")
            st.write("   - Create campaigns targeting individual lifestyles")
            st.write("   - Develop personal shopping experiences")
            st.write("   - Focus on convenience and efficiency")
    
    # Age-based recommendations
    with st.expander("Age-Based Strategies", expanded=True):
        st.subheader("Life Stage Customer Targeting")
        
        age_analysis = df.groupby('Age')['Purchase'].agg(['mean', 'count']).reset_index()
        best_age = age_analysis.loc[age_analysis['mean'].idxmax()]
        
        st.success(f"**Primary Target: {best_age['Age']} Age Group**")
        st.write(f"**Justification:** {best_age['Age']} customers spend ${best_age['mean']:.2f} on average with {best_age['count']:,} customers")
        
        st.write("**Strategic Actions:**")
        st.write("1. **Product Development for Target Age Group:**")
        st.write(f"   - Develop products specifically for {best_age['Age']} demographic")
        st.write("   - Create age-appropriate product categories")
        st.write("   - Design products that appeal to this life stage")
        
        st.write("2. **Marketing Campaigns:**")
        st.write(f"   - Create targeted campaigns for {best_age['Age']} age group")
        st.write("   - Develop age-appropriate messaging")
        st.write("   - Use platforms popular with this demographic")
        
        st.write("3. **Store Experience:**")
        st.write(f"   - Optimize store layout for {best_age['Age']} preferences")
        st.write("   - Train staff to understand this demographic")
        st.write("   - Create age-appropriate shopping experiences")
    
    # Revenue optimization
    with st.expander("Revenue Optimization Strategies", expanded=True):
        st.subheader("Maximizing Revenue Through Data-Driven Decisions")
        
        st.write("**1. Dynamic Pricing Strategy:**")
        st.write("   - Implement segment-based pricing based on spending patterns")
        st.write("   - Use customer data to optimize price points")
        st.write("   - Create personalized pricing for high-value customers")
        
        st.write("**2. Personalized Product Recommendations:**")
        st.write("   - Develop AI-driven recommendation systems")
        st.write("   - Use purchase history for targeted suggestions")
        st.write("   - Create personalized shopping experiences")
        
        st.write("**3. Targeted Loyalty Programs:**")
        st.write("   - Design segment-specific loyalty rewards")
        st.write("   - Create tiered membership programs")
        st.write("   - Offer personalized incentives based on spending")
        
        st.write("**4. Black Friday Strategy Optimization:**")
        st.write("   - Target high-spending segments with exclusive offers")
        st.write("   - Create segment-specific Black Friday campaigns")
        st.write("   - Optimize inventory for predicted demand by segment")
    
    # Inventory management
    with st.expander("Inventory Management Recommendations", expanded=True):
        st.subheader("Data-Driven Inventory Optimization")
        
        st.write("**1. Segment-Based Inventory Planning:**")
        st.write("   - Stock products preferred by high-spending demographics")
        st.write("   - Adjust inventory levels based on customer segment preferences")
        st.write("   - Use predictive analytics for demand forecasting")
        
        st.write("**2. Category-Specific Strategies:**")
        st.write("   - Analyze product category performance by segment")
        st.write("   - Optimize category mix based on segment preferences")
        st.write("   - Develop category-specific marketing strategies")
        
        st.write("**3. Seasonal Inventory Optimization:**")
        st.write("   - Plan inventory based on seasonal segment behavior")
        st.write("   - Adjust stock levels for peak shopping periods")
        st.write("   - Use historical data for demand prediction")
    
    # Marketing strategies
    with st.expander("Marketing Strategy Recommendations", expanded=True):
        st.subheader("Data-Driven Marketing Approaches")
        
        st.write("**1. Segment-Based Email Marketing:**")
        st.write("   - Create personalized email campaigns for each segment")
        st.write("   - Use behavioral data for targeted messaging")
        st.write("   - Develop segment-specific promotional offers")
        
        st.write("**2. Social Media Targeting:**")
        st.write("   - Use demographic data for social media campaigns")
        st.write("   - Create platform-specific content for each segment")
        st.write("   - Develop influencer partnerships for target demographics")
        
        st.write("**3. Personalized Promotional Offers:**")
        st.write("   - Design offers based on segment spending patterns")
        st.write("   - Create time-sensitive promotions for high-value segments")
        st.write("   - Develop loyalty incentives for repeat customers")
        
        st.write("**4. Cross-Channel Marketing:**")
        st.write("   - Integrate online and offline marketing efforts")
        st.write("   - Create consistent messaging across all channels")
        st.write("   - Use data to optimize channel mix for each segment")
    
    # Implementation roadmap
    with st.expander("Implementation Roadmap", expanded=False):
        st.subheader("Strategic Implementation Plan")
        
        st.write("**Phase 1 (Immediate - 1-3 months):**")
        st.write("   - Implement basic segment-based marketing campaigns")
        st.write("   - Start data collection and analysis processes")
        st.write("   - Develop initial customer segmentation models")
        
        st.write("**Phase 2 (Short-term - 3-6 months):**")
        st.write("   - Launch personalized product recommendations")
        st.write("   - Implement dynamic pricing strategies")
        st.write("   - Develop targeted loyalty programs")
        
        st.write("**Phase 3 (Medium-term - 6-12 months):**")
        st.write("   - Full implementation of data-driven strategies")
        st.write("   - Advanced analytics and AI integration")
        st.write("   - Complete store optimization based on findings")
        
        st.write("**Phase 4 (Long-term - 12+ months):**")
        st.write("   - Continuous optimization and refinement")
        st.write("   - Expansion of successful strategies")
        st.write("   - Development of new data-driven initiatives")
    
    # Success metrics
    with st.expander("Success Metrics and KPIs", expanded=False):
        st.subheader("Measuring the Impact of Recommendations")
        
        st.write("**Key Performance Indicators:**")
        st.write("   - Revenue growth by customer segment")
        st.write("   - Customer lifetime value improvement")
        st.write("   - Segment-specific conversion rates")
        st.write("   - Inventory turnover optimization")
        st.write("   - Marketing campaign ROI by segment")
        
        st.write("**Expected Outcomes:**")
        st.write("   - 15-25% increase in revenue from targeted segments")
        st.write("   - 20-30% improvement in customer retention")
        st.write("   - 10-15% reduction in inventory costs")
        st.write("   - 25-35% increase in marketing campaign effectiveness")

if __name__ == "__main__":
    main() 