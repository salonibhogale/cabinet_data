

import pandas as pd

# set -> what is this doing
# len --> get the number of rows
#
# get unique values for the columns: state, constituency, house , year, rank, party, gender, ls_number
#
# for example for house:
# unique_values_for_column_house = set(cabinet_csv_file.house)
# print(unique_values_for_column_house)


cabinet_csv_file = pd.read_csv("cabinet_data_final_1006.csv")
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

print(cabinet_csv_file.columns)
cabinet_csv_file.loc[cabinet_csv_file['PARTY']=='SAMATA PARTY', 'PARTY']= 'SP'
cabinet_csv_file.loc[cabinet_csv_file['PARTY']=='LOK JAN SHAKTI PARTY', 'PARTY']= 'LJSP'
cabinet_csv_file.loc[cabinet_csv_file['PARTY']=='AKALI DAL', 'PARTY']= 'AD'
cabinet_csv_file.loc[cabinet_csv_file['PARTY']=='BANGLA CONG','PARTY']= 'BC'
cabinet_csv_file['PARTY']= cabinet_csv_file['PARTY'].str.replace(' ','')
updated_unique_values_for_party = set(cabinet_csv_file.PARTY)
print(updated_unique_values_for_party)
# 4-June
# See what are the unique values for each column

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


cabinet_csv_file.groupby('PARTY').count()
#cleaning column for appointment_begin
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['appointment_begin']) == True, 'appointment_begin'] = 'NOT_AVAILABLE'
cabinet_csv_file.loc[cabinet_csv_file['appointment_begin']=='N/a','appointment_begin']='NOT_AVAILABLE'

unique_values_for_appointment_begin= set(cabinet_csv_file.appointment_begin)
print(unique_values_for_appointment_begin)
bool_series_appointment_begin = pd.isnull(cabinet_csv_file['appointment_begin'])
set_of_boolean_series_appointment_begin =set(bool_series_appointment_begin)
sum_appointment_begin=sum(set_of_boolean_series_appointment_begin)
print(sum_appointment_begin)#no nan in appointment begin

#cleaning column for appointment_end
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['appointment_end']) == True, 'appointment_end'] = 'NOT_AVAILABLE'
cabinet_csv_file.loc[cabinet_csv_file['appointment_end']=='N/a','appointment_end']='NOT_AVAILABLE'
bool_series_appointment_end = pd.isnull(cabinet_csv_file['appointment_end'])
set_of_boolean_series_appointment_end = set(bool_series_appointment_end)
sum_appointment_end= sum(set_of_boolean_series_appointment_end)
print(sum_appointment_begin)#no nan in appointment_end
#cleaning column for rank
unique_values_for_RANK=set(cabinet_csv_file.RANK)
print(unique_values_for_RANK)
#cleaning column for rank_comment
unique_values_for_rank_comment= set(cabinet_csv_file.RANK_COMMENT)
print(unique_values_for_rank_comment)
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['RANK_COMMENT']) == True, 'RANK_COMMENT'] = 'NOT_APPLICABLE'
#cleaning column for constituecy
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['CONSTITUENCY']) == True, 'CONSTITUENCY'] = 'NOT_APPLICABLE'
#cleaning column for state
cabinet_csv_file.loc[pd.isnull(cabinet_csv_file['STATE']) == True, 'STATE'] = 'NOT_APPLICABLE'
#finding out the difference between appointment_begin and appointment_end
from datetime import datetime

cabinet_csv_file['appointment_begin_in_datetime']= pd.to_datetime(cabinet_csv_file['appointment_begin'], format="%A, %d %B %Y")
#changing some particular data in the column appointment_end
cabinet_csv_file.loc[cabinet_csv_file['appointment_end']=='Tuesday, 4 November, 1969','appointment_end']='Tuesday, 4 November 1969'
cabinet_csv_file['appointment_end_in_datetime']= pd.to_datetime(cabinet_csv_file['appointment_end'], format='%A, %d %B %Y')

import numpy as np
cabinet_csv_file['appointment_difference_in_years'] = cabinet_csv_file['appointment_end_in_datetime'] - cabinet_csv_file['appointment_begin_in_datetime']
cabinet_csv_file['appointment_difference_in_years'] = cabinet_csv_file['appointment_difference_in_years'] / np.timedelta64(1, 'Y')
print(cabinet_csv_file['appointment_difference_in_years'])

cabinet_csv_file['starting_year'] = cabinet_csv_file['appointment_begin_in_datetime'].dt.year
cabinet_csv_file['starting_year'] = pd.to_datetime(cabinet_csv_file['starting_year'], format='%Y')
cabinet_csv_file['end_year'] = cabinet_csv_file['appointment_end_in_datetime'].dt.year
cabinet_csv_file['end_year'] = pd.to_datetime(cabinet_csv_file['end_year'], format='%Y')




# cabinet_csv_file['list_of_years'] = ''
list_of_years = list(range(1952,2019))

def convert_year_to_datetime(year):
    return pd.to_datetime(year, format = '%Y')

list_of_years_datetime = [convert_year_to_datetime(x) for x in list_of_years]


year_list = []
for i in range(0, len(cabinet_csv_file)):
    year_string = ''
    start_year = cabinet_csv_file['starting_year'].iloc[i]
    end_year = cabinet_csv_file['end_year'].iloc[i]
    for year in list_of_years_datetime:
        if year >= start_year and year<= end_year:
           year_string += year.strftime('%Y,')
    year_list.append(year_string)

# assigning list to a new column in the pandas dataframe
cabinet_csv_file['list_of_years'] = pd.Series(year_list).values
print(cabinet_csv_file['list_of_years'])

cabinet_csv_file['appointment_begin_in_datetime'] = cabinet_csv_file['appointment_begin_in_datetime'].dt.strftime('%Y-%m-%d')
cabinet_csv_file['appointment_end_in_datetime'] = cabinet_csv_file['appointment_end_in_datetime'].dt.strftime('%Y-%m-%d')


import plotly.figure_factory as ff



# build out the entire data frame using a for loop
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


# getting the aggregates

education_df = cabinet_csv_file[cabinet_csv_file['ministry_category']=='education']

# trying with all df - education_df = cabinet_csv_file
# trying to plot these for each year

education_df[education_df['NAME']=='T S Soundaram Ramachandran']
all_names = list(set(education_df.NAME))
all_years = [x for x in education_df.list_of_years]
all_years = list(set(','.join(all_years).split(',')))
all_years.remove('')
all_years = [int(x) for x in all_years]
all_years.sort()

count_rs = {}
count_ls = {}
count_none = {}

d = {a1[0]:1, a1[1]:2}

# assign all values of dictionary to 0

for i in range(0, len(all_years)):
    count_rs[all_years[i]]=0
    count_ls[all_years[i]]=0
    count_none[all_years[i]]=0


for i in range(0, len(all_names)):
    df_subset = education_df[education_df['NAME'] == all_names[i]]
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

def split_years(rows, j):
    year_split = rows.list_of_years.iloc[j].split(',')
    year_split.remove('')
    year_split = [int(x) for x in year_split]
    return(year_split)


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


import plotly.express as px

fig = px.bar(all_dfs_combined, x='years', y='count',
             color='house',
             labels={'count':'Number of MPs'}, height=400)
fig.show()






