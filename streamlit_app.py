import plotly.graph_objs as go
import plotly.express as px
import streamlit as st
# import dash
# from dash import dcc
# # from dash import dhc as html
# # import dash_core_components as dcc
# import dash_html_components as html

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 15, 13, 17, 20]

st.write('<h1>Hello, *World!* :sunglasses:</>')
# Line chart
line_chart = go.Figure(data=go.Scatter(x=x_data, y=y_data, mode='lines', name='Line Chart'))
# line_chart.show()
st.plotly_chart(line_chart, use_container_width=True)

# Bar chart
bar_chart = go.Figure(data=go.Bar(x=x_data, y=y_data))
# bar_chart.show()
st.plotly_chart(bar_chart, use_container_width=True)

# Scatter plot
scatter_plot = px.scatter(x=x_data, y=y_data, title='Scatter Plot')
# scatter_plot.show()
st.plotly_chart(scatter_plot, use_container_width=True)

# Heatmap
heatmap_data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
heatmap = go.Figure(data=go.Heatmap(z=heatmap_data, colorscale='Viridis'))
# heatmap.show()
st.plotly_chart(heatmap, use_container_width=True)

# Create Dash application
# app = dash.Dash(__name__)

# # Define layout
# app.layout = html.Div(children=[
#     html.H1("Interactive Data Visualization with Plotly and Dash"),
#     dcc.Graph(id='line-chart', figure=line_chart),
#     dcc.Graph(id='bar-chart', figure=bar_chart),
#     dcc.Graph(id='scatter-plot', figure=scatter_plot),
#     dcc.Graph(id='heatmap', figure=heatmap)
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
