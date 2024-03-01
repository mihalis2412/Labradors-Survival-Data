#!/usr/bin/env python
# coding: utf-8

# In[2]:


from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("Labradors.csv")
# Assuming 'df' is your DataFrame containing the 'lifespan' column
kmf = KaplanMeierFitter()
kmf.fit(df['lifespan'], event_observed=df['event'])
# Initialize the figure
fig = go.Figure()

# Add Kaplan-Meier curve
fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.survival_function_.iloc[:, 0], mode='lines', name='Kaplan-Meier Estimate'))

# Find median survival time
median_survival_time = kmf.median_survival_time_

# Add markers for median survival with custom legend label
fig.add_trace(go.Scatter(x=[median_survival_time], y=[0.5], 
                         mode='markers', 
                         marker=dict(color='red', size=13), 
                         name='Median Survival Time'))  # Update legend label

# Round the median survival time to 2 digits
median_survival_time_rounded = round(median_survival_time, 2)

# Add annotations for median survival
fig.add_annotation(x=median_survival_time, y=0.5, text=f'Median Survival: {median_survival_time_rounded} years', arrowhead=2, ax=-150, ay=-0)

# Add confidence intervals
ci_lower = kmf.confidence_interval_.iloc[:, 0]
ci_upper = kmf.confidence_interval_.iloc[:, 1]


fig.add_trace(go.Scatter(x=kmf.timeline, y=ci_lower, mode='lines', line=dict(color='green', width=0), showlegend=False))
fig.add_trace(go.Scatter(x=kmf.timeline, y=ci_upper, mode='lines', fill='tonexty', fillcolor='rgba(0, 255, 0, 0.2)', line=dict(color='green', width=0), name='95% Confidence Interval'))


# Update layout
fig.update_layout(title='Interactive Kaplan-Meier Plot of Labradors',
                  xaxis_title='Years',
                  yaxis_title='Survival Probability',
                  xaxis=dict(range=[0, 20]),  # Extend x-axis limits
                  showlegend=True)

fig.show()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




