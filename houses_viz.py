import plotly.graph_objects as go
fig = go.Figure()

# ADD TRACE: Total
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

# ADD TRACE: PM
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].year),
            y=list(df[(df['house']=='Lok Sabha') & (df['position']=='PM')].counts),
            name='Lok Sabha',
            visible=False,
            marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].year),
            y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='PM')].counts),
            name='Rajya Sabha',
            visible=False,
            marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].year),
            y=list(df[(df['house']=='not_applicable') & (df['position']=='PM')].counts),
            name='Not Applicable',
            visible=False,
            marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].year),
            y=list(df[(df['house']=='Lok Sabha') & (df['position']=='CM')].counts),
            name='Lok Sabha',
            visible=False,
            marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].year),
            y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='CM')].counts),
            name='Rajya Sabha',
            visible=False,
            marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].year),
            y=list(df[(df['house']=='not_applicable') & (df['position']=='CM')].counts),
            name='Not Applicable',
            visible=False,
            marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].year),
            y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DPM')].counts),
            name='Lok Sabha',
            visible=False,
            marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].year),
            y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DPM')].counts),
            name='Rajya Sabha',
            visible=False,
            marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].year),
            y=list(df[(df['house']=='not_applicable') & (df['position']=='DPM')].counts),
            name='Not Applicable',
            visible=False,
            marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].year),
            y=list(df[(df['house']=='Lok Sabha') & (df['position']=='DCM')].counts),
            name='Lok Sabha',
            visible=False,
            marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].year),
            y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='DCM')].counts),
            name='Rajya Sabha',
            visible=False,
            marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].year),
            y=list(df[(df['house']=='not_applicable') & (df['position']=='DCM')].counts),
            name='Not Applicable',
            visible=False,
            marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].year),
            y=list(df[(df['house']=='Lok Sabha') & (df['position']=='MoS')].counts),
            name='Lok Sabha',
            visible=False,
            marker=dict(
                color='#C85250',
                line=dict(
                    color='#C85250'))))

fig.add_trace(
     go.Bar(x=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].year),
            y=list(df[(df['house']=='Rajya Sabha') & (df['position']=='MoS')].counts),
            name='Rajya Sabha',
            visible=False,
            marker=dict(
                color='#F7BEC0',
                line=dict(
                    color='#F7BEC0'))))
fig.add_trace(
     go.Bar(x=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].year),
            y=list(df[(df['house']=='not_applicable') & (df['position']=='MoS')].counts),
            name='Not Applicable',
            visible=False,
            marker=dict(
                color='#E9EAE0',
                line=dict(
                    color='#E9EAE0'))))


button_layer_1_height = 1.50
# fig.update_layout(, pad={"b":30})
fig.update_layout(
    title_text="House Representation Across Ranks",
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,90]),
    xaxis=dict(range=[1947,2020]),
    height = 600,
    width =1200,
    plot_bgcolor= '#444444',
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "House Representation Across Ranks"}]),

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
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False]},
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
            direction="down",
            xanchor="left",
            yanchor="top",
            x = 0,
            y = 1.1
        ),

    ])
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#444444')

fig.show()
import plotly.offline.offline
print(plotly.offline.plot(fig, include_plotlyjs=False, output_type='div'))
