import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class= pd.DataFrame(
            data=[0,0],
            index={'eyes open': 0, 'eyes closed': 1}.keys(),
            columns=['Probability']
        )
    prob_per_class.loc[pred_class] = pred_proba

    for x in prob_per_class.index.to_list():
        if x not in pred_class: 
            prob_per_class.loc[x] = 1 - pred_proba

    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y = [0,1],
            width=600, height=300, template='seaborn')

    st.plotly_chart(fig)


def resize_input_image(img, version):  
    """
    Check if image is Greyscale or Colour
    Reshape image to the average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]))

    # Check if the image is grayscale
    if len(img_resized.getbands()) == 1:
        # Convert to RGB to have 3 channels
        img_resized = img_resized.convert("RGB")
        img_array = np.array(img_resized)
        my_image = np.expand_dims(img_array, axis=0) / 255
    else:
        my_image = np.expand_dims(np.array(img_resized), axis=0) / 255

    # Check if the image has 4 channels and convert to 3 channels
    if img_resized.mode == 'RGBA':
        img_resized = img_resized.convert("RGB")

    img_array = np.array(img_resized)
    my_image = np.expand_dims(img_array, axis=0) / 255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and make prediction on the uploaded image
    """

    model = load_model(f"outputs/{version}/driver_awareness_detector.h5")

    pred_proba = model.predict(my_image)[0,0]

    target_map = {v: k for k, v in {'eyes closed': 0, 'eyes open': 1}.items()}

    pred_class =  target_map[pred_proba > 0.5]  

    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        "The prodiction given for the image uploaded is: "
        f"**{pred_class.lower()}**.")

    return pred_proba, pred_class