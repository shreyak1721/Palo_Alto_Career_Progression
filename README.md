# Career Progression & Promotion Gap Analysis

## Palo Alto Networks HR Analytics

A data analytics and machine learning project focused on analyzing employee career progression, promotion gaps, role stagnation, training needs, manager stability, and retention opportunities.

The project combines exploratory data analysis, feature engineering, clustering, and an interactive Streamlit dashboard to provide a structured view of employee career progression patterns.

---

## Project Objective

The objective of this project is to analyze employee career progression and identify patterns that may indicate:

- Promotion gaps
- Role stagnation
- Training and development needs
- Managerial stability patterns
- Potential retention opportunities

The project goes beyond traditional attrition analysis by examining employee career trajectories and progression-related indicators.

---

## Dataset

The dataset contains **1,470 employee records** with HR and career-related attributes such as:

- Age
- Attrition
- Department
- Job Role
- Job Level
- Years at Company
- Years in Current Role
- Years Since Last Promotion
- Years With Current Manager
- Training Times Last Year
- Performance Rating
- Job Satisfaction
- Monthly Income
- Percent Salary Hike
- Work-Life Balance
- and other employee attributes

---

## Feature Engineering

The following career progression features were created:

### Promotion Gap Ratio

`Years Since Last Promotion / Years At Company`

Measures promotion delay relative to an employee's company tenure.

### Role Stagnation Index

`Years In Current Role / Years At Company`

Measures the proportion of company tenure spent in the current role.

### Training Intensity Score

`Training Times Last Year / Years At Company`

Measures training exposure relative to company tenure.

### Manager Stability Indicator

`Years With Current Manager / Years At Company`

Measures the proportion of company tenure associated with the current manager.

### Career Velocity Score

`Job Level / Total Working Years`

Provides an analytical indicator of career progression relative to overall experience.

### Career Stage

Employees were categorized into:

- Early Career
- Growth Stage
- Mid Career
- Senior Career

---

## Exploratory Data Analysis

The analysis includes:

- Attrition distribution
- Years Since Last Promotion
- Years In Current Role
- Promotion Gap Ratio
- Department-wise promotion gap analysis
- Promotion Gap Ratio vs historical attrition
- Role Stagnation by Job Role
- Correlation analysis of career progression features

---

## Career Clustering

K-Means clustering was used to identify employee career progression patterns.

The clustering model uses numerical career-related features including:

- Promotion Gap Ratio
- Role Stagnation Index
- Training Intensity Score
- Manager Stability Indicator
- Career Velocity Score
- Years at Company
- Years in Current Role
- Years Since Last Promotion
- Years With Current Manager

`Attrition` was excluded from the clustering features to avoid target leakage.

A working solution of **4 career clusters** was selected using the elbow method and cluster interpretability.

### Cluster Distribution

| Cluster | Employees |
|---|---:|
| Cluster 0 | 728 |
| Cluster 1 | 209 |
| Cluster 2 | 294 |
| Cluster 3 | 239 |

---

## Hierarchical Clustering

Agglomerative Hierarchical Clustering using Ward linkage was also performed with four clusters.

The hierarchical clustering results were compared with the K-Means assignments to provide an additional validation perspective.

---

## Promotion Gap Risk

A project-defined Promotion Gap Risk Score was developed using:

- 60% Promotion Gap Ratio
- 40% Role Stagnation Index

Employees were categorized into:

- Low
- Medium
- High

Promotion Gap Risk.

This is a **project-defined analytical indicator**, not a validated predictive model.

---

## Retention Opportunity

A Retention Opportunity Index was developed using:

- Promotion Gap Risk
- Role Stagnation
- Training Intensity

Employees were categorized into Low, Medium, and High retention opportunity groups.

Historical employees with `Attrition = No`, High Promotion Gap Risk, and High Retention Opportunity were examined as potential retention opportunities.

This is a retrospective analytical segmentation and should not be interpreted as a prediction of future employee behavior.

---

## Training & Manager Stability Analysis

The project also analyzes:

- Training development needs
- Manager stability indicators
- Career progression patterns across departments
- Career progression patterns across career stages

These indicators are intended to support further HR analysis and investigation.

---

## Key Project Metrics

| Metric | Value |
|---|---:|
| Total Employees | 1,470 |
| Historical Attrition | 16.1% |
| Career Clusters | 4 |
| High Promotion Gap Risk | 462 |
| High Retention Opportunities | 485 |
| Employees Needing Development | 713 |

---

## Streamlit Dashboard

An interactive Streamlit dashboard was developed to explore the results.

The project includes an interactive Streamlit dashboard for exploring career
progression patterns, promotion gaps, retention opportunities, training needs,
and managerial stability.

### Dashboard Preview

![Streamlit Dashboard](dashboard_screenshot.png)

### Filters

- Department
- Job Role
- Career Stage
- Promotion Gap Risk

### KPI Cards

- Total Employees
- Historical Attrition
- High Promotion Gap Risk
- High Retention Opportunities
- Training Needs

### Visualizations

- Career Cluster Distribution
- Promotion Gap Risk Distribution
- Historical Attrition Rate by Career Cluster
- High Retention Opportunities by Department
- Training Needs by Department
- Manager Stability vs Promotion Gap Risk
- Career Cluster Profile Heatmap
- High Retention Opportunities by Career Stage
- Management Insights

---

## Technology Stack

**Programming:** Python

**Data Analysis:** Pandas, NumPy

**Visualization:** Matplotlib, Seaborn, Plotly

**Machine Learning:** Scikit-learn

**Dashboard:** Streamlit

**Development:** Google Colab, Visual Studio Code

---

## Project Workflow

```text
HR Dataset
    ↓
Data Quality Checks
    ↓
Feature Engineering
    ↓
Exploratory Data Analysis
    ↓
Feature Selection & Scaling
    ↓
K-Means Clustering
    ↓
Cluster Profiling
    ↓
Hierarchical Clustering Validation
    ↓
Promotion Gap Risk Analysis
    ↓
Retention Opportunity Analysis
    ↓
Training & Manager Stability Analysis
    ↓
KPI Dataset
    ↓
Streamlit Dashboard
