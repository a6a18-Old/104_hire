#!/usr/bin/env python
# coding: utf-8

# In[81]:


from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
import os

SaveDirectory = os.getcwd()
webdriver_path = SaveDirectory + '\chromedriver.exe'


#https://www.104.com.tw/job/6qtss?jobsource=hotjob_chr
#https://www.104.com.tw/job/6er8p?jobsource=hotjob_chr
#keyword = input("想找的職業：")
driver = webdriver.Chrome(executable_path=webdriver_path) #開啟firefox
#driver.get("https://www.104.com.tw/jobs/search/?keyword=" + keyword + "order=1&jobsource=2018indexpoc&ro=0") #前往這個網址
driver.get("https://www.104.com.tw/job/6er8p?jobsource=hotjob_chr")
sleep(4)
soup = BeautifulSoup(driver.page_source, 'html.parser')


# In[82]:


tool = soup.select("p.mb-5.r3.job-description__content.text-break")
print(tool[0].get_text())

content = tool[0].get_text()


# In[83]:


alist = content.split("\n")


# In[84]:


alist


# In[85]:


import re

ex = []

for item in alist:
    ipath = u"%s"%(item)
    result = re.findall(r'[\u0041-\u007A]+', ipath)
    ex.extend(result)
    #print(result)


# In[86]:


ex


# In[87]:


sss = set(ex)
print(sss)


# In[88]:


dic = {}
for iii in list(sss):
    dic[iii] = ex.count(iii)


# In[89]:


dic


# In[90]:


sorted(dic.items(),key=lambda item:item[1],reverse=True)


# In[ ]:




