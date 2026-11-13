
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Add backend folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'backend')
    )
)

from clustering import perform_clustering

# Page configuration
st.set_page_config(
    page_title="Renewable Energy Clustering",
    page_icon="🌱",
    layout="wide"
)

# Dashboard title
st.title("🌱 Renewable Energy Clustering Analysis")
st.write(
    "Analysis of Solar and Wind Energy using "
    "Apache HBase and K-Means Clustering"
)

st.markdown("---")

# Retrieve clustering results
df = perform_clustering()

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Energy Sources", df['source'].nunique())

with col3:
    st.metric("Clusters Identified", df['cluster'].nunique())

st.markdown("---")

# Dataset display
st.subheader("📊 Renewable Energy Dataset")
st.dataframe(df, use_container_width=True)

# Cluster distribution
st.subheader("📈 Cluster Distribution")

cluster_counts = (
    df['cluster']
    .value_counts()
    .sort_index()
    .reset_index()
)

cluster_counts.columns = ['Cluster', 'Records']

fig = px.bar(
    cluster_counts,
    x='Cluster',
    y='Records',
    color='Cluster',
    title='Number of Records in Each Cluster',
    text='Records'
)

st.plotly_chart(fig, use_container_width=True)

# Energy source distribution
st.subheader("⚡ Energy Source Distribution")

source_counts = df['source'].value_counts().reset_index()
source_counts.columns = ['Energy Source', 'Records']

fig2 = px.pie(
    source_counts,
    names='Energy Source',
    values='Records',
    title='Solar vs Wind Records',
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)

# Energy output comparison
st.subheader("🔋 Energy Output by Source")

fig3 = px.bar(
    df,
    x='source',
    y='energy_output',
    color='source',
    title='Energy Output Comparison',
    labels={
        'source': 'Energy Source',
        'energy_output': 'Energy Output'
    }
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

st.success("Dashboard data loaded successfully from Apache HBase!")
st.caption(
    "Note: This project uses illustrative sample measurements."
)
