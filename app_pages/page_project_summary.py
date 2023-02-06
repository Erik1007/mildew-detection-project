import streamlit as st
import matplotlib.pyplot as plt 

def page_project_summary_body():

    st.write("## Project Summary Overview")

    st.info(### General Information:
        f"Cherry Leaves are an intergral ingrediant found in numerous products world wide, making them a big business "
        f"Depending on how they are used, the Cherry Leaves can be found in anything from Tea, to skin care products "
        f"to over the counter vitamens and even used medicanally to help boost testosterone and clense the liver "
        f"However, as a naturally growing product, Cherry Trees and the leaves are subject to fungal infections, such as "
        f"Powdery Mildew. According to [Wikipwedia](https://en.wikipedia.org/wiki/Powdery_mildew), the ascomycete fungi "
        f"attacks and infects the lower leaves in more humid climates with devestating effects on the life of the  "
        f"host plant reducing plant harvest and other future harm. The fungi spores spread with air movement making it   "
        f"vital to quickly identify infected leaves and treat them preventing the infection from causing further damage"
    )

    if st.checkbox("### Problem Statement:"):
        st.info(
            f"Farmy and Foods agricultural plantation has recently discovered Powdery Mildew infecitons in some of "
            f"their Cherry Trees. The Cherry Leaves production is one of their largest portfolio assets and there "
            f"can be a large financial short term and long term to a variety of thier crops if the infection is not "
            f"identified and prevented quickly. With conventional means, there is a large labor cost in time and resources "
            f"to identify infected leaves. Farmy and Foods requires a new method to quickly identify infected leaves "
            f"from healthy leaves in order to save time and labor to treat the trees, save the harvest and protect the "
            f"company's bottom line."
        )

    st.info(
        f""
    )
    )