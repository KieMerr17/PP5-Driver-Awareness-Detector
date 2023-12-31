import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd


def page_three_content():

    st.info(
        "To acheive the business requirement, you can upload a picture of a drivers eyes and detect their awareness. "
        "It will identify if the image displays a drivers eyes as 'eyes open' or 'eyes closed'."
    )

    st.write(
        "Images used to train the model can be found "
        "[here](https://www.kaggle.com/datasets/kutaykutlu/drowsiness-detection)."
    )

    st.write(
        "---"
    )

    st.write(
        "**Upload your image below, you may select multiple images**"
    )

    image_buffer = st.file_uploader('', type='jpeg', accept_multiple_files=True)

    