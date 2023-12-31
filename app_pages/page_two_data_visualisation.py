import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def page_two_content():
    st.write("### Awareness Visualisation")
    st.info(
        "To fulfill the first business requirement, we have developed a visualisation technique capable of distinguishing "
        "between a drivers eyes which are aware and open and that of eyes which are closed."
    )

    version = 'v1'
    if st.checkbox("Difference between average images from each set and the variability across those images"):

        avg_eyes_open = plt.imread(f"outputs/{version}/avg_var_eyes_open.png")
        avg_eyes_closed = plt.imread(f"outputs/{version}/avg_var_eyes_closed.png")

        st.warning(
            "*The average and variability images didn't show obvious "
            "patterns where it was clear to differentiate one to another. "
            "However, eyes_closed images did show more white in the centre of the images")
        
        st.image(avg_eyes_open, caption="Eyes Open: Average and Variability")
        st.image(avg_eyes_closed, caption="Eyes Closed: Average and Variability")
        st.write("---")