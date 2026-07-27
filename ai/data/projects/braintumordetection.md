---
id: project_brain_tumor_segmentation

title: Brain Tumor Detection & Segmentation using Attention U-Net

type: project

status: Completed

priority: 85

visibility: public

category: Deep Learning

repository: MRI-Brain-Tumor-Detection-Segmentation-using-Attention-U-Net

skills:
  - Python
  - TensorFlow
  - Keras
  - OpenCV
  - NumPy
  - Matplotlib
  - CNN
  - Attention U-Net
  - Medical Imaging
  - Semantic Segmentation
  - Computer Vision
  - Deep Learning

dataset:
  - BraTS 2020

last_updated: 2024-07-01
---

# Overview

Brain Tumor Detection & Segmentation is a deep learning project focused on automated analysis of brain MRI scans. The system combines a Convolutional Neural Network (CNN) for tumor detection with an Attention U-Net architecture for precise pixel-level tumor segmentation.

The project was built using the BraTS 2020 dataset and includes a complete pipeline for preprocessing 3D MRI volumes, extracting 2D slices, training segmentation models, and visualizing predictions.

---

# Motivation

Manual segmentation of brain tumors from MRI scans is time-consuming and requires significant clinical expertise.

The goal of this project was to explore how deep learning can automate tumor detection and accurately delineate tumor boundaries, making medical image analysis faster and more consistent.

---

# Objectives

The primary objectives of this project were:

- Detect brain tumors from MRI scans using deep learning.
- Generate accurate pixel-wise tumor segmentation masks.
- Build a complete preprocessing and training pipeline for medical imaging.
- Evaluate segmentation quality using standard medical imaging metrics.
- Visualize predictions alongside ground truth masks for qualitative analysis.

---

# Dataset

The project uses the **BraTS 2020 (Brain Tumor Segmentation Challenge)** dataset.

Dataset characteristics:

- 3D MRI volumes
- HDF5 (`.h5`) file format
- Ground truth segmentation masks
- Multiple MRI modalities including:
  - FLAIR
  - T1
  - T1CE
  - T2

More than **10,000 MRI slice-mask pairs** were generated for model training and validation.

---

# Architecture

The project consists of two major deep learning components.

## Tumor Detection

A Convolutional Neural Network (CNN) was used to classify MRI scans based on the presence of brain tumors.

Responsibilities:

- Feature extraction
- Binary classification
- Tumor presence prediction

---

## Tumor Segmentation

The segmentation model is based on the **Attention U-Net** architecture.

Responsibilities:

- Pixel-level tumor localization
- Skip connections for spatial information
- Attention Gates for improved focus on tumor regions
- Binary segmentation mask generation

---

## Data Pipeline

A custom preprocessing pipeline was developed to prepare MRI data for training.

Pipeline includes:

- Loading `.h5` MRI volumes
- Extracting 2D slices from 3D scans
- Image normalization
- Mask preprocessing
- Dataset shuffling
- Train-validation split
- Dynamic reshaping for model compatibility

---

# Model Architecture

## Detection Network

- Convolutional Neural Network (CNN)
- Convolution layers
- ReLU activations
- Max Pooling
- Dense layers
- Sigmoid classification output

---

## Segmentation Network

Attention U-Net architecture with:

- Encoder blocks
- MaxPooling layers
- Bottleneck with Dropout
- Decoder with UpSampling
- Skip Connections
- Attention Gates
- Final 1×1 convolution
- Sigmoid activation

Input size:

- 128 × 128 MRI slices

Output:

- Binary segmentation mask

---

# Training

Framework:

- TensorFlow
- Keras

Training techniques:

- Adam Optimizer
- Binary Cross Entropy Loss
- Early Stopping
- Dropout Regularization

---

# Evaluation

Model performance was evaluated using:

- Dice Coefficient
- Binary Accuracy

Qualitative evaluation included:

- Original MRI slices
- Ground truth masks
- Predicted segmentation masks
- Overlay visualizations

---

# Results

The trained models demonstrated:

- Accurate tumor localization
- Smooth segmentation boundaries
- High overlap between predicted and ground truth masks
- Reliable segmentation performance across validation samples

Visualization overlays confirmed strong alignment between predicted tumor regions and annotated masks.

---

# Technologies

Programming

- Python

Deep Learning

- TensorFlow
- Keras

Computer Vision

- OpenCV

Scientific Computing

- NumPy

Visualization

- Matplotlib

Development Environment

- Jupyter Notebook

---

# My Contributions

I independently developed the complete deep learning workflow, including:

- MRI data preprocessing
- 3D to 2D slice extraction
- Dataset preparation
- CNN model development
- Attention U-Net implementation
- Model training and validation
- Performance evaluation
- Prediction visualization

---

# Challenges

Major technical challenges included:

- Processing large 3D MRI datasets efficiently
- Extracting meaningful 2D training samples
- Maintaining alignment between MRI slices and segmentation masks
- Handling class imbalance in medical segmentation
- Preventing overfitting during training
- Improving boundary accuracy using Attention Gates

---

# Key Learnings

This project strengthened my understanding of:

- Medical image preprocessing
- Deep learning for healthcare applications
- Semantic image segmentation
- Attention U-Net architecture
- CNN-based image classification
- TensorFlow/Keras model development
- Medical imaging evaluation metrics
- End-to-end deep learning pipelines

---

# Resume Summary

Developed a deep learning pipeline for brain tumor detection using Convolutional Neural Networks (CNNs) and tumor segmentation using Attention U-Net on MRI scans from the BraTS 2020 dataset. Built custom preprocessing pipelines for volumetric MRI data, trained segmentation models using TensorFlow/Keras, and evaluated performance using Dice Coefficient and binary accuracy.

---

# Interview Talking Points

## Why Attention U-Net?

Attention U-Net enhances the traditional U-Net architecture by introducing Attention Gates that enable the model to focus on relevant tumor regions while suppressing background information, leading to improved segmentation accuracy.

## Why Dice Coefficient?

Dice Coefficient is widely used in medical image segmentation because it directly measures the overlap between predicted segmentation masks and ground truth annotations, making it more informative than pixel accuracy for imbalanced datasets.

## Biggest Technical Challenge

The most challenging aspect of the project was efficiently preprocessing volumetric MRI scans into high-quality training samples while preserving accurate correspondence between MRI slices and segmentation masks.

---

# Keywords

Deep Learning, Brain Tumor Detection, Brain Tumor Segmentation, Medical Imaging, CNN, Attention U-Net, TensorFlow, Keras, Computer Vision, Semantic Segmentation, MRI, BraTS 2020, Dice Coefficient, Healthcare AI

