# Boat Type Classification Project

This project focuses on building and evaluating image classification models to identify different types of boats from the provided dataset.

## Project Goal

The objective is to train and compare two image classification models:

1. A baseline convolutional neural network (CNN)
2. A transfer-learning model using MobileNetV2

The implementation is contained in the notebook file named boat_classification_notebook_template.ipynb.

## Project Requirements Alignment

The notebook and workflow are structured to follow the assignment requirements for this project:

- Classify 9 boat categories from the provided dataset.
- Use a CNN baseline model.
- Use transfer learning with a lightweight pretrained model, specifically MobileNetV2.
- Evaluate both models using classification metrics and confusion-matrix-based analysis.
- Follow a reproducible data-splitting approach with fixed random seeds.

## Data Analysis and Preparation

### Dataset Overview
- The dataset contains images for 9 boat classes.
- The images are stored in class-specific folders.
- The workflow loads the images from the dataset directory and organizes them into training, validation, and test subsets.

### Data Split Strategy
- For the CNN workflow, the data is split into train, validation, and test subsets using a reproducible split with random state 43.
- For the transfer-learning workflow, the data is split into train, validation, and test subsets using a reproducible split with random state 1.
- The image datasets are loaded with TensorFlow’s image_dataset_from_directory function.
- Images are normalized to the range 0 to 1 using a scale factor of 1/255.
- Data is loaded in batches of 32.

### Analysis Focus
The data preparation step is designed to support proper model evaluation by:
- preventing leakage between training and evaluation data,
- using separate validation data during training,
- using a distinct test set for final evaluation,
- keeping the workflow consistent with the project requirements.

## Model Workflow

### 1. Baseline CNN
- Builds a simple CNN architecture with convolutional layers, max pooling, global average pooling, and dense layers.
- Compiles the model with Adam optimizer and categorical cross-entropy loss.
- Tracks accuracy, precision, and recall.
- Trains the model for 20 epochs.
- Evaluates performance on the test set.

### 2. Transfer-Learning Model
- Uses MobileNetV2 as the base model.
- Freezes the pretrained base layers and adds a custom classification head.
- Includes dropout and batch normalization layers.
- Compiles the model with Adam optimizer and categorical cross-entropy loss.
- Tracks accuracy, precision, and recall.
- Trains the model for 50 epochs with early stopping based on validation loss.
- Evaluates performance on the test set.

## Evaluation and Results

The notebook includes:
- training and validation loss/accuracy plots,
- confusion matrix visualization,
- classification reports,
- comparison of CNN and transfer-learning results.

The README is intended to reflect the project requirements and the data-analysis workflow used in the notebook rather than to overstate performance without direct evaluation output.

## Summary

This project demonstrates a structured deep-learning workflow for boat image classification, including dataset preparation, baseline CNN modeling, transfer-learning modeling, and evaluation. The notebook is organized to align with the assignment instructions and to support a clear comparison between the two approaches.
