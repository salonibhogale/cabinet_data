import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('aggregates_using_groupby.csv')
fig = go.Figure()
fig.add_trace(
     go.Bar(x=list(count_ls.keys()),
    y=list(count_ls.values()),

     name='Lok Sabha',
            visible=True,
 marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(count_rs.keys()),
    y=list(count_rs.values()),
     name='Rajya Sabha',
            visible=True,
 marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(count_none.keys()),
    y=list(count_none.values()),
     name='Not Applicable',
            visible=True,
 marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].counts),
     name='Lok Sabha',
            visible=False,
 marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].counts),
     name='Rajya Sabha',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].year),
     y=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].counts),
     name='Not Applicable',
visible=False,
 marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))



fig.update_layout(
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,82]),
    xaxis=dict(range=[1951,2019]),
    plot_bgcolor= '#444444',

    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "House Distribution"}]),

                dict(label="Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Prime Minister Rank: by House"}]),

                dict(label="Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,False,False]},
                           {"title": "Cabinet Minister Rank: by House"}]),
                dict(label="Deputy Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False]},
                           {"title": "Deputy Prime Minister Rank: by House"}]),
                dict(label="Deputy Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,False]},
                           {"title": "Deputy Cabinet Minister Rank: by House"}]),


                dict(label="Minister of State",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,True]},
                           {"title": "Minister of State Rank: by House"}])
            ]),

yanchor="top"
        ),

    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
# Set title
fig.update_layout(title_text=" House Representation Across Ranks")

fig.show()
