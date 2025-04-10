# TensorFlow Linear Regression Examples

This repository contains simple TensorFlow examples demonstrating linear regression models. The code showcases how to create, train, and use basic neural networks to learn simple mathematical relationships.

## Overview

The code implements two separate linear regression models:
1. A model that learns the function y = 2x
2. A model that learns the function y = x + 10

Each model is trained using a simple neural network with one input and one output layer.

## Requirements

- Python 3.11.x (note: Tensorflow isn't supported for Python versions 3.12 and higher at this time)
- TensorFlow

## Installation

1. Clone this repository.
2. (Optional but highly recommended) Create and activate a Python3 virtual environment.
3. Install the required packages:
```bash
source install-project-dependencies.sh
```
1. Validate whether all dependencies have been installed successfully:
```bash
python3 validate-tensorflow-install.py
```

## Code Structure

The code is organized into several functions:

- `create_and_compile_model()`: Creates and compiles a simple neural network model
- `define_data_two_times_x()`: Generates training data for y = 2x
- `define_data_x_plus_10()`: Generates training data for y = x + 10
- `main()`: Executes the training and prediction for both models

## Usage

Run the script directly:
```bash
python3 hello-tensorflow.py
```

The script will:
1. Train the first model to learn y = 2x
2. Make a prediction for x = 6.0 (expected output: 12.0)
3. Train the second model to learn y = x + 10
4. Make a prediction for x = 15.0 (expected output: 25.0)

## Model Architecture

Each model consists of:
- Input layer with shape (1,)
- Dense layer with 1 unit
- SGD optimizer
- Mean squared error loss function

## Training

Both models are trained for 500 epochs using stochastic gradient descent (SGD) as the optimizer. The training is performed silently (verbose=0).

## Expected Output

When running the script, you should see two predictions:
1. A prediction close to 12.0 for the first model
2. A prediction close to 25.0 for the second model

Note: Due to the stochastic nature of neural networks, the exact values may vary slightly between runs. 