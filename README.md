# Walmart Black Friday Analysis

Statistical analysis of customer purchase behavior during Black Friday to determine if spending habits differ between male and female customers.

## 🎯 Business Problem

Walmart's management team wants to analyze customer purchase behavior (specifically, purchase amount) against customer gender and other factors to make better business decisions. 

## The key questions

**Do women spend more on Black Friday than men?**
**Are women spending more money per transaction than men? Why or Why not?**
**Confidence intervals and distribution of the mean of the expenses by female and male customers**
**Are confidence intervals of average male and female spending overlapping? How can Walmart leverage this conclusion to make changes or improvements?**
**Results when the same activity is performed for Married vs Unmarried**
**Results when the same activity is performed for Age**

## 📊 Analysis Features

- **Hypothesis Testing** - Statistical significance testing for gender differences
- **Confidence Intervals** - Reliable estimates with different confidence levels
- **Central Limit Theorem** - Sample size impact on statistical precision
- **Customer Segmentation** - Age, occupation, city category analysis
- **Interactive Dashboard** - Comprehensive Streamlit application

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/walmart-confidence-interval.git
   cd walmart-confidence-interval
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - Local: http://localhost:8501
   - Network: http://your-ip:8501

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
