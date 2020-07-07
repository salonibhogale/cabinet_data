import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
     go.Bar(x=list(count_male.keys()),
            y=list(count_male.values()),
            name='Male',
            visible=True,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))


fig.add_trace(
     go.Bar(x=list(count_female.keys()),
            y=list(count_female.values()),
            name='Female',
            visible=True,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='PM')].year),
            y=list(df[(df['gender']=='M') & (df['position']=='PM')].counts),
            name='Male',
            visible=False,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='PM')].year),
            y=list(df[(df['gender']=='F') & (df['position']=='PM')].counts),
            name='Female',
            visible=False,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='CM')].year),
            y=list(df[(df['gender']=='M') & (df['position']=='CM')].counts),
            name='Male',
            visible=False,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='CM')].year),
            y=list(df[(df['gender']=='F') & (df['position']=='CM')].counts),
            name='Female',
            visible=False,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='DPM')].year),
            y=list(df[(df['gender']=='M') & (df['position']=='DPM')].counts),
            name='Male',
            visible=False,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='DPM')].year),
            y=list(df[(df['gender']=='F') & (df['position']=='DPM')].counts),
            name='Female',
            visible=False,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))


fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='DCM')].year),
            y=list(df[(df['gender']=='M') & (df['position']=='DCM')].counts),
            name='Male',
            visible=False,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='DCM')].year),
            y=list(df[(df['gender']=='F') & (df['position']=='DCM')].counts),
            name='Female',
            visible=False,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='M') & (df['position']=='MoS')].year),
            y=list(df[(df['gender']=='M') & (df['position']=='MoS')].counts),
            name='Male',
            visible=False,
            marker=dict(
                color='#2A8B8E',
                line=dict(
                    color='#2A8B8E'))))

fig.add_trace(
     go.Bar(x=list(df[(df['gender']=='F') & (df['position']=='MoS')].year),
            y=list(df[(df['gender']=='F') & (df['position']=='MoS')].counts),
            name='Female',
            visible=False,
            marker=dict(
                color='#D8F0F0',
                line=dict(
                    color='#D8F0F0'))))

fig.update_layout(
    title_text="Gender Representation Across Ranks",
    barmode='stack',
    bargap=0.45,
    yaxis=dict(range=[0,90]),
    xaxis=dict(range=[1947,2020]),
    plot_bgcolor= '#444444',
    height = 600,
    width =1200,
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True,True,False,False,False,False,False,False,False,False,False,False]},
                           {"title": "Gender Distribution"}]),

                dict(label="Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,True,True,False,False,False,False,False,False,False,False]},
                           {"title": "Prime Minister Rank: by Gender"}]),

                dict(label="Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,True,True,False,False,False,False,False,False]},
                           {"title": "Cabinet Minister Rank: by Gender"}]),
                dict(label="Deputy Prime Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,True,True,False,False,False,False]},
                           {"title": "Deputy Prime Minister Rank: by Gender"}]),
                dict(label="Deputy Cabinet Minister",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,True,True,False,False]},
                           {"title": "Deputy Cabinet Minister Rank: by Gender"}]),


                dict(label="Minister of State",
                     method="update",
                     args=[{"visible": [False,False,False,False,False,False,False,False,False,False,True,True]},
                           {"title": "Minister of State Rank: by Gender"}])
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
# Set title
fig.update_layout(title_text=" Gender Representation Across Ranks")

fig.show()

import plotly.offline.offline
print(plotly.offline.plot(fig, include_plotlyjs=False, output_type='div'))

