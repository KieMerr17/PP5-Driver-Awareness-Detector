import streamlit as st 
from app_pages.multipage import MultiPage

# Import from the functions from each page to be shown on the dashboard
from app_pages.page_one_summary import page_one_content
from app_pages.page_two_data_visualisation import page_two_content


# App name
app = MultiPage(app_name= "Driver Awareness Detector")

# page names and functions to be imported
app.add_page("Project Summary", page_one_content)
app.add_page("Data Visualisation", page_two_content)



app.run()