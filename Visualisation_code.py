import pandas as pd
import numpy as np

cabinet_csv_file = pd.read_csv("cabinet_data_final_3006.csv")
cabinet_csv_file = cabinet_csv_file.fillna('')

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
count_ls={}
count_rs={}
count_not_applicable={}
count_none = {}
all_years = [x for x in range(1947, 2020)]
for i in range(0, len(all_years)):
    count_male[all_years[i]] = 0
    count_female[all_years[i]] = 0
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
# print(aggregate_df.groupby(['name','year','house','position']).agg({'house':'count'}))
req_agg = aggregate_df.groupby(['name','year','house','position']).agg({'house':'count'})
req_agg.columns = ['count_rows']
req_agg = req_agg.reset_index()

# reaggregate - doing this retains the configuration such that
# each name is only counted once (as we drop the count calculated in the above aggregation)
req_agg_drop_cols = req_agg[['year','house','position']]
# print(req_agg_drop_cols.groupby(['year','house','position']).agg({'house':'count'}))

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
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


button_layer_1_height = 1.08
# fig.update_layout(, pad={"b":30})
fig.update_layout(
    title_text="House Representation Across Ranks",
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,90]),
    xaxis=dict(range=[1947,2019]),
    height = 300,
    width =600,
    plot_bgcolor= '#444444',
    margin=dict(t=100, b=0, l=0, r=0),
    updatemenus=[
        dict(

            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "House Representation Across Ranks"}]),

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
            direction="down",
            # pad={"t": 10,"b":10},
            xanchor="left",
            yanchor="top",
            x = 0,
            y = button_layer_1_height
        ),

    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
# Set title

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
    f_rows = df_subset[df_subset['GENDER']=='F']
    m_rows = df_subset[df_subset['GENDER']=='M']
    year_split_f = []
    year_split_m = []
    for j in range(0, len(f_rows)):
        year_split_f = year_split_f + split_years(f_rows, j)
    year_split_f = list(set(year_split_f))
    for x in year_split_f:
        count_female[x]+=1
    for j in range(0, len(m_rows)):
        year_split_m = year_split_m + split_years(m_rows, j)
    year_split_m = list(set(year_split_m))
    for x in year_split_m:
        count_male[x]+=1

df = req_agg_var

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
     go.Bar(x=list(count_male.keys()),
    y=list(count_male.values()),

     name='Male',
            visible=True,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))


fig.add_trace(
     go.Bar(x=list(count_female.keys()),
    y=list(count_female.values()),
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
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='PM')].year),
     y=list(df[(df['gender']=='F') & (df['position']=='PM')].counts),
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
    xaxis=dict(range=[1947,2019]),
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


