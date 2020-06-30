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

########################################################## PLOTTING DATA FOR HOUSES ################################################################

########################################################## GROUP BY METHOD ################################################################
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

req_agg_var.to_csv('aggregates_using_groupby.csv',index=False)



######################################################### GETTING AGGREGATES ##########################################################
######################################################### METHOD 2 ##########################################################
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
all_years = [x for x in range(1947, 2020)]
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

# COMPARE THE VALUES OF THE AGGREGATES

### CHANGE THE CODE HERE
