# LSTM Wind Speed Prediction Documentation


## Overview
This document provides an overview and explanation of the code designed to train an LSTM (Long Short-Term Memory) model to predict wind speed based on historical data.

## Table of Contents
1. [﻿Introduction](https://#introduction) 
2. [﻿Data Requirements](https://#data-requirements) 
3. [﻿Code Explanation](https://#code-explanation) 
    - [﻿Data Loading and Preparation](https://#data-loading-and-preparation) 
    - [﻿Feature Creation](https://#feature-creation) 
    - [﻿Data Scaling](https://#data-scaling) 
    - [﻿Model Training](https://#model-training) 
    - [﻿Prediction and Visualization](https://#prediction-and-visualization) 
4. [﻿Output](https://#output) 
5. [﻿Conclusion](https://#conclusion) 
## Introduction
The primary purpose of this code is to predict wind speed using an LSTM model. The model is trained on historical wind speed data to forecast future values.

## Data Requirements
- **Input CSV File Structure**:
    - **Station ID**: Unique identifier for the weather station.
    - **Location**: Geographical location of the station.
    - **Date**: Date of the recorded wind speed.
    - **Wind Speed**: Recorded wind speed (in km/h or mph).
## Code Explanation
### Data Loading and Preparation
- The code reads the CSV file using Pandas.
- It extracts the wind speed values from the 4th column.
- A plot is generated to visualize wind speed variations over time.
### Feature Creation
- Three input features (X1, X2, X3) are created by shifting the wind speed data.
- Each prediction is based on the wind speeds of the previous three days.
### Data Scaling
- Both input features and target values are scaled to a range between 0 and 1 using MinMaxScaler.
### Model Training
- An LSTM model is defined using the Sequential API.
- The model is trained on 80% of the data for 25 epochs.
- The loss for each epoch is displayed during training.
### Prediction and Visualization
- The model makes predictions on the test set (20% of data).
- Two plots are generated:
    - **Scatter Plot**: Compares actual vs. predicted wind speed values.
    - **Line Plot**: Shows actual and predicted wind speed over time.
## Output
- **Scatter Plot**: Visualizes the accuracy of predictions against actual values.
- **Line Plot**: Illustrates how well the model captures trends and fluctuations in wind speed.
## Conclusion
The final output allows for a visual assessment of the LSTM model's performance in predicting wind speeds based on historical data. A successful model will have predictions closely following actual values in the line plot and points clustering around a diagonal line in the scatter plot.

