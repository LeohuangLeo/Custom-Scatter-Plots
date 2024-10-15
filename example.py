# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import subprocess

# # Sample data for two scatter plots
# x1 = np.random.rand(10)
# y1 = np.random.rand(10)
# file_paths1 = [
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg"
# ]

# x2 = np.random.rand(10)
# y2 = np.random.rand(10)
# file_paths2 = [
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
#     r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg"
# ]

# # Create subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# # Create scatter plots
# sc1 = ax1.scatter(x1, y1)
# sc2 = ax2.scatter(x2, y2)

# # Function to handle clicks
# def on_click(event):
#     # Check if the click was inside any axes
#     if event.inaxes is not None:
#         # Get the clicked point coordinates
#         x_click, y_click = event.xdata, event.ydata
        
#         # Determine which scatter plot was clicked
#         if event.inaxes == ax1:
#             x_data, y_data, file_paths = x1, y1, file_paths1
#         elif event.inaxes == ax2:
#             x_data, y_data, file_paths = x2, y2, file_paths2
#         else:
#             return
        
#         # Find the closest point
#         distances = np.sqrt((x_data - x_click)**2 + (y_data - y_click)**2)
#         closest_index = np.argmin(distances)

#         # Open the file corresponding to the closest point
#         file_path = file_paths[closest_index]
        
#         # Open the file with the default application
#         if os.path.exists(file_path):
#             subprocess.run(["open", file_path])  # Use subprocess to open the file
#         else:
#             print(f"File does not exist: {file_path}")

# # Connect the click event to the handler
# cid = fig.canvas.mpl_connect('button_press_event', on_click)

# plt.show()






import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import os
import subprocess
import sys

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # Expose the server variable for deployments

# Sample data for two scatter plots
df1 = pd.DataFrame({
    'x': [0.1, 0.4, 0.3, 0.7, 0.6, 0.2, 0.9, 0.5, 0.8, 0.3],
    'y': [0.2, 0.5, 0.4, 0.8, 0.7, 0.3, 0.9, 0.6, 0.85, 0.35],
    'file_path': [
        r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
        r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
        r"/Users/ting-lianghuang/Desktop/leo/Picture:Video/TWSA_logo.jpg",
        r"/Users/your_username/Desktop/file4.jpg",
        r"/Users/your_username/Desktop/file5.jpg",
        r"/Users/your_username/Desktop/file6.jpg",
        r"/Users/your_username/Desktop/file7.jpg",
        r"/Users/your_username/Desktop/file8.jpg",
        r"/Users/your_username/Desktop/file9.jpg",
        r"/Users/your_username/Desktop/file10.jpg"
    ]
})

df2 = pd.DataFrame({
    'x': [0.15, 0.45, 0.35, 0.75, 0.65, 0.25, 0.95, 0.55, 0.85, 0.35],
    'y': [0.25, 0.55, 0.45, 0.85, 0.75, 0.35, 0.95, 0.65, 0.9, 0.4],
    'file_path': [
        r"/Users/your_username/Desktop/file11.jpg",
        r"/Users/your_username/Desktop/file12.jpg",
        r"/Users/your_username/Desktop/file13.jpg",
        r"/Users/your_username/Desktop/file14.jpg",
        r"/Users/your_username/Desktop/file15.jpg",
        r"/Users/your_username/Desktop/file16.jpg",
        r"/Users/your_username/Desktop/file17.jpg",
        r"/Users/your_username/Desktop/file18.jpg",
        r"/Users/your_username/Desktop/file19.jpg",
        r"/Users/your_username/Desktop/file20.jpg"
    ]
})

# Define the layout of the app
app.layout = html.Div([
    html.H1("Interactive Scatter Plots with File Opening", style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(
            id='scatter-plot-1',
            figure={
                'data': [
                    go.Scatter(
                        x=df1['x'],
                        y=df1['y'],
                        mode='markers',
                        marker={'size': 12, 'color': 'blue'},
                        name='Scatter Plot 1',
                        customdata=df1['file_path'],  # Attach file paths to points
                        hoverinfo='text',
                        hovertext=df1['file_path']
                    )
                ],
                'layout': go.Layout(
                    title='Scatter Plot 1',
                    clickmode='event+select',
                    xaxis={'title': 'X Axis'},
                    yaxis={'title': 'Y Axis'},
                    # yaxis={'title': '(X,Y)'},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='scatter-plot-2',
            figure={
                'data': [
                    go.Scatter(
                        x=df2['x'],
                        y=df2['y'],
                        mode='markers',
                        marker={'size': 12, 'color': 'red'},
                        name='Scatter Plot 2',
                        customdata=df2['file_path'],  # Attach file paths to points
                        hoverinfo='text',
                        hovertext=df2['file_path']
                    )
                ],
                'layout': go.Layout(
                    title='Scatter Plot 2',
                    clickmode='event+select',
                    # xaxis={'title': 'X Axis'},
                    # yaxis={'title': 'Y Axis'},
                    hovermode='closest'
                )
            }
        ),
        html.P('(X,Y)', style = {"width": "300pt", "height": "300pt", "top": "150pt", "position": "relative"})
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),
    html.Div([
        dcc.Graph(
            id='scatter-plot-1',
            figure={
                'data': [
                    go.Scatter(
                        x=df1['x'],
                        y=df1['y'],
                        mode='markers',
                        marker={'size': 12, 'color': 'blue'},
                        name='Scatter Plot 1',
                        customdata=df1['file_path'],  # Attach file paths to points
                        hoverinfo='text',
                        hovertext=df1['file_path']
                    )
                ],
                'layout': go.Layout(
                    # title='Scatter Plot 1',
                    clickmode='event+select',
                    # xaxis={'title': 'X Axis'},
                    # yaxis={'title': 'Y Axis'},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='scatter-plot-2',
            figure={
                'data': [
                    go.Scatter(
                        x=df2['x'],
                        y=df2['y'],
                        mode='markers',
                        marker={'size': 12, 'color': 'red'},
                        name='Scatter Plot 2',
                        customdata=df2['file_path'],  # Attach file paths to points
                        hoverinfo='text',
                        hovertext=df2['file_path']
                    )
                ],
                'layout': go.Layout(
                    # title='Scatter Plot 2',
                    clickmode='event+select',
                    # xaxis={'title': 'X Axis'},
                    # yaxis={'title': 'Y Axis'},
                    hovermode='closest'
                )
            }
        )
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),
    # Hidden Div to store the clicked file path (optional)
    html.Div(id='output-file-path', style={'display': 'none'})
])

# Callback to handle clicks on Scatter Plot 1 and Scatter Plot 2
@app.callback(
    Output('output-file-path', 'children'),
    [Input('scatter-plot-1', 'clickData'),
     Input('scatter-plot-2', 'clickData')]
)
def open_file(click1, click2):
    # Determine which plot was clicked
    if click1:
        file_path = click1['points'][0]['customdata']
    elif click2:
        file_path = click2['points'][0]['customdata']
    else:
        return ''

    # Attempt to open the file
    if os.path.exists(file_path):
        try:
            if sys.platform.startswith('darwin'):
                subprocess.run(['open', file_path])
            elif os.name == 'nt':
                os.startfile(file_path)
            elif os.name == 'posix':
                subprocess.run(['xdg-open', file_path])
            else:
                print(f"Unsupported OS: Cannot open file {file_path}")
        except Exception as e:
            print(f"Error opening file {file_path}: {e}")
    else:
        print(f"File does not exist: {file_path}")

    return file_path  # Not used, but required by the callback

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)