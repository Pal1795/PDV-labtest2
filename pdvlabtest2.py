
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
from pandas import DataFrame


# In[8]:

df=pd.read_csv("oil_reserves.csv")
df


# In[123]:

import pandas as pd
import numpy as np
milk=pd.read_csv('milk_production.csv')
milk


# In[124]:

milk[['Cow Milk-2013-14','Boffalo Milk-2013-14','Goat Milk-2013-14']].sum()


# In[125]:

milk[milk['Cow Milk-2013-14']==milk['Cow Milk-2013-14'].max()]['State/ UT Name'] #cowmilk


# In[126]:

milk[milk['Boffalo Milk-2013-14']==milk['Boffalo Milk-2013-14'].max()][['State/ UT Name']] #buffalomilk


# In[127]:

milk[milk['Goat Milk-2013-14']==milk['Goat Milk-2013-14'].max()][['State/ UT Name']] #goat milk


# In[128]:

milk=pd.read_csv('milk_production.csv')
milk.head()


# In[129]:

milk["TOTAL"]=np.sum(milk.iloc[:,1:],axis=1)
milk.head()


# In[130]:

milk.sort_values('TOTAL',ascending='FALSE').max()


# In[131]:

milk["COWMILK"]=np.sum(milk.iloc[:,2:7],axis=1)       #cowmilk
milk


# In[132]:

milk["BUFFALOMILK"]=np.sum(milk.iloc[:,7:12],axis=1)  #buffalomilk
milk.head(5)


# In[133]:

milk["GOATMILK"]=np.sum(milk.iloc[:,8:],axis=1) #goatmilk
milk.head(5)


# # FIRST QUESTION

# In[134]:

milk["maxmilk2013_14"] = milk["Cow Milk-2013-14"] + milk["Boffalo Milk-2013-14"] + milk["Goat Milk-2013-14"]
milk


# In[135]:

milk[milk["maxmilk2013_14"]==milk["maxmilk2013_14"].max()]["State/ UT Name"]


# # second

# In[136]:


milk["year2011"]=milk["Cow Milk-2010-11"] + milk["Boffalo Milk-2010-11"] + milk["Goat Milk-2010-11"]
milk.head(5)


# In[137]:

milk["year2012"]=milk["Cow Milk-2011-12"] + milk["Boffalo Milk-2011-12"] + milk["Goat Milk-2011-12"]
milk


# In[138]:

milk["year2014"]=milk["Cow Milk-2013-14"] + milk["Boffalo Milk-2013-14"] + milk["Goat Milk-2013-14"]
milk


# In[139]:

milk["year2015"]=milk["Cow Milk-2014-15"] + milk["Boffalo Milk-2014-15"] + milk["Goat Milk-2014-15"]
milk


# In[140]:

milk["year2016"]=milk["Cow Milk-2015-16"] + milk["Boffalo Milk-2015-16"] + milk["Goat Milk-2015-16"]
milk


# In[141]:

milk["year2011"]=milk["Cow Milk-2010-11"] + milk["Boffalo Milk-2010-11"] + milk["Goat Milk-2010-11"]
print("Top 5 cities of 2011")
print("\n")
print(milk.sort_values("year2011",ascending=False)["State/ UT Name"].head())


# # fourth 

# In[142]:

milk[milk["year2016"].ge(milk["year2015"]) & milk["year2015"].ge(milk["year2014"])].head() 


# 
# # line chart

# In[158]:

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('milk_production.csv', index_col = False)
data['State/ UT Name'='Karnataka']
plt.plot(data[''], data['Cow Milk-2010-11'], linestyle="dotted", marker='^', color="red")

plt.plot(data['Karnataka'], data['Cow Milk-2011-12'], linestyle="solid", marker='o', color="green")

plt.plot(data['Karnataka'], data['Cow Milk-2013-14'], linestyle="dashed", marker='<', color="blue")
plt.xlabel("year")
plt.ylabel("Milk Production")

# add legend
plt.legend()
plt.title("Milk Analysis")
plt.show()


# # pie chart

# In[157]:


cow = [milk.get_value(0,"Cow Milk-2011-12"),milk.get_value(0,"Cow Milk-2013-14"),milk.get_value(0,"Cow Milk-2014-15"),milk.get_value(0,"Cow Milk-2015-16")]
buffalo = [milk.get_value(0,"Boffalo Milk-2011-12"),milk.get_value(0,"Boffalo Milk-2013-14"),milk.get_value(0,"Boffalo Milk-2014-15"),milk.get_value(0,"Boffalo Milk-2015-16")]
goat =[milk.get_value(0,"Goat Milk-2011-12"),milk.get_value(0,"Goat Milk-2013-14"),milk.get_value(0,"Goat Milk-2014-15"),milk.get_value(0,"Goat Milk-2015-16")]

fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(wspace = 0.5, hspace = 0.3)

axes[0,0].pie(cow,labels=[2012,2014,2015,2016],autopct='%1.1f%%')
axes[0,0].set_title("cow production")

axes[0,1].pie(buffalo,labels=[2012,2014,2015,2016],autopct='%1.1f%%')
axes[0,1].set_title("Buffalo production")

axes[1,0].pie(goat,labels=[2012,2014,2015,2016],autopct='%1.1f%%')
axes[1,0].set_title("Goat production")
plt.show()
print(buffalo)


# In[ ]:



