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
    st.write("---")



    st.write("### Model Performance ###")

    st.write("##### Accuracy and Val_Accuracy #####")
    st.warning(
        "Accuracy serves as a metric to assess the overall correctness of the model's predictions against "
        "the true labels in the dataset. It is calculated as the ratio of correct predictions to the total number of predictions made by the model.\n\n"
        "During the model training process, a variant of accuracy known as validation accuracy (val_accuracy) is often used. "
        "In machine learning, it is customary to divide the dataset into training and validation sets. \n\n"
        "The training set is employed for model training, while the validation set is used to evaluate the model's "
        "performance throughout the training phase."
    )

    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')
    st.write("---")

    