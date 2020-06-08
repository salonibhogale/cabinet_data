from typing import Any, Union

import pandas as pd

# set -> what is this doing
# len --> get the number of rows
#
# get unique values for the columns: state, constituency, house , year, rank, party, gender, ls_number
#
# for example for house:
# unique_values_for_column_house = set(cabinet_csv_file.house)
# print(unique_values_for_column_house)
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

cabinet_csv_file = pd.read_csv("cabinet_data_consistency_1205_26M.csv")

unique_values_for_state = set(cabinet_csv_file.state)
print(unique_values_for_state)
#  Punjab and Punajb,
u=set(cabinet_csv_file.num_of_years)
print(u)
unique_values_for_constituency = set(cabinet_csv_file.constituency)
print(unique_values_for_constituency)
unique_values_for_house = set(cabinet_csv_file.house)
print(unique_values_for_house)
# nan for house
unique_values_for_year = set(cabinet_csv_file.year)  # Why is the year appearing as only nan?
print(unique_values_for_year)
unique_values_for_party = set(cabinet_csv_file.party)
print(unique_values_for_party)
# SAMATA PARTY and Samata Party(some parties are in lowercase while others are in uppercase
unique_values_for_gender = set(cabinet_csv_file.gender)
print(unique_values_for_gender)
unique_values_for_ls_number = set(cabinet_csv_file.ls_number)
print(unique_values_for_ls_number)
unique_values_for_department_update = set(cabinet_csv_file.department_update)
print(unique_values_for_department_update)


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
    if col in ['name','gender','party','ministry','department','department_update','rank','rank_comment','party.1','house','constituency','state']:
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




#unique_values_for_house = set(cabinet_csv_file.house)

#bool_series = pd.isnull(cabinet_csv_file["house"])

#len(cabinet_csv_file)
#cabinet_csv_file[['house']].count()
#cabinet_csv_file.groupby('house').count()



