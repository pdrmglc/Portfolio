#Import the required Libraries
import streamlit as st
import io
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


st.set_page_config(layout="wide")


# Functions for each of the pages
def home(uploaded_file):

    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())


def displayplot():
    st.header('Plot of Data')
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    color = st.color_picker('Pick A Color', '#00f900')

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=color))
    st.plotly_chart(plot, use_container_width=True)

    buffer = io.StringIO()
    plot.write_html(buffer, include_plotlyjs='cdn')
    html_bytes = buffer.getvalue().encode()

    st.download_button(
        label='Download HTML',
        data=html_bytes,
        file_name='stuff.html',
        mime='text/html'
    )


st.image("imagens/logo.png")
# Add a title and intro text
st.title('Programming-Enhanced Graphs Automation and Statistics Utility System')
st.text('This is a web app to allow exploration of data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing your data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Scatter Plot'])

upload = False
# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)
    upload = True

def upload_message():
    st.header(":red[**Upload a file first!**]")

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    if upload:
        data_summary()
    else:
        upload_message()
elif options == 'Data Header':
    if upload:
        data_header()
    else:
        upload_message()
elif options == 'Scatter Plot':
    if upload:
        displayplot()
    else:
        upload_message()