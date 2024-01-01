import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# import functions from src folder
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )


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
        "**Please upload your image below, you may select multiple images**"
    )

    image_buffer = st.file_uploader('', type='png', accept_multiple_files=True)

    if image_buffer is not None:

        df_report = pd.DataFrame([])

        for image in image_buffer:

            img_pil = (Image.open(image))
            # Inform of the image being tested
            st.info(f"Image to be analysed is: **{image.name}**")

            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'

            # Pull the resized image details
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = pd.concat([df_report,
                                    pd.DataFrame({"Image name": [image.name], 
                                                'Image result': [pred_class]})],
                                                ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)