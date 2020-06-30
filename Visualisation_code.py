import pandas as pd
import numpy as np




cabinet_csv_file = pd.read_csv("cabinet_data_final_1006.csv")
###################################################### BUILDING DATA FOR #####################################################################
######################################################### GANTT CHART ########################################################################
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

###################################################### BUILDING DATA FOR #####################################################################
######################################################### BAR CHART ########################################################################

# getting the aggregates

# trying with all df - education_df = cabinet_csv_file
# trying to plot these for each year

def split_years(rows, j):
    year_split = rows.list_of_years.iloc[j].split(',')
    year_split.remove('')
    year_split = [int(x) for x in year_split]
    return(year_split)


######################################################### SETTING DICTIONARIES TO ZERO ##########################################################
count_female = {}
count_male = {}
count_male_pm ={}
count_female_pm={}
count_male_dcm={}
count_female_dcm={}
count_male_cm={}
count_male_dpm={}
count_male_mos={}
count_male_other={}
count_male_dm={}
count_female_cm={}
count_female_dpm={}
count_female_other={}
count_female_mos={}
count_female_dm={}


count_ls={}
count_rs={}
count_not_applicable={}
count_none={}
count_m={}
count_f={}
all_years = [x for x in range(1952, 2019)]
for i in range(0, len(all_years)):
    count_male[all_years[i]] = 0
    count_female[all_years[i]] = 0
    count_female_pm[all_years[i]]= 0
    count_male_pm[all_years[i]]= 0
    count_female_dcm[all_years[i]] = 0
    count_male_dcm[all_years[i]] = 0
    count_female_dm[all_years[i]] = 0
    count_male_dm[all_years[i]] = 0
    count_female_mos[all_years[i]] = 0
    count_male_mos[all_years[i]] = 0
    count_female_dpm[all_years[i]] = 0
    count_male_dpm[all_years[i]] = 0
    count_female_other[all_years[i]] = 0
    count_male_other[all_years[i]] = 0
    count_female_cm[all_years[i]] = 0
    count_male_cm[all_years[i]] = 0

    count_ls[all_years[i]]=0
    count_rs[all_years[i]]=0
    count_not_applicable[all_years[i]]=0
    count_none[all_years[i]]=0




########################################################## PLOTTING DATA FOR HOUSES###############################################################
year=[]
house=[]
position=[]
name = []
all_names = list(set(cabinet_csv_file.NAME))
for i in range(0, len(cabinet_csv_file)):
    name_req = cabinet_csv_file.NAME.iloc[i]
    years_split = cabinet_csv_file.list_of_years.iloc[i].split(',')
    years_split.remove('')
    house_req = cabinet_csv_file.HOUSE.iloc[i]
    pos_req = cabinet_csv_file.RANK.iloc[i]
    for j in years_split:
        name.append(name_req)
        year.append(j)
        house.append(house_req)
        position.append(pos_req)

aggregate_df = pd.DataFrame()
aggregate_df['name']= pd.Series(name).values
aggregate_df['year']= pd.Series(year).values
aggregate_df['house'] = pd.Series(house).values
aggregate_df['position'] = pd.Series(position).values


# Generate aggregate counts (first aggregate by name)
print(aggregate_df.groupby(['name','year','house','position']).agg({'house':'count'}))
req_agg = aggregate_df.groupby(['name','year','house','position']).agg({'house':'count'})
req_agg.columns = ['count_rows']
req_agg = req_agg.reset_index()

# reaggregate - doing this retains the configuration such that
# each name is only counted once (as we drop the count calculated in the above aggregation)
req_agg_drop_cols = req_agg[['year','house','position']]
print(req_agg_drop_cols.groupby(['year','house','position']).agg({'house':'count'}))

req_agg_var = req_agg_drop_cols.groupby(['year','house','position']).size().reset_index(name='counts')
for i in range(0, len(all_names)):
    df_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == all_names[i]]
    ls_rows = df_subset[df_subset['HOUSE']=='Lok Sabha']
    rs_rows = df_subset[df_subset['HOUSE']=='Rajya Sabha']
    none_rows = df_subset[df_subset['HOUSE']=='not_applicable']
    year_split_ls = []
    year_split_rs = []
    year_split_none = []
    for j in range(0, len(ls_rows)):
        year_split_ls = year_split_ls + split_years(ls_rows, j)
    year_split_ls = list(set(year_split_ls))
    for x in year_split_ls:
        count_ls[x]+=1
    for j in range(0, len(rs_rows)):
        year_split_rs = year_split_rs + split_years(rs_rows, j)
    year_split_rs = list(set(year_split_rs))
    for x in year_split_rs:
        count_rs[x]+=1
    for j in range(0, len(none_rows)):
        year_split_none = year_split_none + split_years(none_rows, j)
    year_split_none = list(set(year_split_none))
    for x in year_split_none:
        count_none[x]+=1
df = req_agg_var
print(df)
male= pd.DataFrame




import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
     go.Bar(x=list(count_ls.keys()),
    y=list(count_ls.values()),

     name='Lok Sabha',
            visible=True,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))


fig.add_trace(
     go.Bar(x=list(count_rs.keys()),
    y=list(count_rs.values()),
     name='Rajya Sabha',
            visible=True,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(count_none.keys()),
    y=list(count_none.values()),
     name='Not Applicable',
            visible=True,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))



fig.update_layout(
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,82]),
    xaxis=dict(range=[1951,2019]),
    plot_bgcolor= '#444444',

    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "House Distribution"}]),

                dict(label="Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Prime Minister Rank: by House"}]),

                dict(label="Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False]},
                           {"title": "Cabinet Minister Rank: by House"}]),
                dict(label="Deputy Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False]},
                           {"title": "Deputy Prime Minister Rank: by House"}]),
                dict(label="Deputy Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False]},
                           {"title": "Deputy Cabinet Minister Rank: by House"}]),


                dict(label="Minister of State",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True]},
                           {"title": "Minister of State Rank: by House"}])
            ]),

yanchor="top"
        ),

    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
# Set title
fig.update_layout(title_text=" House Representation Across Ranks")

fig.show()

######################################################### PLOTTING DATA FOR GENDER ##########################################################
############################################################################################################################################
year=[]
gender=[]
position=[]
name = []
all_names = list(set(cabinet_csv_file.NAME))
for i in range(0, len(cabinet_csv_file)):
    name_req = cabinet_csv_file.NAME.iloc[i]
    years_split = cabinet_csv_file.list_of_years.iloc[i].split(',')
    years_split.remove('')
    gender_req = cabinet_csv_file.GENDER.iloc[i]
    pos_req = cabinet_csv_file.RANK.iloc[i]
    for j in years_split:
        name.append(name_req)
        year.append(j)
        gender.append(gender_req)
        position.append(pos_req)

aggregate_df = pd.DataFrame()
aggregate_df['name']= pd.Series(name).values
aggregate_df['year']= pd.Series(year).values
aggregate_df['gender'] = pd.Series(gender).values
aggregate_df['position'] = pd.Series(position).values


# Generate aggregate counts (first aggregate by name)
print(aggregate_df.groupby(['name','year','gender','position']).agg({'gender':'count'}))
req_agg = aggregate_df.groupby(['name','year','gender','position']).agg({'gender':'count'})
req_agg.columns = ['count_rows']
req_agg = req_agg.reset_index()

# reaggregate - doing this retains the configuration such that
# each name is only counted once (as we drop the count calculated in the above aggregation)
req_agg_drop_cols = req_agg[['year','gender','position']]
print(req_agg_drop_cols.groupby(['year','gender','position']).agg({'gender':'count'}))

req_agg_var = req_agg_drop_cols.groupby(['year','gender','position']).size().reset_index(name='counts')
for i in range(0, len(all_names)):
    df_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == all_names[i]]
    f_rows = df_subset[df_subset['GENDER']=='M']
    m_rows = df_subset[df_subset['GENDER']=='F']

    year_split_f = []
    year_split_m = []

    for j in range(0, len(f_rows)):
        year_split_f = year_split_f + split_years(f_rows, j)
    year_split_f = list(set(year_split_f))
    for x in year_split_f:
        count_f[x]+=1
    for j in range(0, len(m_rows)):
        year_split_m = year_split_m + split_years(m_rows, j)
    year_split_m = list(set(year_split_m))
    for x in year_split_m:
        count_rs[x]+=1

df = req_agg_var
print(df)
male= pd.DataFrame




import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
     go.Bar(x=list(count_m.keys()),
    y=list(count_m.values()),

     name='Male',
            visible=True,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))


fig.add_trace(
     go.Bar(x=list(count_f.keys()),
    y=list(count_f.values()),
     name='Female',
            visible=True,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='PM')].year),
     y=list(df[(df['gender']=='M') & (df['position']=='PM')].counts),
     name='Male',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='Female') & (df['position']=='PM')].year),
     y=list(df[(df['gender']=='Female') & (df['position']=='PM')].counts),
     name='Female',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='CM')].year),
     y=list(df[(df['gender']=='M') & (df['position']=='CM')].counts),
     name='Male',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='CM')].year),
     y=list(df[(df['gender']=='F') & (df['position']=='CM')].counts),
     name='Female',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='DPM')].year),
     y=list(df[(df['gender']=='M') & (df['position']=='DPM')].counts),
     name='Male',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='DPM')].year),
     y=list(df[(df['gender']=='F') & (df['position']=='DPM')].counts),
     name='Female',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='DCM')].year),
     y=list(df[(df['gender']=='M') & (df['position']=='DCM')].counts),
     name='Male',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='DCM')].year),
     y=list(df[(df['gender']=='F') & (df['position']=='DCM')].counts),
     name='Female',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))



fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='MoS')].year),
     y=list(df[(df['gender']=='M') & (df['position']=='MoS')].counts),
     name='Male',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='MoS')].year),
     y=list(df[(df['gender']=='F') & (df['position']=='MoS')].counts),
     name='Female',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))




fig.update_layout(
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,82]),
    xaxis=dict(range=[1951,2019]),
    plot_bgcolor= '#444444',

    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Gender Distribution"}]),

                dict(label="Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,True,True,False,False,False,False,False,False,False,False]},
                           {"title": "Prime Minister Rank: by Gender"}]),

                dict(label="Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,True,True,False,False,False,False,False,False]},
                           {"title": "Cabinet Minister Rank: by Gender"}]),
                dict(label="Deputy Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,True,True,False,False,False,False]},
                           {"title": "Deputy Prime Minister Rank: by Gender"}]),
                dict(label="Deputy Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,True,True,False,False]},
                           {"title": "Deputy Cabinet Minister Rank: by Gender"}]),


                dict(label="Minister of State",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,True,True]},
                           {"title": "Minister of State Rank: by Gender"}])
            ]),

yanchor="top"
        ),

    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
# Set title
fig.update_layout(title_text=" Gender Representation Across Ranks")

fig.show()
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
