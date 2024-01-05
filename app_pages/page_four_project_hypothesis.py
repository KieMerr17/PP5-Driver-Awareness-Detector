import streamlit as st


def page_four_content():
    st.write("### Hypothesis and Conclusion")

    # Hypothesis 1
    st.info(
        "Hypothesis 1:\n\n"
        "It is said that tired drivers may show a higher degree of closed eyes compared to alert drivers. \n\n"
    )

    st.success(
        "Conclusion:\n\n"
        "To validate this hypothesis, we conducted an analysis of the dataset, specifically focusing on the average "
        "degree of eye openness and closedness.\n\n "
        "Using Machine Learning, it was shown that the average degree of eye openness in fatigued drivers is notably "
        "lower than that observed in alert individuals. This observation is reinforced by the examination of both "
        "Average Image and Variability Images, highlighting the distinction between eyes open and eyes closed."
    )

    # Hypothesis 2
    st.info(
        "Hypothesis 2:\n\n"
        "It is said that a machine learning model can discern a visual pattern to classify closed and open eyes with an accuracy surpassing 90%."
    )

    st.success(
        "Conclusion:\n\n"
        "To validate this hypothesis, a machine learning model was trained on the dataset, and its performance was evaluated. "
        "The model achieved an accuracy exceeding 90% on the test set, thereby substantiating the hypothesis."
    )

