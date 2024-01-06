# Driver Awareness Detector

## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)



### Deployed Dashboard [here](https://driver-awareness-detector-cac7971f0415.herokuapp.com/)


## Dataset Content
The dataset used for the project shows greyscale images of singular eye open and eye closed images with a small amount of surrounding features. It uses 48,000 images split evenly into 2 sets, 'eyes open', 'eyes closed'. 

Identifying signs of tiredness in drivers is important for accident prevention and preserving lives, because driving while fatigued can result in severe and tragic outcomes. 

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/kutaykutlu/drowsiness-detection).


## Business Requirements

In response to the escalating incidence of vehicle accidents attributed to tired driving, there is a recognized demand for machine learning sytem. The objective is to demonstrate the capability of machine learning in analyzing human eye movements, specifically focusing on its 'openness' to identify potential signs of driver tiredness. The project encompasses three essential business requirements, A visual identification of a drivers awareness, An accurate prediction of a driver awareness, create downloadable reports based on these predictions.

Successfully meeting these requirements serves as a proof of concept, paving the way for subsequent development. The ultimate aim is to create a real-time video machine learning system for the detection of drowsiness. 

Further details on the business requirements are provided below.

1. Visual Assessment of Driver Awareness

The system will conduct image analysis to visually distinguish between drivers who are alert and those who are not. The focus of this analysis will be on evaluating the 'openness' of the drivers' eyes to identify potential indicators of tiredness.

2. Accurate Prediction of Driver Awareness

The model will be designed as a binary classifier, employing machine learning algorithms and computer vision techniques to precisely predict whether a given driver is starting to show signs of tiredness based on their eye state.

3. Generation of Downloadable Reports

Following the analysis of a driver's eye, the system will generate detailed prediction reports for each examination. These reports will contain information such as the date and time of the examination, the outcome of the prediction, 'Eyes Open' or 'Eyes Closed', and the associated probability. Users will be able to download these reports for reference and further analysis.