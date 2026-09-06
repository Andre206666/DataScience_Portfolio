# Neural Network - MNIST Digit Recognition 🧠

## Overview
A deep learning neural network built from scratch using PyTorch
that recognizes handwritten digits with 97%+ accuracy.
This project demonstrates core ML Engineering skills including
model architecture design, training loops and evaluation.

## Architecture


## Results
| Metric | Value |
|---|---|
| Training samples | 60,000 |
| Test samples | 10,000 |
| Accuracy | 97%+ |
| Epochs | 5 |
| Optimizer | Adam |

## What I learned
- How neural networks learn through backpropagation
- Why ReLU activation functions matter
- How to evaluate model performance
- PyTorch model architecture design

## Tech Stack
- **Framework:** PyTorch 2.14
- **Dataset:** MNIST (70,000 handwritten images)
- **Environment:** Jupyter Notebook

## How to run
```bash
pip install torch torchvision
```
Open `neural_network.ipynb` and run all cells

## Key insight
The model starts with zero knowledge and learns to recognize
digits through 300,000+ parameter adjustments across 5 epochs.