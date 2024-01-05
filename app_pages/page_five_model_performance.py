import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_five_content():
    
    version = 'v1'

    st.write(
        "This page presents a clear and visual representation of how the data has been"
        "divided and the shows the model's performance."
        )

    st.write("### Image Labels Distribution ###")

    st.warning(
        "The complete dataset was partitioned into three subsets:\n\n"
        "1. Training set (70% of the dataset): This comprises the initial data employed to 'fit' or train the model.\n\n"
        "2. Validation set (10% of the dataset): This assists in refining the model's performance through fine-tuning after each epoch.\n\n"
        "3. Test set (20% of the dataset): This reveals the final accuracy of the model after the training phase."
        )
    st.write("---")

    label_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(label_distribution, caption='Label Distribution for Train, Validation, and Test Sets')

    