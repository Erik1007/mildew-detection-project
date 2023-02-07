********************
# Mildew Detection in Cherry Leaves
********************


********************
## Table of Contents:
1. [Introduction](#Introduction)
2. [Business Requirements](#Business-Requirements)
3. [Hypothesis and Validation](#Hypothesis-and-Validation)
4. [ML Task Rationale](#ML-Task-Rationale)
5. [ML Business Case](#ML-Business-Case)
6. [Dashboard Design](#Dashboard-Design)
7. [Unfixed Bugs](#Unfixed-Bugs)
8. [Deployment](#Deployment)
9. [Data Analysis and Machine Learning Libraries](#Data-Analysis-and-Machine-Learning-Libraries)
10. [Credits](#Credits)
11. [Acknowledgements](#Acknowledgements)
********************



********************
## Introduction
********************


This project is to facilitate the means to create a Data Analysis Machine Learning Tool that can accuratly determine if an upladed image of a Cherry Leafe contains a healthy Cherry Leaf or one infected with a powedery Mildew.



********************
## Business Requirements
********************
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.



********************
## Hypothesis and Validation
********************

* 1 - Cherry Leaves infected with powdery mildew have white blotches, streaks and surface making them appear
differently than healthy Cherry leaves

* 2 - The ML image visualizer will be able to differentiate between a healthy cherry leafe and an infected cherry leaf with at least 97% accuracy.

* 3 - The ML image visualizer can help decrease the amount of time needed to differentiate between the images thereby saving the employee and company both time and money during the inspection process.

* 4 - Validation of the image visualizer will come from the the ML pipline performance of the validation and test set differentiating between an infected leaf and and a healthy leaf with at least 97% accuracy.



********************
## ML Task Rationale
********************

* 1 - The company requires a ML data visualization tool to efficiently and accuratly determine a healthy cherry leaf from an infected cherry leaf. 

* 2 - The company requires a data visualization tool that can be used widespread through the company in order to save employee time, and company resources. 

* 3 - The company will benefit by saving time, money, resources and ultimately by increasing the amount of healthy produc to the market, thereby increasing the amount of revenue brought into the company.



********************
## ML Business Case
********************

* 1 - The business objective: Devising a method/tool to increase accuracy and efficency evaluating a leaf infected with powedery mildew from a healthy leaf.

* 2 - The Customer requires a dashboard containing the ability to upload images of leaves for the machine to quickly determine if the image of the leaf is contains a healthy or a leaf infected with powdery mildew with 97% accuracy.

* 3 - The Customer requires for propietary reasons that thier internal data remains secret so as to not give the competition the ability to match the production of cherry leaves delivered to the market.

* 4 - The inputs are images of both healthy and infected cherry leaves that will be used to train the ML tool to learn the difference and the expected output is a ML tool that with an accuracy of 97% determines if the uploaded image shows a healthy or infected leaf.

* 5 - Conventional data analysis can be used to visually inspect and differentiate the images of the leaves to determine if the image contains a healthy leaf or one infected with powdery mildew.


********************
## Dashboard Design
********************

* 1 - A project summary page, showing the project dataset summary and the client's requirements.

* 2 - A page listing your findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew

* 3 - A page containing:

        - A link to download a set of cherry leaf images for live prediction (you may use the Kaggle repository that was provided to you).

        - A User Interface with a file uploader widget. The user should have the capacity to upload multiple images. For each image, it will display the image and a prediction statement, indicating if a cherry leaf is healthy or contains powdery mildew and the probability associated with this statement.

        - A table with the image name and prediction results, and a download button to download the table.

* 4 - A page indicating your project hypothesis and how you validated it across the project.

* 5 - A technical page displaying your model performance.

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


********************
## Unfixed Bugs
********************

* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.


********************
## Deployment
********************


### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Gitpod Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

********************
## Data Analysis and Machine Learning Libraries
********************


* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.

********************
## Credits 
********************


- Assistance and support for this project came in two main groups: **content** and **data/images**. Below, youll find sitings for both groups and links to each source:

********************
### Content 

* [Code Institute Malaria Walk Through Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/) was heavily used for instructional purposes, and guidance through the development of this project.

* [Streamlit](https://docs.streamlit.io/library/api-reference/write-magic/st.write) documentation was used for assistance in the writting the app pages

* [Code Institute Streamlit lessons](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/fc2f9892cfa44eee9cc8bf585c21df88/4?activate_block_id=block-v1%3Acode_institute%2BCI_DA_ML%2B2021_Q4%2Btype%40vertical%2Bblock%407636b337caeb4035bd7b5568404802f6) was used as guidance for the dashboard execution in this project.

* [GyanShashwat1611/WalkthroughProject01](https://github.com/GyanShashwat1611/WalkthroughProject01) github repository was used for code reference and assistance for in the jupyter notebook set up, code and execution; as well as for the app pages design, set up and code

* [valerieoni/mildew-detection](https://github.com/valerieoni/mildew-detection) github repository was used for readme guidance and code reference. 

* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

********************
### Dataset / Media

* [Kaggle Cheery Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) was used as the source for the data set and the images for this project

* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. 



********************
## Acknowledgements
* I would like to thank my mentor **Marcel Mulders** for his time, help, expertise and especially for his motivation during the creation and execution of this project.
