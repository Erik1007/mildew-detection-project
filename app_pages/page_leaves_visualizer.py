import streamlit as st 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import itertools
import random


def page_leaves_visualizer_body():
    st.title("Powdery Mildew Detection in Cherry Leaves")
    st.info(
        f"This page will show the difference between a **healthy** Cherry Leaf "
        f"and one infected with **powdery mildew**.\n\n"
    )