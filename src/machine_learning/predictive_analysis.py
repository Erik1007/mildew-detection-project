import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def resize_input_image(img, version):
    """
    Resize image to average image size
    """
    image_shape = load_pickle_file(
        file_name=f"outputs/{version}/image_shape.pk1")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    return np.expand_dims(img_resized, axis=0)/255


def make_prediction(my_image, version):
    """
    Load and perform ML prediction over images provided
    """

    model = load_model(f'outputs/{version}/mildew_detector_model.h5')
    prediction_probability = model.predict(my_image)[0, 0]
    predictions_labels = {'healthy': 0, 'powdery_mildew': 1}

    target_map = {v: k for k, v in predictions_labels.items()}
    predicted_class = target_map[prediction_probability > 0.5]

    if predicted_class == target_map[0]:
        prediction_probability = 1 - prediction_probability

    statement = "Based on predictive analysis, the cherry leaf indicates "

    if predicted_class.lower() == 'healthy':
        statement = f"{statement} as **{predicted_class.lower()}**"
    else:
        statement = f"{statement} as infected with **powdery mildew**."
  
    st.write(statement)
        
    return prediction_probability, predicted_class


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class= pd.DataFrame(
            data=[0,0],
            index={'healthy': 0, 'powdery_mildew': 1}.keys(),
            columns=['Probability']
        )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index
    
    fig = px.bar(
            prob_per_class,
            x = 'Diagnostic',
            y = prob_per_class['Probability'],
            range_y=[0,1],
            width=600, height=300,template='seaborn')
    st.plotly_chart(fig)


