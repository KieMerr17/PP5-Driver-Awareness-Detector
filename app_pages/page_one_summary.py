import streamlit as st

def page_one_content():

    st.write("### Project Summary ###")

    st.success(
        "##### Project General Information\n\n"
        "Tiredness poses a considerable threat to driver safety, compromising the driver's ability to remain "
        "focused, and respond rapidly while on the road. This issue commonly occurs during extended driving periods or in "
        "monotonous scenarios, such as nighttime driving or on lengthy, straight motorways. "
        "Identifying signs of tiredness in drivers is important for accident prevention and preserving lives, because driving while fatigued "
        "can result in severe and tragic outcomes."
    )
    st.info(
        "##### Project Dataset #####\n\n"
        "The dataset used for the project shows greyscale images of singular eye open and eye closed images with a small amount of surrounding features. "
        "It uses 48,000 images split evenly into 2 sets, 'eyes open', 'eyes closed'.\n\n"
        "The dataset can be found here:\n\n "
        "https://www.kaggle.com/datasets/kutaykutlu/drowsiness-detection"
    )
    st.warning(
        "##### Business Requirements #####\n\n"
        "This project has three critical Business Requirements:\n\n"
        "- A visual identification of a drivers awareness \n\n "
        "- An accurate prediction of a driver awareness \n\n "
        "- Create downloadable reports based on these predictions.\n\n "
        "The successful completion of these requirements will serve as a proof of concept, paving the way for further development. "
        "The ultimate objective is to establish a machine learning system capable of detecting a drivers awareness."
        )