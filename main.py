#!/usr/bin/env python3

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd


df = pd.read_csv("SkillCraft1_Dataset.csv")

data = [
    go.Parcoords(
        line=dict(color=df['LeagueIndex'],
                  colorscale=[[0, '#00FF00'],
                              [0.5, '#0000FF'],
                              [1.0, '#FF0000']]),

        dimensions=list([
            dict(range=[1, 7],
                 label='League',
                 values=df['LeagueIndex']),
            dict(range=[0, 500],
                 constraintrange=[50, 500],
                 label='APM',
                 values=df['APM']),
            dict(range=[0, 25000],
                 label='Total Hours',
                 values=df['TotalHours']),
            dict(range=[0, 130],
                 label='Hours per week',
                 values=df['HoursPerWeek']),
            dict(range=[0, 0.05],
                 label='Select by hotkeys',
                 values=df['SelectByHotkeys']),
            dict(range=[0, 0.01],
                 label='Number of PACs',
                 values=df['NumberOfPACs']),
        ])
    )
]

layout = go.Layout(
    plot_bgcolor='#E5E5E5',
    paper_bgcolor='#E5E5E5'
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='parcoords-basic')
