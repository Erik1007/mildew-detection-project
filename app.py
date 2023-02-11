import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_project_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.leaf_visualizer import page_leaf_visualizer_body
from app_pages.performance import page_performance_body
from app_pages.mildew_detector import page_mildew_detection_page

app = MultiPage(app_name = "Mildew-Detection-Project")

app.add_page("Project Summary", page_project_summary_body)
app.add_page("Cherry Leaf Visualizer", page_leaves_visualizer_body)
app.add_page('Mildew Detector', page_mildew_detector_body)
app.add_page("Hypothesis and Visualization", page_project_hypothesis_body)
app.add_page('ML Performance Metric', page_ml_performance_body)

app.run()