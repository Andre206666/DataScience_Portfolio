
# Handwritten Digit Recognition with PyTorch

A deep learning project that classifies handwritten digits (0–9) using the MNIST dataset and a fully connected neural network.

The project covers the main stages of a machine learning workflow: data preparation, model development, training, validation, testing, performance analysis, and model saving.

## Project Highlights

- Built a multilayer perceptron (MLP) with PyTorch.
- Designed a neural network with two hidden layers and ReLU activations.
- Trained the model using backpropagation, `CrossEntropyLoss`, and the Adam optimizer.
- Split the official training dataset into training and validation sets.
- Selected the best checkpoint based on validation accuracy.
- Evaluated the selected model on the held-out test dataset.
- Generated training curves, a confusion matrix, and prediction examples.
- Saved the trained model weights for future inference.

## Model Architecture

| Layer | Output Features | Activation |
|---|---:|---|
| Flatten | 784 | None |
| Fully connected | 128 | ReLU |
| Fully connected | 64 | ReLU |
| Output layer | 10 | None |

The network receives 28 × 28 grayscale images, flattens each image into a vector of 784 features, and outputs scores for the 10 digit classes.

The output layer returns raw logits. `CrossEntropyLoss` handles the required log-softmax operation internally, so a separate softmax layer is not needed during training.

**Trainable parameters:** 109,386

## Dataset

This project uses [MNIST](https://www.tensorflow.org/datasets/catalog/mnist), a dataset of handwritten digit images.

- Image size: 28 × 28 pixels
- Image type: grayscale
- Classes: digits 0 through 9
- Official training set: 60,000 images
- Official test set: 10,000 images

The official training set is divided into:

- Training: 54,000 images
- Validation: 6,000 images
- Testing: 10,000 images

The test set is kept separate during training and model selection.

The dataset is downloaded automatically by `torchvision` on the first run.

## Tech Stack

- Python
- PyTorch
- torchvision
- NumPy
- Matplotlib

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Andre206666/DataScience_Portfolio.git
cd DataScience_Portfolio/24_neural_network
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

The first execution requires an internet connection to download MNIST.

The script automatically selects a supported GPU when available and otherwise runs on the CPU.

## Outputs

The project generates the following files:

| File | Description |
|---|---|
| `mnist_model.pth` | Saved model weights |
| `outputs/training_history.png` | Training and validation loss and accuracy |
| `outputs/confusion_matrix.png` | Correct and incorrect predictions by digit |
| `outputs/prediction_examples.png` | Sample images with true and predicted labels |

Generated outputs are excluded from Git by `.gitignore` to avoid committing large files unnecessarily.


## Results

The model achieved **97.30% test accuracy** after 5 training epochs on the MNIST dataset.

| Metric | Result |
|---|---:|
| Training accuracy | 98.33% |
| Best validation accuracy | 97.18% |
| Final test accuracy | 97.30% |
| Trainable parameters | 109,386 |
| Epochs | 5 |
| Batch size | 64 |
| Optimizer | Adam |
| Learning rate | 0.001 |

### Per-Class Test Accuracy

| Digit | Accuracy |
|---|---:|
| 0 | 98.27% |
| 1 | 98.77% |
| 2 | 98.84% |
| 3 | 96.04% |
| 4 | 97.66% |
| 5 | 96.41% |
| 6 | 98.23% |
| 7 | 96.60% |
| 8 | 96.20% |
| 9 | 95.74% |

The model performed best on digit 2 (98.84%) and had its lowest accuracy on digit 9 (95.74%). These results can guide further error analysis and model improvements.


## What I Learned

This project provides practical experience with:

- Neural network architecture and tensor transformations
- Forward propagation and backpropagation
- Gradient-based optimization
- Training, validation, and test-set separation
- Classification accuracy and confusion matrices
- Saving and reusing model weights
- Reproducible experiments using random seeds

The model uses PyTorch's automatic differentiation and neural network layers; backpropagation is not implemented manually from scratch.

## Future Improvements

- Compare the MLP against a convolutional neural network (CNN).
- Tune the learning rate, batch size, and hidden-layer dimensions.
- Analyze which digits are most frequently misclassified.
- Compare training time on CPU and GPU.
- Add per-class precision, recall, and F1-score.
