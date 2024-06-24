# Wine Predictor

This repository contains a machine learning application designed to classify wines based on their chemical properties using the K-Nearest Neighbors (KNN) algorithm. The dataset used for this project contains 13 features for wines grown in the same region in Italy, derived from three different cultivars.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Steps](#steps)
- [Accuracy](#accuracy)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to classify wines into three categories based on their chemical properties using a machine learning classification technique. We use the K-Nearest Neighbors (KNN) algorithm to build our classifier.

## Dataset

The dataset (`WinePredictor.csv`) consists of the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The dataset includes 13 different features for each wine sample.

## Features

The dataset includes the following features:

1. Alcohol
2. Malic acid
3. Ash
4. Alcalinity of ash
5. Magnesium
6. Total phenols
7. Flavanoids
8. Nonflavanoid phenols
9. Proanthocyanins
10. Color intensity
11. Hue
12. OD280/OD315 of diluted wines
13. Proline

Based on these features, the wines can be classified into three classes:

- Class 1
- Class 2
- Class 3

## Installation

1. Clone the repository:
   \`\`\`sh
   git clone https://github.com/Mahesh-Pawar-02/Python-Assignment-15.git
   \`\`\`
2. Navigate to the project directory:
   \`\`\`sh
   cd WinePredictor
   \`\`\`
3. Install the required dependencies:
   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

## Usage

1. Ensure that `WinePredictor.csv` is in the project directory.
2. Run the script:
   
   python WinePredictor.py

## Steps

The application follows these steps:

1. **Get Data**: Load data from `WinePredictor.csv`.
2. **Clean, Prepare, and Manipulate Data**: Prepare the data in a format suitable for the algorithm.
3. **Train Data**: Use the K-Nearest Neighbors (KNN) algorithm with K=3. Train the model using 70% of the dataset.
4. **Test Data**: Test the model using the remaining 30% of the dataset. Display the classification result.
5. **Calculate Accuracy**: Calculate the accuracy of the model using the `CheckAccuracy` function. The dataset is divided into training and testing data to evaluate the accuracy for different values of K.

## Accuracy

The accuracy of the KNN model is calculated by dividing the dataset into training and testing sets and evaluating the model's performance for different values of K.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your changes or suggestions.

------------------------------------------------Thank You------------------------------------------------
