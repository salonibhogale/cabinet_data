import pandas as pd
import numpy as np

cabinet_csv_file = pd.read_csv("cabinet_data_final_3006.csv")
cabinet_csv_file = cabinet_csv_file.fillna('')

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
        print(i)
        # print(name_instance)
        # get list of years
        # print(cabinet_csv_file.list_of_years.iloc[i])

        # for these years: check if same name is for rank 'CM'
        if cabinet_csv_file.list_of_years.iloc[i]!='':
            split_years = cabinet_csv_file.list_of_years.iloc[i].split(',')
            split_years.remove('')
            # for these years check if any with same name is "NOT" CM
            df_subset = cabinet_csv_file[(cabinet_csv_file['NAME']==name_instance) & (cabinet_csv_file['RANK']=='CM')]
            # setting PM's metadata to 0
            dict = {}
            for s in split_years:
                dict[s]=0
            print(dict)
            for j in split_years:
                for k in range(0, len(df_subset)):
                    if j in df_subset.iloc[k].list_of_years:
                        dict[j]+=1
            print(dict)

# Proved that for all years: PMs hold > 1 position as CM as well

# but are there any members who hold >1 positions at any point of time?

def position_clash(check_position, compare_position, cabinet_csv_file):
    for i in range(0, len(cabinet_csv_file)):
        if cabinet_csv_file.RANK.iloc[i]==check_position:
            name_instance = cabinet_csv_file.NAME.iloc[i]

            # for these years: check if same name is for rank 'CM'
            if cabinet_csv_file.list_of_years.iloc[i]!='':
                split_years = cabinet_csv_file.list_of_years.iloc[i].split(',')
                split_years.remove('')
                # for these years check if any with same name is "NOT" CM
                df_subset = cabinet_csv_file[(cabinet_csv_file['NAME']==name_instance) & (cabinet_csv_file['RANK']==compare_position)]
                # setting PM's metadata to 0
                dict = {}
                for s in split_years:
                    dict[s]=0
                # print(dict)
                for j in split_years:
                    for k in range(0, len(df_subset)):
                        if j in df_subset.iloc[k].list_of_years:
                            dict[j]+=1
                if 0 not in dict.values():
                    print("Error for",name_instance, i)

position_clash('PM','CM',cabinet_csv_file)
position_clash('DCM','CM',cabinet_csv_file)
position_clash('MoS','CM',cabinet_csv_file)
position_clash('DPM','CM',cabinet_csv_file)
position_clash('Other','CM',cabinet_csv_file)

# Error for Jai Sukh Lal Hathi 376
# Error for PIYUSH GOYAL 1982
# Error for M. THAMBIDURAI 2584
# Error for BABUL SUPRIYO 3291
# Error for Morarji Desai 753
# Error for Yeshwantrao Chavan 1118
# Error for Sardar Vallabhbhai Patel 1878
# Error for LAL KRISHNA ADVANI 3444
# Error for DEVI LAL 3448
# Error for Krishna Chandra Pant 803
# Error for Madhavsinh Solanki 1538
