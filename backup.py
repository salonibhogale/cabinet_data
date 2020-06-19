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
