import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Walmart Black Friday: Business Story",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for business presentation
st.markdown("""
<style>
    .main-header {
        color: #1f77b4;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    .story-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    
    .key-insight {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .recommendation-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .metric-highlight {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load and preprocess the Walmart dataset"""
    try:
        df = pd.read_csv('Dataset/walmart_data.csv')
        df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})
        return df
    except FileNotFoundError:
        st.error("Dataset not found! Please ensure 'walmart_data.csv' is in the Dataset folder.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">Walmart Black Friday: The Business Story</h1>', unsafe_allow_html=True)
    st.markdown("### A Data-Driven Journey from Customer Insights to Strategic Action")
    
    # Load data
    df = load_data()
    
    if df is None:
        st.info("Please upload the walmart_data.csv file to the Dataset folder to begin the story.")
        return
    
    # Navigation
    st.sidebar.title("Story Chapters")
    
    if st.sidebar.button("📖 Executive Summary", use_container_width=True):
        st.session_state.story_chapter = "Executive Summary"
    
    if st.sidebar.button("🎯 The Business Challenge", use_container_width=True):
        st.session_state.story_chapter = "Business Challenge"
    
    if st.sidebar.button("📊 Key Findings", use_container_width=True):
        st.session_state.story_chapter = "Key Findings"
    
    if st.sidebar.button("🔍 Deep Dive Analysis", use_container_width=True):
        st.session_state.story_chapter = "Deep Dive"
    
    if st.sidebar.button("💡 Strategic Recommendations", use_container_width=True):
        st.session_state.story_chapter = "Recommendations"
    
    if st.sidebar.button("📈 Implementation Roadmap", use_container_width=True):
        st.session_state.story_chapter = "Roadmap"
    
    # Initialize story chapter
    if 'story_chapter' not in st.session_state:
        st.session_state.story_chapter = "Executive Summary"
    
    # Story content based on selection
    if st.session_state.story_chapter == "Executive Summary":
        show_executive_summary(df)
    elif st.session_state.story_chapter == "Business Challenge":
        show_business_challenge(df)
    elif st.session_state.story_chapter == "Key Findings":
        show_key_findings(df)
    elif st.session_state.story_chapter == "Deep Dive":
        show_deep_dive(df)
    elif st.session_state.story_chapter == "Recommendations":
        show_recommendations(df)
    elif st.session_state.story_chapter == "Roadmap":
        show_roadmap(df)

def show_executive_summary(df):
    """Executive summary with key metrics and story overview"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 📖 Executive Summary")
    st.markdown("""
    **The Challenge:** Walmart needed to understand customer spending patterns during Black Friday to optimize marketing strategies and inventory management.
    
    **The Solution:** Comprehensive analysis of 537,577 Black Friday transactions across gender, age, location, and occupation demographics.
    
    **The Impact:** Identified significant spending differences and actionable insights for targeted marketing and inventory optimization.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Transactions", f"{len(df):,}")
    
    with col2:
        st.metric("Total Revenue", f"${df['Purchase'].sum():,.0f}")
    
    with col3:
        st.metric("Avg Purchase", f"${df['Purchase'].mean():.2f}")
    
    with col4:
        st.metric("Unique Customers", f"{df['User_ID'].nunique():,}")
    
    # Gender comparison
    male_avg = df[df['Gender']=='Male']['Purchase'].mean()
    female_avg = df[df['Gender']=='Female']['Purchase'].mean()
    gender_diff = female_avg - male_avg
    
    st.markdown('<div class="key-insight">', unsafe_allow_html=True)
    st.markdown(f"## 🎯 Key Insight: Gender Spending Difference")
    st.markdown(f"**Female customers spend ${gender_diff:.2f} more on average than male customers**")
    st.markdown(f"- Male Average: ${male_avg:.2f}")
    st.markdown(f"- Female Average: ${female_avg:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistical significance
    male_purchases = df[df['Gender']=='Male']['Purchase']
    female_purchases = df[df['Gender']=='Female']['Purchase']
    t_stat, p_value = stats.ttest_ind(male_purchases, female_purchases)
    
    if p_value < 0.05:
        st.success("✅ **Statistically Significant:** This difference is reliable and not due to chance")
    else:
        st.warning("⚠️ **Not Statistically Significant:** The difference may be due to chance")

def show_business_challenge(df):
    """The business problem and context"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 🎯 The Business Challenge")
    st.markdown("""
    **Walmart's Dilemma:**
    
    With 100 million customers (50M male, 50M female), Walmart needed to understand:
    
    - **Do women spend more on Black Friday than men?**
    - **Which customer segments drive the highest revenue?**
    - **How can we optimize inventory and marketing for maximum impact?**
    
    **The Data:**
    - 537,577 Black Friday transactions
    - Customer demographics: Gender, Age, City, Occupation, Marital Status
    - Purchase amounts and product categories
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Data overview visualization
    col1, col2 = st.columns(2)
    
    with col1:
        # Gender distribution
        gender_counts = df['Gender'].value_counts()
        fig = px.pie(values=gender_counts.values, names=gender_counts.index,
                     title="Customer Gender Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Purchase distribution
        fig = px.histogram(df, x='Purchase', nbins=50,
                          title="Purchase Amount Distribution",
                          labels={'Purchase': 'Purchase Amount ($)', 'count': 'Frequency'})
        st.plotly_chart(fig, use_container_width=True)

def show_key_findings(df):
    """Key findings with supporting evidence"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 📊 Key Findings")
    st.markdown("""
    Our analysis revealed several critical insights that can transform Walmart's Black Friday strategy.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Finding 1: Gender Difference
    st.markdown("### 🎯 Finding 1: Significant Gender Spending Difference")
    
    male_avg = df[df['Gender']=='Male']['Purchase'].mean()
    female_avg = df[df['Gender']=='Female']['Purchase'].mean()
    gender_diff = female_avg - male_avg
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **The Numbers:**
        - Female Average: ${female_avg:.2f}
        - Male Average: ${male_avg:.2f}
        - Difference: ${gender_diff:.2f}
        """)
        
        # Statistical test
        male_purchases = df[df['Gender']=='Male']['Purchase']
        female_purchases = df[df['Gender']=='Female']['Purchase']
        t_stat, p_value = stats.ttest_ind(male_purchases, female_purchases)
        
        st.markdown(f"**Statistical Test:** p-value = {p_value:.6f}")
        if p_value < 0.05:
            st.success("✅ **Statistically Significant**")
        else:
            st.warning("⚠️ **Not Statistically Significant**")
    
    with col2:
        # Gender comparison chart
        gender_stats = df.groupby('Gender')['Purchase'].agg(['mean', 'count']).reset_index()
        fig = px.bar(gender_stats, x='Gender', y='mean',
                     title="Average Purchase by Gender",
                     labels={'mean': 'Average Purchase ($)', 'Gender': 'Gender'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Finding 2: Age Analysis
    st.markdown("### 📈 Finding 2: Age-Based Spending Patterns")
    
    age_analysis = df.groupby('Age')['Purchase'].agg(['mean', 'count']).reset_index()
    best_age = age_analysis.loc[age_analysis['mean'].idxmax()]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Top Spending Age Group:**
        - Age Range: {best_age['Age']}
        - Average Spend: ${best_age['mean']:.2f}
        - Customer Count: {best_age['count']:,}
        """)
    
    with col2:
        # Age spending chart
        fig = px.bar(age_analysis, x='Age', y='mean',
                     title="Average Purchase by Age Group",
                     labels={'mean': 'Average Purchase ($)', 'Age': 'Age Group'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Finding 3: City Analysis
    st.markdown("### 🏙️ Finding 3: Geographic Spending Patterns")
    
    city_analysis = df.groupby('City_Category')['Purchase'].agg(['mean', 'count']).reset_index()
    best_city = city_analysis.loc[city_analysis['mean'].idxmax()]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Top Spending City Category:**
        - Category: {best_city['City_Category']}
        - Average Spend: ${best_city['mean']:.2f}
        - Customer Count: {best_city['count']:,}
        """)
    
    with col2:
        # City spending chart
        fig = px.bar(city_analysis, x='City_Category', y='mean',
                     title="Average Purchase by City Category",
                     labels={'mean': 'Average Purchase ($)', 'City_Category': 'City Category'})
        st.plotly_chart(fig, use_container_width=True)

def show_deep_dive(df):
    """Deep dive analysis with advanced insights"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 🔍 Deep Dive Analysis")
    st.markdown("""
    Advanced statistical analysis reveals the reliability and business impact of our findings.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Confidence Intervals
    st.markdown("### 📊 Confidence Intervals: How Reliable Are Our Findings?")
    
    male_purchases = df[df['Gender']=='Male']['Purchase']
    female_purchases = df[df['Gender']=='Female']['Purchase']
    
    male_mean = male_purchases.mean()
    female_mean = female_purchases.mean()
    
    # Calculate 95% confidence intervals
    male_ci = stats.t.interval(0.95, len(male_purchases)-1, 
                              loc=male_mean, scale=stats.sem(male_purchases))
    female_ci = stats.t.interval(0.95, len(female_purchases)-1, 
                                loc=female_mean, scale=stats.sem(female_purchases))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**95% Confidence Intervals:**")
        st.markdown(f"**Male:** (${male_ci[0]:,.2f}, ${male_ci[1]:,.2f})")
        st.markdown(f"**Female:** (${female_ci[0]:,.2f}, ${female_ci[1]:,.2f})")
        
        # Check overlap
        overlap = not (male_ci[1] < female_ci[0] or female_ci[1] < male_ci[0])
        
        if overlap:
            st.warning("⚠️ **Overlapping Intervals:** Cannot conclude significant difference")
        else:
            st.success("✅ **Non-overlapping Intervals:** Significant difference detected")
    
    with col2:
        # Business impact calculation
        total_customers = 100_000_000  # 50M each
        potential_revenue = abs(female_mean - male_mean) * (total_customers / 2)
        
        st.markdown("**Business Impact:**")
        st.markdown(f"**Potential Revenue Impact:** ${potential_revenue:,.0f}")
        st.markdown("**Based on 100M customers (50M each gender)**")
    
    # Marital Status Analysis
    st.markdown("### 💍 Marital Status Impact")
    
    married_purchases = df[df['Marital_Status']==1]['Purchase']
    unmarried_purchases = df[df['Marital_Status']==0]['Purchase']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Marital Status Comparison:**
        - Married Average: ${married_purchases.mean():,.2f}
        - Unmarried Average: ${unmarried_purchases.mean():,.2f}
        - Difference: ${married_purchases.mean() - unmarried_purchases.mean():,.2f}
        """)
    
    with col2:
        # Marital status distribution
        marital_counts = df['Marital_Status'].value_counts()
        fig = px.pie(values=marital_counts.values, names=['Unmarried', 'Married'],
                     title="Marital Status Distribution")
        st.plotly_chart(fig, use_container_width=True)

def show_recommendations(df):
    """Strategic recommendations based on findings"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 💡 Strategic Recommendations")
    st.markdown("""
    Based on our comprehensive analysis, here are actionable strategies for Walmart's Black Friday success.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gender-based recommendations
    male_avg = df[df['Gender']=='Male']['Purchase'].mean()
    female_avg = df[df['Gender']=='Female']['Purchase'].mean()
    
    if female_avg > male_avg:
        st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
        st.markdown("### 🎯 Primary Target: Female Customers")
        st.markdown(f"**Justification:** Women spend ${female_avg - male_avg:.2f} more on average")
        st.markdown("""
        **Strategic Actions:**
        1. **Product Development:** Expand female-focused product categories
        2. **Marketing Campaigns:** Create women-specific Black Friday promotions
        3. **Store Layout:** Position female-preferred products prominently
        4. **Inventory Management:** Increase stock of female-targeted items
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
        st.markdown("### 🎯 Primary Target: Male Customers")
        st.markdown(f"**Justification:** Men spend ${male_avg - female_avg:.2f} more on average")
        st.markdown("""
        **Strategic Actions:**
        1. **Product Development:** Expand male-focused product categories
        2. **Marketing Campaigns:** Create men-specific Black Friday promotions
        3. **Store Layout:** Optimize for male shopping patterns
        4. **Inventory Management:** Increase stock of male-targeted items
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Age-based recommendations
    age_analysis = df.groupby('Age')['Purchase'].agg(['mean', 'count']).reset_index()
    best_age = age_analysis.loc[age_analysis['mean'].idxmax()]
    
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown(f"### 📈 Age-Based Strategy: Target {best_age['Age']} Age Group")
    st.markdown(f"**Justification:** {best_age['Age']} customers spend ${best_age['mean']:.2f} on average")
    st.markdown("""
    **Strategic Actions:**
    1. **Product Development:** Develop products for target age demographic
    2. **Marketing Campaigns:** Create age-appropriate messaging
    3. **Store Experience:** Optimize layout for target age preferences
    4. **Digital Marketing:** Use platforms popular with this demographic
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Revenue optimization
    st.markdown('<div class="recommendation-box">', unsafe_allow_html=True)
    st.markdown("### 💰 Revenue Optimization Strategies")
    st.markdown("""
    **1. Dynamic Pricing:**
    - Implement segment-based pricing based on spending patterns
    - Use customer data to optimize price points
    
    **2. Personalized Marketing:**
    - Develop AI-driven recommendation systems
    - Create targeted email campaigns for each segment
    
    **3. Inventory Management:**
    - Stock products preferred by high-spending demographics
    - Adjust inventory levels based on customer segment preferences
    
    **4. Black Friday Strategy:**
    - Target high-spending segments with exclusive offers
    - Create segment-specific Black Friday campaigns
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def show_roadmap(df):
    """Implementation roadmap and success metrics"""
    st.markdown('<div class="story-section">', unsafe_allow_html=True)
    st.markdown("## 📈 Implementation Roadmap")
    st.markdown("""
    A phased approach to implementing our data-driven recommendations.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Implementation phases
    st.markdown("### 🚀 Phase 1: Immediate Actions (1-3 months)")
    st.markdown("""
    - Implement basic segment-based marketing campaigns
    - Start data collection and analysis processes
    - Develop initial customer segmentation models
    - **Expected Outcome:** 5-10% increase in targeted segment engagement
    """)
    
    st.markdown("### 📊 Phase 2: Short-term Optimization (3-6 months)")
    st.markdown("""
    - Launch personalized product recommendations
    - Implement dynamic pricing strategies
    - Develop targeted loyalty programs
    - **Expected Outcome:** 15-20% increase in revenue from targeted segments
    """)
    
    st.markdown("### 🎯 Phase 3: Full Implementation (6-12 months)")
    st.markdown("""
    - Complete data-driven strategy implementation
    - Advanced analytics and AI integration
    - Full store optimization based on findings
    - **Expected Outcome:** 25-30% improvement in customer retention
    """)
    
    st.markdown("### 🔄 Phase 4: Continuous Optimization (12+ months)")
    st.markdown("""
    - Continuous optimization and refinement
    - Expansion of successful strategies
    - Development of new data-driven initiatives
    - **Expected Outcome:** Sustained competitive advantage
    """)
    
    # Success metrics
    st.markdown("### 📊 Success Metrics & KPIs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Key Performance Indicators:**")
        st.markdown("""
        - Revenue growth by customer segment
        - Customer lifetime value improvement
        - Segment-specific conversion rates
        - Inventory turnover optimization
        - Marketing campaign ROI by segment
        """)
    
    with col2:
        st.markdown("**Expected Outcomes:**")
        st.markdown("""
        - 15-25% increase in revenue from targeted segments
        - 20-30% improvement in customer retention
        - 10-15% reduction in inventory costs
        - 25-35% increase in marketing campaign effectiveness
        """)
    
    # Business impact summary
    total_customers = 100_000_000
    male_avg = df[df['Gender']=='Male']['Purchase'].mean()
    female_avg = df[df['Gender']=='Female']['Purchase'].mean()
    potential_revenue = abs(female_avg - male_avg) * (total_customers / 2)
    
    st.markdown('<div class="metric-highlight">', unsafe_allow_html=True)
    st.markdown("## 💰 Total Business Impact")
    st.markdown(f"**Potential Revenue Impact:** ${potential_revenue:,.0f}")
    st.markdown("**Based on implementing gender-based targeting strategies across 100M customers**")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 