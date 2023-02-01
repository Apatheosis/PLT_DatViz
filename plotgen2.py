import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import openpyxl as pyx
import pandas as pd

data = "/Users/lennardnicolaisen/Documents/Python/Projects/DatViz_York/parlgov_edited.xlsx"

pd_form_data = pd.read_excel(data,sheet_name='cabinet_means',index_col="cabinet_id",engine='openpyxl')

df = pd.DataFrame(pd_form_data)

cnt_row_vals_dict = {
    'cyp':df.loc[1:3],
    'esp':df.loc[4:9],
    'fr':df.loc[10:13],
    'grc':df.loc[14:17],
    'hrv':df.loc[18:21],
    'ita':df.loc[22:28],
    'mlt':df.loc[29:31],
    'pt':df.loc[32:25],
    'svn':df.loc[36:40]
    }

cnt_dict = {
    "cyp":"o",
    "esp":"v",
    "fra":"2",
    "grc":"8",
    "hrv":"s",
    "ita":"p",
    "mlt":"P",
    "pt":"*",
    "svn":"h"
    }

#fig = plt.figure()
#ax = plt.subplot()

'''for i in df['Country'].items():
    if i[1] == 'CYP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:blue',label=i[1])
    elif i[1] == 'ESP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:orange',label=i[1])
    elif i[1] == 'FRA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:green',label=i[1])
    elif i[1] == 'GRC':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:red',label=i[1])
    elif i[1] == 'HRV':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:purple',label=i[1])
    elif i[1] == 'ITA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:brown',label=i[1])
    elif i[1] == 'MLT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:pink',label=i[1])
    elif i[1] == 'PT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:olive',label=i[1])
    elif i[1] == 'SVN':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plt.scatter(x,y,marker=f'${i[1]}$',s=200,c='tab:cyan',label=i[1])'''

fig, ax = plt.subplots(1,3,figsize=(9,3))

#fig state-market
for i in df['Country'].items():
    if i[1] == 'CYP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot1 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:blue',label=i[1])
    
    elif i[1] == 'ESP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot2 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:orange',label=i[1])
    
    elif i[1] == 'FRA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot3 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:green',label=i[1])
    
    elif i[1] == 'GRC':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot4 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:red',label=i[1])
    
    elif i[1] == 'HRV':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot5 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:purple',label=i[1])
    
    elif i[1] == 'ITA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot6 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:brown',label=i[1])
    
    elif i[1] == 'MLT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot7 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:pink',label=i[1])
    
    elif i[1] == 'PT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot8 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:olive',label=i[1])
    
    elif i[1] == 'SVN':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet state_market'].loc[i[0]]
        plot9 = ax[0].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:cyan',label=i[1])

ax[0].axis([1,9,1,9])
handles = []

ax[0].legend(handles=[plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9])
ax[0].axline(
    (5,0.0),
    (5,9),
    c='0',
    linewidth=1
)
ax[0].axline(
    (0,5),
    (9,5),
    c='0',
    linewidth=1
)
ax[0].set_xlabel("Left - Right")
ax[0].set_ylabel("State - Market")

#fig liberty-authority


for i in df['Country'].items():
    if i[1] == 'CYP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot1 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:blue',label=i[1])
    
    elif i[1] == 'ESP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot2 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:orange',label=i[1])
    
    elif i[1] == 'FRA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot3 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:green',label=i[1])
    
    elif i[1] == 'GRC':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot4 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:red',label=i[1])
    
    elif i[1] == 'HRV':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot5 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:purple',label=i[1])
    
    elif i[1] == 'ITA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot6 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:brown',label=i[1])
    
    elif i[1] == 'MLT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot7 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:pink',label=i[1])
    
    elif i[1] == 'PT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot8 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:olive',label=i[1])
    
    elif i[1] == 'SVN':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet liberty_authority'].loc[i[0]]
        plot9 = ax[1].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:cyan',label=i[1])

ax[1].axis([1,9,1,9])
handles = []

ax[1].legend(handles=[plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9])
ax[1].axline(
    (5,0.0),
    (5,9),
    c='0',
    linewidth=1
)
ax[1].axline(
    (0,5),
    (9,5),
    c='0',
    linewidth=1
)
ax[1].set_xlabel("Left - Right")
ax[1].set_ylabel("Liberty - Authority")

#fig eu anti-pro
for i in df['Country'].items():
    if i[1] == 'CYP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot1 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:blue',label=i[1])
    
    elif i[1] == 'ESP':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot2 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:orange',label=i[1])
    
    elif i[1] == 'FRA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot3 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:green',label=i[1])
    
    elif i[1] == 'GRC':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot4 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:red',label=i[1])
    
    elif i[1] == 'HRV':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot5 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:purple',label=i[1])
    
    elif i[1] == 'ITA':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot6 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:brown',label=i[1])
    
    elif i[1] == 'MLT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot7 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:pink',label=i[1])
    
    elif i[1] == 'PT':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot8 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:olive',label=i[1])
    
    elif i[1] == 'SVN':
        x = df['mean cabinet left_right'].loc[i[0]]
        y = df['mean cabinet eu_anti_pro'].loc[i[0]]
        plot9 = ax[2].scatter(x,y,marker=cnt_dict[str(i[1]).lower()],s=20,c='tab:cyan',label=i[1])

ax[2].axis([1,9,1,9])
handles = []

ax[2].legend(handles=[plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9])
ax[2].axline(
    (5,0.0),
    (5,9),
    c='0',
    linewidth=1
)
ax[2].axline(
    (0,5),
    (9,5),
    c='0',
    linewidth=1
)
ax[2].set_xlabel("Left - Right")
ax[2].set_ylabel("EU: Anti - Pro")

plt.show()