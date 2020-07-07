import plotly.figure_factory as ff
import pandas as pd

cabinet_csv_file = pd.read_csv("cabinet_data_final_3006.csv")
cabinet_csv_file = cabinet_csv_file.fillna('')

cabinet_csv_file_req = cabinet_csv_file[(cabinet_csv_file['RANK']=='PM')]
cabinet_csv_file_req = cabinet_csv_file_req.sort_values(by=['appointment_begin_in_datetime'])

df2=[]
for i in range(0, len(cabinet_csv_file_req)):
    if cabinet_csv_file_req.RANK.iloc[i]=='PM':
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
        if cabinet_csv_file_req['PARTY'].iloc[i] == 'JP':
            party_name = 'Janata Party'
        elif cabinet_csv_file_req['PARTY'].iloc[i] == 'JD':
            party_name = 'Janata Dal'
        elif cabinet_csv_file_req['PARTY'].iloc[i] == 'INC':
            party_name = 'Indian National Congress'
        elif cabinet_csv_file_req['PARTY'].iloc[i] == 'BJP':
            party_name = 'Bharatiya Janata Party'
        dict_to_append = dict(Task=name,
                              Start=cabinet_csv_file_req['appointment_begin_in_datetime'].iloc[i],
                              Finish= cabinet_csv_file_req['appointment_end_in_datetime'].iloc[i],
                              Resource=party_name)
        df2.append(dict_to_append)




 # visualize the chart: make this more intuitive (better colours? )
colors = {'Indian National Congress': '#3E92CC',
          'Janata Party':'#D34E24',
          'Janata Dal': '#129490',
          'Bharatiya Janata Party': '#F28123',
          }

fig = ff.create_gantt(df2, colors=colors,showgrid_x = True, showgrid_y = True, title="Terms of Prime Ministers: 1947 to 2019", index_col='Resource', show_colorbar=True, group_tasks=True)



fig.show()

import plotly.offline.offline
print(plotly.offline.plot(fig, include_plotlyjs=False, output_type='div'))
