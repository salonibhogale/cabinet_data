import pandas as pd
import plotly.figure_factory as ff
from datetime import datetime
import numpy as np
import plotly.express as px


# set -> what is this doing
# len --> get the number of rows
#
# get unique values for the columns: state, constituency, house , year, rank, party, gender, ls_number
#
# for example for house:
# unique_values_for_column_house = set(cabinet_csv_file.house)
# print(unique_values_for_column_house)


cabinet_csv_file = pd.read_csv("cabinet_data_final_1006.csv")

################################################### CAPITALIZING COLUMNS #####################################################################
##############################################################################################################################################

for col in cabinet_csv_file.columns:
    if col in ['name','gender','party','department','rank','rank_comment','house','constituency','state']:
        cabinet_csv_file.rename(columns={col: col.upper()}, inplace=True)

####################################################### DATA CLEANING ########################################################################
##############################################################################################################################################

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


cabinet_csv_file['appointment_begin_in_datetime']= pd.to_datetime(cabinet_csv_file['appointment_begin'], format="%A, %d %B %Y")
#changing some particular data in the column appointment_end
cabinet_csv_file.loc[cabinet_csv_file['appointment_end']=='Tuesday, 4 November, 1969','appointment_end']='Tuesday, 4 November 1969'
cabinet_csv_file['appointment_end_in_datetime']= pd.to_datetime(cabinet_csv_file['appointment_end'], format='%A, %d %B %Y')


cabinet_csv_file['appointment_difference_in_years'] = cabinet_csv_file['appointment_end_in_datetime'] - cabinet_csv_file['appointment_begin_in_datetime']
cabinet_csv_file['appointment_difference_in_years'] = cabinet_csv_file['appointment_difference_in_years'] / np.timedelta64(1, 'Y')
print(cabinet_csv_file['appointment_difference_in_years'])

cabinet_csv_file['starting_year'] = cabinet_csv_file['appointment_begin_in_datetime'].dt.year
cabinet_csv_file['starting_year'] = pd.to_datetime(cabinet_csv_file['starting_year'], format='%Y')
cabinet_csv_file['end_year'] = cabinet_csv_file['appointment_end_in_datetime'].dt.year
cabinet_csv_file['end_year'] = pd.to_datetime(cabinet_csv_file['end_year'], format='%Y')

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
cabinet_csv_file.loc[cabinet_csv_file['ministry_category']=='steel, coal, mines, oil, petrol, chemicals, fertillizers', 'ministry_category']= "steel, coal, mines, oil, petrol, chemicals, fertilizers"
cabinet_csv_file.loc[cabinet_csv_file['ministry_category2']=='steel, coal, mines, oil, petrol, chemicals, fertillizers', 'ministry_category']= "steel, coal, mines, oil, petrol, chemicals, fertilizers"
cabinet_csv_file.loc[cabinet_csv_file['ministry_category']=='rural development, community development, panchayati raj, rural development', 'ministry_category']= "rural development, community development, panchayati raj"
cabinet_csv_file.loc[cabinet_csv_file['ministry_category2']=='rural development, community development, panchayati raj, rural development', 'ministry_category']= "rural development, community development, panchayati raj"


# fixing ministry names and categories for some ministries
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='revenue & banking','ministry_category']='finance'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='indo pak agreement','ministry_category']='external affairs'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='disinvestment','ministry_category']='finance'
# adding second ministry category for some ministries
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='food & agriculture','ministry_category2']='agriculture'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='food & civil supplies','ministry_category2']='commerce, industry, civil supplies'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='food, agriculture, community development & cooperation','ministry_category2']='agriculture; community development, panchayati raj, rural development'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='food processing industries, agriculture','ministry_category2']='agriculture'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='Social and women\'s welfare','ministry_category2']='women, social justice, minority, tribal affairs'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='urban affairs & emplyoment','ministry_category2']='labour, employment, rehabilitation'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='urban employment & poverty alleviation','ministry_category2']='labour, employment, rehabilitation'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='works, housing & rehabilitation','ministry_category2']='labour, employment, rehabilitation'
cabinet_csv_file.loc[cabinet_csv_file['ministry_name']=='tourism & culture','ministry_category2']='culture'


min_names = []
min_category = []
for i in set(cabinet_csv_file.ministry_category):
    subset_df1 = cabinet_csv_file[cabinet_csv_file.ministry_category==i]
    ministry_names1 = set(subset_df1.ministry_name)
    subset_df2 = cabinet_csv_file[cabinet_csv_file.ministry_category2==i]
    ministry_names2 = set(subset_df2.ministry_name)
    all_names = list(ministry_names1) + list(ministry_names2)
    min_names.append(all_names)
    min_category.append(i)

min_cat_df = pd.DataFrame()
min_cat_df['min_category'] = pd.Series(min_category).values
min_cat_df['min_names'] = pd.Series(min_names).values
min_cat_df.to_csv('ministry_categories.csv')


####################################################### ADDING YEARS DATA ####################################################################
##############################################################################################################################################


list_of_years = list(range(1952,2019))

def convert_year_to_datetime(year):
    return pd.to_datetime(year, format = '%Y')

list_of_years_datetime = [convert_year_to_datetime(x) for x in list_of_years]


year_list = []
for i in range(0, len(cabinet_csv_file)):
    year_string = ''
    start_year = pd.to_datetime(cabinet_csv_file['appointment_begin_in_datetime'].iloc[i])
    end_year = pd.to_datetime(cabinet_csv_file['appointment_end_in_datetime'].iloc[i])
    for year in list_of_years_datetime:
        if year >= start_year and year<= end_year:
           year_string += year.strftime('%Y,')
    year_list.append(year_string)

# assigning list to a new column in the pandas dataframe
cabinet_csv_file['list_of_years'] = pd.Series(year_list).values
print(cabinet_csv_file['list_of_years'])


####################################################### FIXING DATE FORMATS ##################################################################
##############################################################################################################################################
cabinet_csv_file['appointment_begin_in_datetime'] = cabinet_csv_file['appointment_begin_in_datetime'].dt.strftime('%Y-%m-%d')
cabinet_csv_file['appointment_end_in_datetime'] = cabinet_csv_file['appointment_end_in_datetime'].dt.strftime('%Y-%m-%d')


####################################################### SUBSETING EXAMPLE ####################################################################
##############################################################################################################################################
print(set(list(cabinet_csv_file[cabinet_csv_file.NAME == 'Kailash Nath Katju'].HOUSE)))
subset_lok_sabha = cabinet_csv_file[(cabinet_csv_file['NAME'] == 'Kailash Nath Katju') & (cabinet_csv_file['HOUSE'] == 'Lok Sabha')]
print(subset_lok_sabha)


###################################################### BUILDING DATA FOR #####################################################################
######################################################### GANTT CHART ########################################################################
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
count_none={}

all_years = [x for x in range(1952, 2019)]
for i in range(0, len(all_years)):
    count_female[all_years[i]]= 0
    count_male[all_years[i]]= 0
    count_ls[all_years[i]]=0
    count_rs[all_years[i]]=0
    count_not_applicable[all_years[i]]=0
    count_none[all_years[i]]=0

######################################################### PLOTTING DATA FOR HOUSE ##########################################################
############################################################################################################################################
all_names = list(set(cabinet_csv_file.NAME))

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


######################################################### PLOTTING DATA FOR GENDER ##########################################################
############################################################################################################################################


all_names = list(set(cabinet_csv_file.NAME))

for i in range(0, len(all_names)):
    df_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == all_names[i]]
    m_rows = df_subset[df_subset['GENDER']=='M']
    f_rows = df_subset[df_subset['GENDER']=='F']
    year_split_m = []
    year_split_f = []
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

# plot out the dictionary

# first create the complete df
complete_df1 = pd.DataFrame()
complete_df1['years'] = pd.Series(list(count_male.keys())).values
complete_df1['count'] = pd.Series(list(count_male.values())).values
complete_df1['gender'] = 'Male'


complete_df2 = pd.DataFrame()
complete_df2['years'] = pd.Series(list(count_female.keys())).values
complete_df2['count'] = pd.Series(list(count_female.values())).values
complete_df2['gender'] = 'Female'

all_dfs = [complete_df1, complete_df2]
all_dfs_combined = pd.concat(all_dfs)

fig = px.bar(all_dfs_combined, x='years', y='count',
             color='gender',
             labels={'count':'Number of MPs'}, height=400)
fig.show()



######################################################### YOU CAN CROSS CHECK YOUR CODE #####################################################
#############################################################################################################################################


# list_of_years_part_2
common_names = []
for i in unique_values_for_name:
    if len(cabinet_csv_file[cabinet_csv_file['NAME'] == i]) > 1:
        common_names.append(i)


list_of_years_2 = pd.DataFrame()



for i in common_names:
    count_rows_gender={}
    for p in range(0,len(all_years)):
        count_rows_gender[all_years[p]]=0
    subset= cabinet_csv_file[cabinet_csv_file['NAME']==i]
    for j in range(0, len(subset)):
        year_split = split_years(subset, j)
        for x in year_split:
            count_rows_gender[x] += 1
    list_of_all_years = [k for k,v in count_rows_gender.items() if v >= 1]
    set1=set(cabinet_csv_file[cabinet_csv_file.NAME == i].GENDER)
    if 'F' in set1:
        for x in list_of_all_years:
            count_female[x] +=1
    else:
        for x in list_of_all_years:
            count_male[x] += 1

unique_names=[]
for i in unique_values_for_name:
    if i not in common_names:
        unique_names.append(i)

for i in unique_names:
    df_gender_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == i]
    f_rows = df_gender_subset[df_gender_subset['GENDER']=='F']
    m_rows = df_gender_subset[df_gender_subset['GENDER']=='M']

    for j in range(0, len(f_rows)):
        year_split = split_years(f_rows, j)
        for x in year_split:
            count_female[x]+=1
    for j in range(0, len(m_rows)):
        year_split = split_years(m_rows, j)
        for x in year_split:
            count_male[x]+=1
complete_gender = pd.DataFrame()
complete_gender['years'] = pd.Series(list(count_female.keys())).values
complete_gender['count'] = pd.Series(list(count_female.values())).values
complete_gender['gender'] = 'Female'


complete_gender2 = pd.DataFrame()
complete_gender2['years'] = pd.Series(list(count_male.keys())).values
complete_gender2['count'] = pd.Series(list(count_male.values())).values
complete_gender2['gender'] = 'Male'

all_dfs_gender = [complete_gender, complete_gender2]
all_dfs_combined_gender = pd.concat(all_dfs_gender)




fig34 = px.bar(all_dfs_combined_gender, x='years', y='count',
             color='gender',
             labels={'count':'Number of MPs'}, height=400)
fig34.show()



for i in common_names:
    set1 = set(cabinet_csv_file[cabinet_csv_file.NAME == i].HOUSE)
    count_rows_ls = {}
    count_rows_rs = {}
    count_rows_none = {}
    for p in range(0, len(all_years)):
        count_rows_ls[all_years[p]] = 0
        count_rows_rs[all_years[p]] = 0
        count_rows_none[all_years[p]] = 0
    if 'Lok Sabha' in set1:
        subset_lok_sabha = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'Lok Sabha')]
        for j in range(0, len(subset_lok_sabha)):
            year_split = split_years(subset_lok_sabha, j)
            for x in year_split:
                count_rows_ls[x] += 1
        list_of_all_years = [k for k,v in count_rows_ls.items() if v >= 1]
        for x in list_of_all_years:
            count_ls[x] +=1

    if 'Rajya Sabha' in set1:
        subset_rajya_sabha = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'Rajya Sabha')]
        for j in range(0, len(subset_rajya_sabha)):
            year_split = split_years(subset_rajya_sabha, j)
            for x in year_split:
                count_rows_rs[x] += 1
        list_of_all_years = [k for k, v in count_rows_rs.items() if v >= 1]
        for x in list_of_all_years:
            count_rs[x] += 1

    if 'not_applicable' in set1:
        subset_not_applicable = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'not_applicable')]
        for j in range(0, len(subset_not_applicable)):
            year_split = split_years(subset_not_applicable, j)
            for x in year_split:
                count_rows_none[x] += 1
        list_of_all_years = [k for k, v in count_rows_none.items() if v >= 1]
        for x in list_of_all_years:
            count_not_applicable[x] += 1
for i in unique_names:
    df_house_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == i]
    ls_rows = df_house_subset[df_house_subset['HOUSE']=='Lok Sabha']
    rs_rows = df_house_subset[df_house_subset['HOUSE']=='Rajya Sabha']
    none_rows = df_house_subset[df_house_subset['HOUSE']=='not_applicable']

    for j in range(0, len(ls_rows)):
        year_split = split_years(ls_rows, j)
        for x in year_split:
            count_ls[x]+=1
    for j in range(0, len(rs_rows)):
        year_split = split_years(rs_rows, j)
        for x in year_split:
            count_rs[x]+=1
complete_df1 = pd.DataFrame()
complete_df1['years'] = pd.Series(list(count_ls.keys())).values
complete_df1['count'] = pd.Series(list(count_ls.values())).values
complete_df1['house'] = 'Lok Sabha'


complete_df2 = pd.DataFrame()
complete_df2['years'] = pd.Series(list(count_rs.keys())).values
complete_df2['count'] = pd.Series(list(count_rs.values())).values
complete_df2['house'] = 'Rajya Sabha'

complete_df3 = pd.DataFrame()
complete_df3['years'] = pd.Series(list(count_not_applicable.keys())).values
complete_df3['count'] = pd.Series(list(count_not_applicable.values())).values
complete_df3['house'] = 'not_applicable'

all_dfs = [complete_df1, complete_df2, complete_df3]
all_dfs_combined = pd.concat(all_dfs)




fig = px.bar(all_dfs_combined, x='years', y='count',
             color='house',
             labels={'count':'Number of MPs'}, height=400)
fig.show()
fig1 = px.line(all_dfs_combined, x="years", y="count", color='house')
fig1.show()
common_names_PM = []
for i in common_names:
    set1=set(cabinet_csv_file[cabinet_csv_file.NAME == i].RANK)
    if 'PM' in set1:
    set1 = set(cabinet_csv_file[cabinet_csv_file.NAME == i].HOUSE)
    count_rows_ls = {}
    count_rows_rs = {}
    count_rows_none = {}
    for p in range(0, len(all_years)):
        count_rows_ls[all_years[p]] = 0
        count_rows_rs[all_years[p]] = 0
        count_rows_none[all_years[p]] = 0
    if 'Lok Sabha' in set1:
        subset_lok_sabha = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'Lok Sabha')]
        for j in range(0, len(subset_lok_sabha)):
            year_split = split_years(subset_lok_sabha, j)
            for x in year_split:
                count_rows_ls[x] += 1
        list_of_all_years = [k for k,v in count_rows_ls.items() if v >= 1]
        for x in list_of_all_years:
            count_ls[x] +=1

    if 'Rajya Sabha' in set1:
        subset_rajya_sabha = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'Rajya Sabha')]
        for j in range(0, len(subset_rajya_sabha)):
            year_split = split_years(subset_rajya_sabha, j)
            for x in year_split:
                count_rows_rs[x] += 1
        list_of_all_years = [k for k, v in count_rows_rs.items() if v >= 1]
        for x in list_of_all_years:
            count_rs[x] += 1

    if 'not_applicable' in set1:
        subset_not_applicable = cabinet_csv_file[(cabinet_csv_file['NAME'] == i) & (cabinet_csv_file['HOUSE'] == 'not_applicable')]
        for j in range(0, len(subset_not_applicable)):
            year_split = split_years(subset_not_applicable, j)
            for x in year_split:
                count_rows_none[x] += 1
        list_of_all_years = [k for k, v in count_rows_none.items() if v >= 1]
        for x in list_of_all_years:
            count_not_applicable[x] += 1
for i in unique_names:
    df_house_subset = cabinet_csv_file[cabinet_csv_file['NAME'] == i]
    ls_rows = df_house_subset[df_house_subset['HOUSE']=='Lok Sabha']
    rs_rows = df_house_subset[df_house_subset['HOUSE']=='Rajya Sabha']
    none_rows = df_house_subset[df_house_subset['HOUSE']=='not_applicable']

    for j in range(0, len(ls_rows)):
        year_split = split_years(ls_rows, j)
        for x in year_split:
            count_ls[x]+=1
    for j in range(0, len(rs_rows)):
        year_split = split_years(rs_rows, j)
        for x in year_split:
            count_rs[x]+=1
complete_df1 = pd.DataFrame()
complete_df1['years'] = pd.Series(list(count_ls.keys())).values
complete_df1['count'] = pd.Series(list(count_ls.values())).values
complete_df1['house'] = 'Lok Sabha'


complete_df2 = pd.DataFrame()
complete_df2['years'] = pd.Series(list(count_rs.keys())).values
complete_df2['count'] = pd.Series(list(count_rs.values())).values
complete_df2['house'] = 'Rajya Sabha'

complete_df3 = pd.DataFrame()
complete_df3['years'] = pd.Series(list(count_not_applicable.keys())).values
complete_df3['count'] = pd.Series(list(count_not_applicable.values())).values
complete_df3['house'] = 'not_applicable'

all_dfs = [complete_df1, complete_df2, complete_df3]
all_dfs_combined = pd.concat(all_dfs)




fig = px.bar(all_dfs_combined, x='years', y='count',
             color='house',
             labels={'count':'Number of MPs'}, height=400)
fig.show()
fig1 = px.line(all_dfs_combined, x="years", y="count", color='house')
fig1.show()

fig5 = go.Figure()
fig5.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker_color='indianred'
fig5.add_trace(
    go.Scatter(x=list(df.index),
               y=list(df.High),
               name="High",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=[df.High.mean()] * len(df.index),
               name="High Average",
               visible=False,
               line=dict(color="#33CFA5", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=list(df.Low),
               name="Low",
               line=dict(color="#F06A6A")))

fig.add_trace(
    go.Scatter(x=list(df.index),
               y=[df.Low.mean()] * len(df.index),
               name="Low Average",
               visible=False,
               line=dict(color="#F06A6A", dash="dash")))

# Add Annotations and Buttons
DM_annotations = [dict(x="2016-03-01",
                         y=df.High.mean(),
                         xref="x", yref="y",
                         text="High Average:<br> %.3f" % df.High.mean(),
                         ax=0, ay=-40),
                    dict(x=df.High.idxmax(),
                         y=df.High.max(),
                         xref="x", yref="y",
                         text="High Max:<br> %.3f" % df.High.max(),
                         ax=0, ay=-40)]
low_annotations = [dict(x="2015-05-01",
                        y=df.Low.mean(),
                        xref="x", yref="y",
                        text="Low Average:<br> %.3f" % df.Low.mean(),
                        ax=0, ay=40),
                   dict(x=df.High.idxmin(),
                        y=df.Low.min(),
                        xref="x", yref="y",
                        text="Low Min:<br> %.3f" % df.Low.min(),
                        ax=0, ay=40)]

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="None",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Yahoo",
                            "annotations": []}]),
                dict(label="High",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Yahoo High",
                            "annotations": high_annotations}]),
                dict(label="Low",
                     method="update",
                     args=[{"visible": [False, False, True, True]},
                           {"title": "Yahoo Low",
                            "annotations": low_annotations}]),
                dict(label="Both",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Yahoo",
                            "annotations": high_annotations + low_annotations}]),
            ]),
        )
    ])

# Set title
fig.update_layout(title_text="Yahoo")

fig.show()



