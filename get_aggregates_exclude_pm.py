import pandas as pd
import numpy as np

cabinet_csv_file = pd.read_csv("cabinet_data_final_3006.csv")
cabinet_csv_file = cabinet_csv_file.fillna('')

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

# are all PMs also CMs?

for i in range(0, len(cabinet_csv_file)):
    if cabinet_csv_file.RANK.iloc[i]=='PM':
        name_instance = cabinet_csv_file.NAME.iloc[i]
        print(name_instance)
        # get list of years
        print(cabinet_csv_file.list_of_years.iloc[i])

        # for these years: check if same name is for rank 'CM'


        df_subset = cabinet_csv_file[cabinet_csv_file['NAME']==name_instance]
        # get year subset
        years_all = split_years(df_subset,i)
        if 'CM' not in list(df_subset.RANK):
            print(name_instance)
