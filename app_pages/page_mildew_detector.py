import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    make_prediction,
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_mildew_detector_body():

    st.header("Mildew Detector")
    st.info(
        f"The Client is interested in predicting wether or not a cherry leaf"
        f" contains powdery mildew"
    )
    st.write('---')

    st.write("Upload images for a prediction and clcik the **Make Prediction** button for results")
    btn_predict = st.button("Make Prediction")
    images_buffer = st.file_uploader(
        'Upload Cherry leaf samples. You may select more than one.',
        type='JPG', accept_multiple_files=True)

    if btn_predict:
        upload_and_predict(images_buffer)

        
