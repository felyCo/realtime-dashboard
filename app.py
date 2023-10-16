import streamlit as st        # Web development
import numpy as np            # Numpy mean, np random
import pandas as pd           # Read CSV, df  manipulation
import time                   # Simulate a real time data, time loop
import plotly.express as px   # Interactive charts

# Read CSV from github repository
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

# This is a more static file, we could use dynamic data such as http://api.coindesk.com/v1/bpi/currentprice.json


st.set_page_config(
    page_title = 'Real-Time Dashboard',
    page_icon= '🌍',
    layout = 'wide'
)


st.title('Real-Time/Live Data Stream Dashboard')

# Top Level Filters
job_filter = st.selectbox("Select the job", pd.unique(df['job']))

# Creating a single element container
placeholder = st.empty()

df = df[df['job'] == job_filter]


# Near real time/live feed simulation

for seconds in range(200):
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))
    
    avg_age = np.mean(df['age_new'])
    
    count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,5)))
    
    
    balance = np.mean(df['balance_new'])
    
    
    with placeholder.container():
        # Create Three Columns
        kpi1, kpi2, kpi3 = st.columns(3)
        
        # Fill Three Coulmns with respective metrics or KPIs
        kpi1.metric(label = "Age 📌", value = round(avg_age), delta = round(avg_age) - 10)
        kpi2.metric(label = "Married Count 📌", value = int(count_married), delta = - 10 + count_married)
        kpi3.metric(label = "A/C Balance $", value = f"$ {round(balance,2)}", delta = - round(balance / count_married) * avg_age)
        
        # Create columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig1 = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
            st.write(fig1)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x = 'age_new')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(0.5)
            
        
        
        