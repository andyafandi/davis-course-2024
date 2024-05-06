import plotly.graph_objs as go
import plotly.express as px
import streamlit as st
# import dash
# from dash import dcc
# # from dash import dhc as html
# # import dash_core_components as dcc
# import dash_html_components as html
import streamlit.components.v1 as components
data_company = ["PT A", "PT B", "PT C"]
choice = st.sidebar.selectbox(
                "Select Company Name", 
                range(1,  len(data_company)+1) ,
                format_func=lambda x: data_company,
                key="selectbox"
            )
# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=200,
)

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 15, 13, 17, 20]

st.write('Hello, *World!* :sunglasses:')
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
