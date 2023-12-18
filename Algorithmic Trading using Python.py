#!/usr/bin/env python
# coding: utf-8

# Algorithmic Trading is the use of algorithms in the financial market to make trading decisions. JP Morgan Chase & Co. is one of the businesses that use Algorithmic Trading for investment decisions. So, if you want to learn how to implement an algorithmic trading strategy,

# In[1]:


import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import yfinance as yf

#get apple stock data from yahoo finance
stock =yf.Ticker("AAPL")
data =stock.history(period ="1y")
print(data.head())


# In[2]:


# now lets implement the momentum strategy in algorithic Trading using python
#calaulation of momentum
data["momentum"]=data["Close"].pct_change()
print(data["momentum"])


# In[5]:


#create subplots to shows momentum and buying/selling markets
fig =make_subplots(rows =2,cols =1)
fig.add_trace(go.Scatter(x=data.index,y=data["Close"],name="Close Price"))
fig.add_trace(go.Scatter(x=data.index,y=data["momentum"],name="Momentum",yaxis="y2"))

#adding the buy and sell signals
fig.add_trace(go.Scatter(x=data.loc[data['momentum']>0].index,
                       y =data.loc[data["momentum"]<0]["Close"],mode="markers",name="Buy",
                       marker =dict(color="red",symbol="triangle-up")))

fig.add_trace(go.Scatter(x=data.loc[data['momentum']>0].index,
                       y =data.loc[data["momentum"]<0]["Close"],mode="markers",name="Sell",
                       marker =dict(color="green",symbol="triangle-down")))
fig.update_layout(title="ALgorithmic Trading using Momentum ",xaxis_title="Date",yaxis_title="Price")
fig.update_yaxes(title ="momentum",secondary_y=True)
fig.show()


# In[ ]:




