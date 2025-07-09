# Walmart Black Friday Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-username/WalmartBlackFriday/main/app.py)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

Statistical analysis of customer purchase behavior during Black Friday to determine if spending habits differ between male and female customers.

## 🎯 Business Problem

Walmart's management team wants to analyze customer purchase behavior (specifically, purchase amount) against customer gender and other factors to make better business decisions. 

📍 [Click here to launch the app](https://walmartblackfriday-umaramanathan.streamlit.app/) 

## The key questions

- **Do women spend more on Black Friday than men?**
- **Are women spending more money per transaction than men? Why or Why not?**
- **Confidence intervals and distribution of the mean of the expenses by female and male customers**
- **Are confidence intervals of average male and female spending overlapping? How can Walmart leverage this conclusion to make changes or improvements?**
- **Results when the same activity is performed for Married vs Unmarried**
- **Results when the same activity is performed for Age**

## 📊 Analysis Features

- **Hypothesis Testing** - Statistical significance testing for gender differences
- **Confidence Intervals** - Reliable estimates with different confidence levels
- **Central Limit Theorem** - Sample size impact on statistical precision
- **Customer Segmentation** - Age, occupation, city category analysis
- **Interactive Dashboard** - Comprehensive Streamlit application

## 🔍 Detailed Research Framework

### Hypothesis Testing
- **Null Hypothesis (H₀)**: No significant difference in spending between male and female customers
- **Alternative Hypothesis (H₁)**: Significant difference in spending between male and female customers
- **Significance Level**: α = 0.05

### Statistical Methods
- **T-Test**: Compare mean spending between genders
- **Confidence Intervals**: 95% and 99% confidence intervals for spending estimates
- **Effect Size**: Cohen's d to measure practical significance
- **Distribution Analysis**: Histograms and box plots for spending distributions

### Business Metrics
- **Average Transaction Value**: By gender, marital status, and age
- **Spending Patterns**: Peak spending times and product categories
- **Customer Segmentation**: High-value customer identification
- **Revenue Optimization**: Targeted marketing strategies
## 📁 Project Structure

```
Walmart Confidence Interval/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Dataset/
│   └── walmart_data.csv  # Black Friday transaction data
├── README.md             # This file
└── venv/                 # Virtual environment
```

## 🔧 Tech Stack

- **Python** - Core programming language
- **Streamlit** - Interactive web application
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Plotly** - Interactive visualizations
- **SciPy** - Statistical analysis
- **Matplotlib/Seaborn** - Data visualization

## 📈 Key Findings

- Statistical evidence for gender-based spending differences
- Central Limit Theorem demonstrates sample size importance
- Age group analysis identifies high-value customer segments
- Geographic variations in Black Friday shopping behavior
- Data-driven recommendations for targeted marketing strategies

## 📋 Dataset Features

| Feature | Description |
|---------|-------------|
| User_ID | Unique customer identifier |
| Product_ID | Product identifier |
| Gender | Customer gender (M/F) |
| Age | Age group categories |
| Occupation | Customer occupation (masked) |
| City_Category | City classification (A/B/C) |
| Marital_Status | Marital status (0/1) |
| ProductCategory | Product category (masked) |
| Purchase | Purchase amount ($) |

## 🎨 Dashboard Sections

1. **Overview** - Dataset information and key metrics
2. **Data Quality** - Null values, outliers, descriptive statistics
3. **Gender Analysis** - Male vs female spending patterns
4. **Age Analysis** - Age group spending behavior
5. **City Analysis** - Geographic spending variations
6. **Occupation Analysis** - Professional segment analysis
7. **Statistical Analysis** - Hypothesis testing, confidence intervals, CLT
8. **Recommendations** - Data-driven business strategies

## 📊 Statistical Methods

- **Independent T-Test** - Gender difference significance testing
- **Confidence Intervals** - Population parameter estimation
- **Central Limit Theorem** - Sample size impact simulation
- **Descriptive Statistics** - Data distribution analysis
- **Outlier Detection** - Data quality assessment

## 💼 Business Impact

- Statistical evidence for gender-targeted marketing
- Customer segment identification for targeted campaigns
- Data-driven inventory optimization strategies
- Interactive dashboard for real-time business intelligence
- Framework for future customer behavior analysis
