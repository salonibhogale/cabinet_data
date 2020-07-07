"""
unique_values_for_name = set(cabinet_csv_file.name)
print(unique_values_for_name)
unique_values_for_state = set(cabinet_csv_file.state)
print(unique_values_for_state)
#  Punjab and Punajb,

unique_values_for_constituency = set(cabinet_csv_file.constituency)
print(unique_values_for_constituency)
unique_values_for_house = set(cabinet_csv_file.house)
print(unique_values_for_house)
# nan for house

unique_values_for_party = set(cabinet_csv_file.party)
print(unique_values_for_party)
# SAMATA PARTY and Samata Party(some parties are in lowercase while others are in uppercase
unique_values_for_gender = set(cabinet_csv_file.gender)
print(unique_values_for_gender)
unique_values_for_ls_number = set(cabinet_csv_file.ls_number)
print(unique_values_for_ls_number)


# nan for ls number

# fixing errors

# fix errors 1
cabinet_csv_file.loc[cabinet_csv_file['state']=='Punajb','state']='Punjab'
# cabinet_csv_file.loc[cabinet_csv_file['id']=="1001",'state']='abcd'
# fix errors 2

cabinet_csv_file['party']= cabinet_csv_file['party'].str.upper()
cabinet_csv_file['state']= cabinet_csv_file['state'].str.upper()

# Tasks for 03/06
# 1. fix all alphabetic columns to upper case
# 2. Fix Party Names
# SAMATA PARTY = SMP
# Lok Jan Shakti Party = LJSP
# Akali Dal = AD
# Janata (S) - J (S)
# BANGLA CONG - BC
# Remove all spaces in 'party' column
# replace all spaces in party column - ' ' to '' --> Google

for col in cabinet_csv_file.columns:
    if col in ['name','gender','party','department','rank','rank_comment','house','constituency','state']:
        cabinet_csv_file.rename(columns={col: col.upper()}, inplace=True)

#cabinet_csv_file.groupby('state').count()
"""


"""
# cleaning column ls_number
print(unique_values_for_ls_number)
#cleaning column for NAME
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['NAME']) == True, 'NAME'] = 'NOT_AVAILABLE'
cabinet_csv_file.loc[cabinet_csv_file['NAME']=='N/a','NAME']='NOT_AVAILABLE'
#cleaning column for GENDER
print(unique_values_for_gender)
#cleaning column for PARTY
print(updated_unique_values_for_party)
bool_series_party = pd.isnull(cabinet_csv_file['PARTY'])
print(cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['PARTY'])])
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['PARTY']) == True, 'PARTY'] = 'NOT_APPLICABLE'
cabinet_csv_file.loc[cabinet_csv_file['PARTY']=='N/a','PARTY']='NOT_APPLICABLE'
"""


"""
all_names = list(set(education_df.NAME))
all_years = [x for x in education_df.list_of_years]
all_years = list(set(','.join(all_years).split(',')))
all_years.remove('')
all_years = [int(x) for x in all_years]
all_years.sort()

count_rs = {}
count_ls = {}
count_none = {}

# assigning a dictionary - data type
# for eg - d = {a1[0]:1, a1[1]:2}

# assign all values of dictionary to 0

for i in range(0, len(all_years)):
    count_rs[all_years[i]]=0
    count_ls[all_years[i]]=0
    count_none[all_years[i]]=0
"""

"""
for i in range(0, len(all_names)):
    df_subset = education_df[education_df['NAME'] == all_na mes[i]]
    ls_rows = df_subset[df_subset['HOUSE']=='Lok Sabha']
    rs_rows = df_subset[df_subset['HOUSE']=='Rajya Sabha']
    none_rows = df_subset[df_subset['HOUSE']=='not_applicable']
    for j in range(0, len(ls_rows)):
        year_split = split_years(ls_rows, j)
        for x in year_split:
            count_ls[x]+=1
    for j in range(0, len(rs_rows)):
        year_split = split_years(rs_rows, j)
        for x in year_split:
            count_rs[x]+=1
    for j in range(0, len(none_rows)):
        year_split = split_years(none_rows, j)
        for x in year_split:
            count_none[x]+=1




# plot out the dictionary

# first create the complete df
complete_df1 = pd.DataFrame()
complete_df1['years'] = pd.Series(list(count_ls.keys())).values
complete_df1['count'] = pd.Series(list(count_ls.values())).values
complete_df1['house'] = 'Lok Sabha'


complete_df2 = pd.DataFrame()
complete_df2['years'] = pd.Series(list(count_rs.keys())).values
complete_df2['count'] = pd.Series(list(count_rs.values())).values
complete_df2['house'] = 'Rajya Sabha'

complete_df3 = pd.DataFrame()
complete_df3['years'] = pd.Series(list(count_none.keys())).values
complete_df3['count'] = pd.Series(list(count_none.values())).values
complete_df3['house'] = 'Not Applicable'

all_dfs = [complete_df1, complete_df2, complete_df3]
all_dfs_combined = pd.concat(all_dfs)




fig = px.bar(all_dfs_combined, x='years', y='count',
             color='house',
             labels={'count':'Number of MPs'}, height=400)
fig.show()
fig1 = px.line(all_dfs_combined, x="years", y="count", color='house')
fig1.show()
#creating the stacked area chart

"""


"""


print(set(cabinet_csv_file['rank']))
# fixing spelling mistakes in ministry_name
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='cabinet secreteriat','ministry_name']='cabinet secretariat'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='law, justice, & company affairs','ministry_name']='law, justice & company affairs'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='law, justice & company affairs ','ministry_name']='law, justice & company affairs'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='earth sciences ', 'ministry_name']='earth sciences'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='personnel & training, pensions, administrative reformos & public grievances', 'ministry_name']='personnel & training, pension, administrative reforms & public grievances'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='personnel, personal grievances & pensions','ministry_name']='personnel, personal grievances, & pension'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='personnel & training, administrative reforms & public grievances & pension','ministry_name']= 'personnel & training, pension, administrative reforms & public grievances'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='personnel, public grievances & pensions','ministry_name']='personnel, public grievances & pension'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='consumer affairs, food & public distribution', 'ministry_name']='food, consumer affairs, public distribution'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']==' labour, employment & rehabilitation', 'ministry_name']='labour, employment & rehabilitation'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='commerce & civil supplies & cooperation', 'ministry_name']='commerce, civil supplies & cooperation'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='steel, mines & coal ', 'ministry_name']='steel, mines & coal'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=="Prime Minister's Office", 'ministry_name']="prime minister's office"
cabinet_csv_file.loc[cabinet_csv_file['ministry_category']=='personnel, public grievances & pension', 'ministry_category']= "personnel, public/private grievances & pension"
cabinet_csv_file.loc[cabinet_csv_file['ministry_category2']=='personnel, public grievances & pension', 'ministry_category2']= "personnel, public/private grievances & pension"

"""


"""
for i in range(0,len(all_names)):
    df_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == all_names[i]]
    m_rows= df_subset[df_subset['GENDER']=='M']
    f_rows= df_subset[df_subset['GENDER']=='F']
    m_rows_PM = df_subset[(df_subset['GENDER']=='M') & (df_subset['RANK']=='PM')]
    f_rows_PM = df_subset[(df_subset['GENDER']=='F') & (df_subset['RANK']=='PM')]
    m_rows_DCM = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'DCM')]
    m_rows_DPM = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'DPM')]
    m_rows_CM = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'CM')]
    m_rows_Other = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'Other')]
    m_rows_MoS = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'MoS')]
    m_rows_DM = df_subset[(df_subset['GENDER'] == 'M') & (df_subset['RANK'] == 'DM')]
    f_rows_DCM = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'DCM')]
    f_rows_DPM = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'DPM')]
    f_rows_CM = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'CM')]
    f_rows_Other = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'Other')]
    f_rows_MoS = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'MoS')]
    f_rows_DM = df_subset[(df_subset['GENDER'] == 'F') & (df_subset['RANK'] == 'DM')]
    year_split_f=[]
    year_split_m=[]
    year_split_m_pm = []
    year_split_f_pm = []
    year_split_m_cm = []
    year_split_f_cm = []
    year_split_m_dcm = []
    year_split_f_dpm = []
    year_split_m_dpm = []
    year_split_f_dcm = []
    year_split_m_other = []
    year_split_f_other = []
    year_split_m_mos = []
    year_split_f_mos = []
    year_split_m_dm = []
    year_split_f_dm = []
    year_split_m_cm = []
    year_split_f_cm = []
    for j in range(0, len(m_rows)):
        year_split_m = year_split_m + split_years(m_rows, j)
    year_split_m = list(set(year_split_m))
    for x in year_split_m:
        count_male[x]+=1
    for j in range(0, len(f_rows)):
        year_split_f = year_split_f + split_years(f_rows, j)
    year_split_f = list(set(year_split_f))
    for x in year_split_f:
        count_female[x]+=1

    for j in range(0, len(m_rows_PM)):
        year_split_m_pm = year_split_m_pm + split_years(m_rows_PM, j)
    year_split_m_pm = list(set(year_split_m_pm))
    for x in year_split_m_pm:
        count_male_pm[x]+=1
    for j in range(0, len(m_rows_DCM)):
        year_split_m_dcm = year_split_m_dcm + split_years(m_rows_DCM, j)
    year_split_m_dcm = list(set(year_split_m_dcm))
    for x in year_split_m_dcm:
        count_male_dcm[x]+=1
    for j in range(0, len(m_rows_Other)):
        year_split_m_other = year_split_m_other + split_years(m_rows_Other, j)
    year_split_m_other = list(set(year_split_m_other))
    for x in year_split_m_other:
        count_male_other[x]+=1
    for j in range(0, len(m_rows_MoS)):
        year_split_m_mos = year_split_m_mos + split_years(m_rows_MoS, j)
    year_split_m_mos = list(set(year_split_m_mos))
    for x in year_split_m_mos:
        count_male_mos[x]+=1


    for j in range(0, len(m_rows_DPM)):
        year_split_m_dpm = year_split_m_dpm + split_years(m_rows_DPM, j)
    year_split_m_dpm = list(set(year_split_m_dpm))
    for x in year_split_m_dpm:
        count_male_dpm[x]+=1
    for j in range(0, len(m_rows_CM)):
        year_split_m_cm = year_split_m_cm + split_years(m_rows_CM, j)
    year_split_m_cm = list(set(year_split_m_cm))
    for x in year_split_m_cm:
        count_male_cm[x]+=1
    for j in range(0, len(f_rows_PM)):
        year_split_f_pm = year_split_f_pm + split_years(f_rows_PM, j)
    year_split_f_pm = list(set(year_split_f_pm))
    for x in year_split_f_pm:
        count_female_pm[x]+=1
    for j in range(0, len(f_rows_DCM)):
        year_split_f_dcm = year_split_f_dcm + split_years(f_rows_DCM, j)
    year_split_f_dcm = list(set(year_split_f_dcm))
    for x in year_split_f_dcm:
        count_female_dcm[x]+=1

    for j in range(0, len(f_rows_Other)):
        year_split_f_other = year_split_f_other + split_years(f_rows_Other, j)
    year_split_f_other = list(set(year_split_f_other))
    for x in year_split_f_other:
        count_female_other[x]+=1
    for j in range(0, len(f_rows_MoS)):
        year_split_f_mos = year_split_f_mos + split_years(f_rows_MoS, j)
    year_split_f_mos = list(set(year_split_f_mos))
    for x in year_split_f_mos:
        count_female_mos[x]+=1
    for j in range(0, len(f_rows_DPM)):
        year_split_f_dpm = year_split_f_dpm + split_years(f_rows_DPM, j)
    year_split_f_dpm = list(set(year_split_f_dpm))
    for x in year_split_f_dpm:
        count_female_dpm[x]+=1
    for j in range(0, len(f_rows_CM)):
        year_split_f_cm = year_split_f_cm + split_years(f_rows_CM, j)
    year_split_f_cm = list(set(year_split_f_cm))
    for x in year_split_f_cm:
        count_female_cm[x]+=1

# plot out the dictionary

############################ USE THIS SUBSETTING TO SORT OUT THE ERROR ############################

df = req_agg_var

 fig.add_trace(
     go.Bar(x=list(df.year),
     y=list(df[df['gender']=='M'].counts),
     name='Male',
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

 fig.add_trace(
     go.Bar(x=list(df.year),
     y=list(df[(df['gender']=='M') & (df['position']=='PM')].counts),
     name='Male',
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))



############################ VISUALIZATION ############################


import plotly.graph_objects as go
fig = go.Figure()

fig.add_trace(
    go.Bar(x=list(count_male.keys()),
    y=list(count_male.values()),
    name='Male',
marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))
fig.add_trace(
    go.Bar(x=list(count_female.keys()),
    y=list(count_female.values()),
    name='Female',
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))

fig.add_trace(
    go.Bar(x=list(count_male_pm.keys()),
    y=list(count_male_pm.values()),
    name='Male',
    visible= False,
marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))
fig.add_trace(
    go.Bar(x=list(count_female_pm.keys()),
    y=list(count_female_pm.values()),
    name='Female',
           visible=False,
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))
fig.add_trace(
    go.Bar(x=list(count_male_cm.keys()),
    y=list(count_male_cm.values()),
    name='Male',
           visible=False,
marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))
fig.add_trace(
    go.Bar(x=list(count_female_cm.keys()),
    y=list(count_female_cm.values()),
    name='Female',
           visible=False,
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))

fig.add_trace(
    go.Bar(x=list(count_male_dcm.keys()),
    y=list(count_male_dcm.values()),
    name='Male',
           visible=False,
           marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))

fig.add_trace(
    go.Bar(x=list(count_female_dcm.keys()),
    y=list(count_female_dcm.values()),
    name='Female',
           visible=False,
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))
fig.add_trace(
    go.Bar(x=list(count_male_dpm.keys()),
    y=list(count_male_dpm.values()),
    name='Male',
           visible=False,
           marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))

fig.add_trace(
    go.Bar(x=list(count_female_dpm.keys()),
    y=list(count_female_dpm.values()),
    name='Female',
           visible=False,
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))
fig.add_trace(
    go.Bar(x=list(count_male_other.keys()),
    y=list(count_male_other.values()),
    name='Male',
           visible=False,
     marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))
fig.add_trace(
    go.Bar(x=list(count_female_other.keys()),
    y=list(count_female_other.values()),
    name='Female',
           visible=False,
marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))

fig.add_trace(
    go.Bar(x=list(count_male_mos.keys()),
    y=list(count_male_mos.values()),
    name='Male',
           visible=False,
           marker=dict(
               color='#2A8B8E',
               line=dict(
                   color='#2A8B8E'))))
fig.add_trace(
    go.Bar(x=list(count_female_mos.keys()),
    y=list(count_female_mos.values()),
    name='Female',
           visible=False,
    marker=dict(
            color='#D8F0F0',
            line=dict(
                color='#D8F0F0'))))


fig.update_layout(
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,80]),
    plot_bgcolor= '#444444',
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Gender Distribution"}]),

                dict(label="Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,True,True,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Prime Minister Rank: by Gender"}]),

                dict(label="Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,True,True,False,False,False,False,False,False,False,False]},
                           {"title": "Cabinet Minister Rank: by Gender"}]),
                dict(label="Deputy Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,True,True,False,False,False,False,False,False]},
                           {"title": "Deputy Cabinet Minister Rank: by Gender"}]),
                dict(label="Deputy Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,True,True,False,False,False,False]},
                           {"title": "Deputy Prime Minister Rank: by Gender"}]),

                dict(label="Other",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,True,True,False,False]},
                           {"title": "Other(Ambiguous Rank): by Gender"}]),
                dict(label="Minister of State",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,True,True]},
                           {"title": "Minister of State Rank: by Gender"}])
            ]),
        )
    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
# Set title
fig.update_layout(title_text=" Gender Representation Across Ranks")

fig.show()
"""

# build out the entire data frame using a for loop
"""
df= []
for i in range(0, len(cabinet_csv_file)):
    if cabinet_csv_file.ministry_category.iloc[i]=='education':
        dict_to_append = dict(Task=cabinet_csv_file['NAME'].iloc[i], Start=cabinet_csv_file['appointment_begin_in_datetime'].iloc[i], Finish= cabinet_csv_file['appointment_end_in_datetime'].iloc[i],Resource=cabinet_csv_file['HOUSE'].iloc[i])
        df.append(dict_to_append)

 # visualize the chart: make this more intuitive (better colours? )
colors = {'Lok Sabha': 'rgb(34,139,34)',
          'Rajya Sabha':'rgb(178,34,34)',
          'not_applicable': 'rgb(254, 255, 51)'}
fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
fig.show()
"""
