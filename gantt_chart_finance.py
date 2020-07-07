import plotly.figure_factory as ff
import pandas as pd

cabinet_csv_file = pd.read_csv("cabinet_data_final_3006.csv")
cabinet_csv_file = cabinet_csv_file.fillna('')

# df= []
# for i in range(0, len(cabinet_csv_file)):
#     if cabinet_csv_file.ministry_category.iloc[i]=='education':
#         dict_to_append = dict(Task=cabinet_csv_file['NAME'].iloc[i],
#                               Start=cabinet_csv_file['appointment_begin_in_datetime'].iloc[i],
#                               Finish= cabinet_csv_file['appointment_end_in_datetime'].iloc[i],
#                               Resource=cabinet_csv_file['RANK'].iloc[i])
#         df.append(dict_to_append)

cabinet_csv_file_req = cabinet_csv_file[(cabinet_csv_file['ministry_name']=='minority affairs')]
cabinet_csv_file_req = cabinet_csv_file_req.sort_values(by=['appointment_begin_in_datetime'])

df2=[]
for i in range(0, len(cabinet_csv_file_req)):
    if cabinet_csv_file_req.ministry_name.iloc[i]=='minority affairs':
        if cabinet_csv_file_req['NAME'].iloc[i] == 'CHANDRA SHEKHAR':
            name = "Chandra Shekhar"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'P. V. NARASIMHA RAO':
            name = "P.V. Narasimha Rao"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'ATAL BIHARI VAJPAYEE':
            name = "Atal Bihari Vajpayee"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'H. D. DEVE GOWDA':
            name = "H.D. Deve Gowda"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'I. K. GUJRAL':
            name = "I.K. Gujral"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'MANMOHAN SINGH':
            name = "Manmohan Singh"
        elif cabinet_csv_file_req['NAME'].iloc[i] == 'NARENDRA MODI':
            name = "Narendra Modi"
        else:
            name = cabinet_csv_file_req['NAME'].iloc[i]
        # name = name + ' (' + cabinet_csv_file_req['PARTY'].iloc[i] + ')'
        if cabinet_csv_file_req['RANK'].iloc[i] == 'CM':
            party_name = 'Cabinet Minister'
        elif cabinet_csv_file_req['RANK'].iloc[i] == 'MoS':
            party_name = 'Minister of State'
        elif cabinet_csv_file_req['RANK'].iloc[i] == 'DCM':
            party_name = 'Deputy Cabinet Minister'
        else:
            party_name = "Other Category"
        dict_to_append = dict(Task=name,
                              Start=cabinet_csv_file_req['appointment_begin_in_datetime'].iloc[i],
                              Finish= cabinet_csv_file_req['appointment_end_in_datetime'].iloc[i],
                              Resource=party_name)
        df2.append(dict_to_append)




 # visualize the chart: make this more intuitive (better colours? )
colors = {'Cabinet Minister': '#3E92CC',
          'Deputy Cabinet Minister':'#D34E24',
          'Minister of State': '#129490',
          'Other Category':'#FFFFF'
          }

fig = ff.create_gantt(df2, colors=colors,showgrid_x = True, showgrid_y = True, title="Council of Ministers for Ministry of Finance", index_col='Resource', show_colorbar=True, group_tasks=True,height=400)

fig.show()



import plotly.offline.offline
print(plotly.offline.plot(fig, include_plotlyjs=False, output_type='div'))
