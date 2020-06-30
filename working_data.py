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

cabinet_csv_file.loc[cabinet_csv_file['appointment_begin']=='Tueday, 13 March 1990','appointment_begin']='Tuesday, 13 March 1990'
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


list_of_years = list(range(1947,2020))

def convert_year_to_datetime(year):
    return pd.to_datetime('01-01-'+ str(year), format = '%d-%m-%Y')

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

cabinet_csv_file.to_csv('cabinet_data_final_3006.csv')
