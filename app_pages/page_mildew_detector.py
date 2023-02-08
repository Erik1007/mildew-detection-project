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

def upload_and_predict(images_buffer):
    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaf Sample Image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)

        
