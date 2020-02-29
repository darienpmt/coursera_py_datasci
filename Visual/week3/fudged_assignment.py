import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                 np.random.normal(43000,100000,3650),
                 np.random.normal(43500,140000,3650),
                  np.random.normal(48000,70000,3650)],
                 index=[1992,1993,1994,1995])
df

import numpy as np, scipy.stats as st
import matplotlib.pyplot as plt

def mean_confidence_interval(data):
    m= np.mean(data)
    l, u= st.t.interval(0.95, len(data)-1, loc=np.mean(data), scale=st.sem(data))
    return m, l, u

d={}
for i in df.index:
    d[i]=mean_confidence_interval(df.loc[i])

plt.figure(figsize= (10, 8))
cm = plt.cm.get_cmap('RdYlBu_r')
# get the range of the confidence interval
means= [d[i][0] for i in d.keys()]
y_r = [d[i][0] - d[i][2] for i in d.keys()]
y=np.mean(means)
norm_means=means-min(means)
norm_means/=max(norm_means)
plt.axhline(y, label='Y axis value of interest: '+ str(y))
plt.bar(range(len(means)), means, yerr=y_r, align='center', capsize=20, width=1, edgecolor='black', linewidth= 1, color= cm(norm_means))
plt.xticks(range(len(d)), d.keys())

plt.xlabel('Years', fontsize= 14)
plt.title('Custom Bar Plot Visualisation using Colour Gradient (Harder Difficulty)', fontsize=18)
plt.legend(loc=2)
plt.show()

