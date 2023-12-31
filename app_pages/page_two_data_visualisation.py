import streamlit as st
import os
import matplotlib.pyplot as plt


def page_two_content():
    #description for the page
    st.write("### Awareness Visualisation")
    st.info(
        "To fulfill the first business requirement, we have developed a visualisation technique capable of distinguishing "
        "between a drivers eyes which are aware and open and that of eyes which are closed."
    )

    # select version folder
    version = 'v1'

    # average and variability
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

    # difference between average images
    if st.checkbox("Differences between average 'Eyes Open' image, and 'Eyes Closed' image."):

        diff_between_avgs = plt.imread(f'outputs/{version}/avg_diff.png')

        st.warning(
            f"We notice this study didn't show patters where we could intuitavely"
            f" differentiate between eyes_open and eyes_closed")

        st.image(diff_between_avgs, caption="Difference between average images for eyes_open and eyes_closed")

    # image montage
    if st.checkbox("Image Montage"):

        # select folder and identify labels
        my_data_dir = 'inputs/awareness'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Please select an option", options=labels, index=0)

        if st.button("View Montage"):
            montage = plt.imread(f'outputs/{label_to_display}Montage.png')
            st.image(montage)
        st.write("---")