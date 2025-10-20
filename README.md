# 🎨 Video Colorization

## 📘 Project Overview
This project implements an **deep learning based video colorization pipeline** that learns to colorize grayscale videos using the large-scale **Kinetics-400** dataset. The system combines **deep learning (CNN/Transformer)** models with **temporal consistency** and a lightweight **Streamlit UI** for interactive visualization.

---

## 🧩 Repository Structure
```bash

Video-Colorization/
│
├── data/
│ ├── kinetics-dataset/ # contains k400_subset.txt and downloaded .gz files
│ ├── dataset/ # extracted videos after running download_kinetics_dataset.py
│ 
├── notebooks/
│ └── inspect_kinetics_dataset.ipynb # verifies video count & previews one sample
│
├── src/
│ ├── download_kinetics.py # downloads & extracts dataset automatically
│ ├── data_loader.py # helper functions for reading frames
│ ├── preprocess.py # frame normalization & grayscale conversion
│ ├── model.py # colorization network (CNN/U-Net/Transformer)
│ ├── train.py # training script
│ ├── inference.py # inference + video reconstruction
│ └── ui/app.py # Streamlit interactive interface
│
├── results/ # sample colorized outputs 
├── docs/ # diagrams, mockups, report visuals
├── requirements.txt
└── README.md
```

## ⚙️ Project Setup

### 1️⃣ Create Environment
```bash
conda create -n video_color_ev python=3.10 -y
conda activate video_color_ev
```

### 2️⃣ Clone the project Repository
```bash
git clone https://github.com/UF-EEE6778-Fall25/Video-Colorization.git
cd Video-Colorization
pip install -r requirements.txt
```

### 3️⃣ Download & Visualize the Kinetics400 Dataset
```bash
python src/download_kinetics_dataset.py
jupyter notebook notebooks/inspect_kinetics_dataset.ipynb
```

### 4️⃣ Model Training
```bash
To be added..
```

### 5️⃣ Inference and UI
```bash
To be added..
```

## 📊 Dataset Description
-  Dataset: [Kinetics-400](https://github.com/cvdfoundation/kinetics-dataset) (subset version)
-  Source: DeepMind / Google Research
-  Type: Short human action videos (~10 seconds each)
-  Format: .mp4 compressed clips inside .tar.gz archives
-  Size: ~20–30 GB for 10 subsets (each 2–3 GB)
-  Usage: Used to train models that understand motion, context, and object color cues.


## System Requirements

### Recommended Setup
To run this repository smoothly, ensure you have one of the following:

-  Anaconda / Miniconda installed (for managing Python environments)
-  VS Code or JupyterLab configured with:
    -  Python and Jupyter extensions
    -  GPU support (if available)
    -  Integrated terminal for running .py and .ipynb files simultaneously

> Run .py files (e.g., download or training scripts) from the terminal,
and .ipynb notebooks from Jupyter Notebook or VS Code Notebook interface.

### Basic Requirements

-  Python ≥ 3.10
-  Conda ≥ 23.x or pip ≥ 23.x
-  GPU with ≥ 6GB VRAM (recommended for training)
-  30–40 GB free storage for dataset and extracted videos

> **Note:** Downloading & extracting the Dataset wil take maximum of 20 minutes.



