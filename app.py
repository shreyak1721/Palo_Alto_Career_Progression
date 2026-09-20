import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Career Progression & Retention Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("Final_Employee_Career_KPI_Dataset.csv")

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Career Progression & Promotion Gap Analysis")

st.markdown(
    """
    **Palo Alto Networks HR Analytics**

    This dashboard analyzes employee career progression, promotion gaps,
    role stagnation, training needs, manager stability, and retention
    opportunities using employee career data.
    """
)

st.info(
    "Note: Promotion Gap Risk and Retention Opportunity are "
    "project-defined analytical indicators based on career progression "
    "features. They are not validated predictive or causal models."
)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

# Department
department_options = ["All"] + sorted(
    df["Department"].unique().tolist()
)

selected_department = st.sidebar.selectbox(
    "Department",
    department_options
)

# Job Role
job_role_options = ["All"] + sorted(
    df["JobRole"].unique().tolist()
)

selected_job_role = st.sidebar.selectbox(
    "Job Role",
    job_role_options
)

# Career Stage
career_stage_options = ["All"] + sorted(
    df["CareerStage"].unique().tolist()
)

selected_career_stage = st.sidebar.selectbox(
    "Career Stage",
    career_stage_options
)

# Promotion Gap Risk
risk_options = ["All", "Low", "Medium", "High"]

selected_risk = st.sidebar.selectbox(
    "Promotion Gap Risk",
    risk_options
)

# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()

if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

if selected_job_role != "All":
    filtered_df = filtered_df[
        filtered_df["JobRole"] == selected_job_role
    ]

if selected_career_stage != "All":
    filtered_df = filtered_df[
        filtered_df["CareerStage"] == selected_career_stage
    ]

if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["PromotionGapRisk"] == selected_risk
    ]

st.sidebar.write(
    f"Showing **{len(filtered_df)}** employees"
)

# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_employees = len(filtered_df)

if total_employees > 0:

    attrition_rate = (
        (filtered_df["Attrition"] == 1).mean() * 100
    )

    high_promotion_risk = (
        filtered_df["PromotionGapRisk"] == "High"
    ).sum()

    high_retention_opportunities = (
        filtered_df["RetentionOpportunity"] == "High"
    ).sum()

    training_needs = (
        filtered_df["TrainingNeedIndicator"] == "Needs Development"
    ).sum()

else:

    attrition_rate = 0
    high_promotion_risk = 0
    high_retention_opportunities = 0
    training_needs = 0

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

st.subheader("📌 Key Project Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Employees",
        total_employees
    )

with col2:
    st.metric(
        "Historical Attrition",
        f"{attrition_rate:.1f}%"
    )

with col3:
    st.metric(
        "High Promotion Gap Risk",
        high_promotion_risk
    )

with col4:
    st.metric(
        "High Retention Opportunities",
        high_retention_opportunities
    )

with col5:
    st.metric(
        "Training Needs",
        training_needs
    )

# --------------------------------------------------
# EMPLOYEE DATA
# --------------------------------------------------

st.subheader("👥 Employee Career KPI Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# --------------------------------------------------
# CAREER CLUSTER DISTRIBUTION
# --------------------------------------------------

st.subheader("📊 Career Cluster Distribution")

cluster_counts = (
    filtered_df["CareerCluster"]
    .value_counts()
    .sort_index()
    .reset_index()
)

cluster_counts.columns = ["CareerCluster", "Employees"]

fig_cluster = px.bar(
    cluster_counts,
    x="CareerCluster",
    y="Employees",
    title="Employees by Career Cluster",
    labels={
        "CareerCluster": "Career Cluster",
        "Employees": "Number of Employees"
    },
    text="Employees"
)

fig_cluster.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_cluster,
    use_container_width=True,
    key="career_cluster_chart"
)


# --------------------------------------------------
# PROMOTION GAP RISK DISTRIBUTION
# --------------------------------------------------

st.subheader("⚠️ Promotion Gap Risk Distribution")

risk_order = ["Low", "Medium", "High"]

risk_counts = (
    filtered_df["PromotionGapRisk"]
    .value_counts()
    .reindex(risk_order, fill_value=0)
    .reset_index()
)

risk_counts.columns = ["PromotionGapRisk", "Employees"]

fig_risk = px.bar(
    risk_counts,
    x="PromotionGapRisk",
    y="Employees",
    title="Employees by Promotion Gap Risk",
    labels={
        "PromotionGapRisk": "Promotion Gap Risk",
        "Employees": "Number of Employees"
    },
    text="Employees"
)

fig_risk.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True,
    key="promotion_gap_risk_chart"
)


# --------------------------------------------------
# ATTRITION RATE BY CAREER CLUSTER
# --------------------------------------------------

st.subheader("📉 Historical Attrition Rate by Career Cluster")

cluster_attrition = (
    filtered_df.groupby("CareerCluster")["Attrition"]
    .mean()
    .mul(100)
    .round(2)
    .reset_index()
)

cluster_attrition.columns = [
    "CareerCluster",
    "HistoricalAttritionRate"
]

fig_attrition = px.bar(
    cluster_attrition,
    x="CareerCluster",
    y="HistoricalAttritionRate",
    title="Historical Attrition Rate by Career Cluster",
    labels={
        "CareerCluster": "Career Cluster",
        "HistoricalAttritionRate": "Historical Attrition Rate (%)"
    },
    text="HistoricalAttritionRate"
)

fig_attrition.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

st.plotly_chart(
    fig_attrition,
    use_container_width=True,
    key="attrition_cluster_chart"
)


# --------------------------------------------------
# HIGH RETENTION OPPORTUNITIES BY DEPARTMENT
# --------------------------------------------------

st.subheader("🎯 High Retention Opportunities by Department")

retention_department = (
    filtered_df[
        filtered_df["RetentionOpportunity"] == "High"
    ]["Department"]
    .value_counts()
    .reset_index()
)

retention_department.columns = [
    "Department",
    "HighRetentionOpportunities"
]

fig_retention = px.bar(
    retention_department,
    x="Department",
    y="HighRetentionOpportunities",
    title="High Retention Opportunities by Department",
    labels={
        "Department": "Department",
        "HighRetentionOpportunities": "Number of Employees"
    },
    text="HighRetentionOpportunities"
)

fig_retention.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_retention,
    use_container_width=True,
    key="retention_department_chart"
)


# --------------------------------------------------
# TRAINING NEEDS BY DEPARTMENT
# --------------------------------------------------

st.subheader("📚 Training Needs by Department")

training_department = (
    filtered_df[
        filtered_df["TrainingNeedIndicator"] == "Needs Development"
    ]["Department"]
    .value_counts()
    .reset_index()
)

training_department.columns = [
    "Department",
    "EmployeesNeedingDevelopment"
]

fig_training = px.bar(
    training_department,
    x="Department",
    y="EmployeesNeedingDevelopment",
    title="Employees Needing Development by Department",
    labels={
        "Department": "Department",
        "EmployeesNeedingDevelopment": "Employees Needing Development"
    },
    text="EmployeesNeedingDevelopment"
)

fig_training.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_training,
    use_container_width=True,
    key="training_department_chart"
)


# --------------------------------------------------
# MANAGER STABILITY VS PROMOTION GAP RISK
# --------------------------------------------------

st.subheader("👨‍💼 Manager Stability vs Promotion Gap Risk")

manager_risk = (
    filtered_df.groupby("ManagerStability")["PromotionGapRiskScore"]
    .mean()
    .reindex(["Lower Stability", "Higher Stability"])
    .reset_index()
)

manager_risk.columns = [
    "ManagerStability",
    "AveragePromotionGapRisk"
]

fig_manager = px.bar(
    manager_risk,
    x="ManagerStability",
    y="AveragePromotionGapRisk",
    title="Average Promotion Gap Risk by Manager Stability",
    labels={
        "ManagerStability": "Manager Stability",
        "AveragePromotionGapRisk": "Average Promotion Gap Risk Score"
    },
    text="AveragePromotionGapRisk"
)

fig_manager.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig_manager,
    use_container_width=True,
    key="manager_stability_chart"
)

# --------------------------------------------------
# CAREER CLUSTER PROFILE
# --------------------------------------------------

st.subheader("🔥 Career Cluster Profile")

cluster_features = [
    "PromotionGapRatio",
    "RoleStagnationIndex",
    "TrainingIntensityScore",
    "ManagerStabilityIndicator",
    "CareerVelocityScore"
]

cluster_profile = (
    filtered_df.groupby("CareerCluster")[cluster_features]
    .mean()
    .round(2)
)

fig_heatmap = px.imshow(
    cluster_profile,
    text_auto=".2f",
    aspect="auto",
    title="Career Cluster Profile",
    labels={
        "x": "Career Progression Feature",
        "y": "Career Cluster",
        "color": "Average Value"
    }
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True,
    key="career_cluster_heatmap"
)

# --------------------------------------------------
# RETENTION OPPORTUNITY BY CAREER STAGE
# --------------------------------------------------

st.subheader("📈 High Retention Opportunities by Career Stage")

career_stage_data = (
    filtered_df[filtered_df["RetentionOpportunity"] == "High"]
    .groupby("CareerStage")
    .size()
    .reset_index(name="Employees")
)

fig_career_stage = px.bar(
    career_stage_data,
    x="CareerStage",
    y="Employees",
    title="High Retention Opportunities by Career Stage",
    labels={
        "CareerStage": "Career Stage",
        "Employees": "Number of Employees"
    },
    text="Employees"
)

fig_career_stage.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig_career_stage,
    use_container_width=True,
    key="retention_career_stage_chart"
)

# --------------------------------------------------
# MANAGEMENT INSIGHTS
# --------------------------------------------------

st.subheader("📊 Management Insights")

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    high_gap = (filtered_df["PromotionGapRisk"] == "High").sum()
    st.metric(
        "Employees with High Promotion Gap Risk",
        high_gap
    )

with insight_col2:
    high_retention = (
        filtered_df["RetentionOpportunity"] == "High"
    ).sum()
    st.metric(
        "High Retention Opportunities",
        high_retention
    )

with insight_col3:
    training_needs = (
        filtered_df["TrainingNeedIndicator"] == "Needs Development"
    ).sum()
    st.metric(
        "Employees Needing Development",
        training_needs
    )

st.markdown("---")

st.write(
    """
    **Management Focus Areas**

    • Monitor employees with high promotion gap risk for possible career stagnation.

    • Identify high retention opportunity employees for proactive career development.

    • Review training needs to support skill development and career progression.

    • Use manager stability indicators to understand differences in employee career experiences.
    """
)