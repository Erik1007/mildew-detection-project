import streamlit as st 


def page_project_hypoothesis_body():

    st.write(## Mildew Detection in Cherry Leaves Hypothesis)

    st.info(
        f"There are 4 main hypotheses for this project: "

        f"1 - Cherry Leaves infected with powdery mildew have white blotches, streaks and surface making them "
        f"    appear differently than healthy Cherry leaves." 
        f"2 - The ML image visualizer will be able to differentiate between a healthy cherry leafe and an "
        f"    infected cherry leaf with at least 97% accuracy."
        f"3 - The ML image visualizer can help decrease the amount of time needed to differentiate between "
        f"    the images thereby saving the employee and company both time and money during the inspection process."
        f"4 - Validation of the image visualizer will come from the the ML pipline performance of the validation "
        f"    and test set differentiating between an infected leaf and and a healthy leaf with at least 97% accuracy."
    )

    st.info(
        f"Images of healthy leaves will present darker green colors, while infected leaves will present lighter "
        f"colors, white streaks, white blotches and white fuzzy surfaces"
        f"The ML image validator will differentiate between a healthy Cherry Leaf and an infected leaf"
        f"The ML image validator will prove to be at least 97% accurate in the training, validating and testing trials."
        f""
    )