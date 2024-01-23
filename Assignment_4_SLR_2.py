#!/usr/bin/env python
# coding: utf-8

# # 2) Salary_hike -> Build a prediction model for Salary_hike

# In[4]:


import pandas as pd
import numpy as np


# In[20]:


salary_data = pd.read_csv(r'C:\Users\poorn\OneDrive\Documents\ExcelR\Asssignment\Assign_4\salary_data.csv')
salary_data


# EDA

# In[21]:


salary_data.head()


# In[22]:


salary_data.shape


# In[23]:


salary_data.info()


# In[24]:


salary_data.describe()


# In[14]:


salary_data.isnull().any().any()


# In[39]:


salary_data=salary_data.rename({'YearsExperience':'Experience'},axis=1)
salary_data


# In[34]:


salary_data.head()


# Data Visualization

# In[53]:


import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf


# In[46]:


sns.displot(salary_data['Salary'])


# In[47]:


sns.displot(salary_data['Experience'])


# In[49]:


sns.lmplot(data = salary_data, x = 'Salary', y = 'Experience', fit_reg = True)


# Correlation

# In[50]:


salary_data.corr()


# MOdel Building

# In[55]:


model= smf.ols("Salary ~ Experience",data = salary_data).fit()


# Model Testing

# In[56]:


model.params


# Finding t and pvalues

# In[57]:


model.tvalues, model.pvalues


# In[ ]:


Finding R square values


# In[59]:


model.rsquared , model.rsquared_adj


# In[ ]:


Let pridict 35 year of experience


# In[64]:


salary_hike= (25792.200199)+( 9449.962321) *(4)
salary


# In[67]:


# Let new data Predict exp 7.5,9.2
new_data=pd.Series([5,9.2])
new_data


# In[69]:


data_pred=pd.DataFrame(new_data,columns=['Experience'])
data_pred


# In[70]:


model.predict(data_pred)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




