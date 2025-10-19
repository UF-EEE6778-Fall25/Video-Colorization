# 🎨 Video Colorization

## 📘 Project Overview
This project implements an **deep learning based video colorization pipeline** that learns to colorize grayscale videos using the large-scale **Kinetics-600** dataset.  
The system combines **deep learning (CNN/Transformer)** models with **temporal consistency** and a lightweight **Streamlit UI** for interactive visualization.

---

## 🧩 Repository Structure
video-colorization/
│
├── data/
│ ├── kinetics-dataset/ # contains k400_subset.txt and downloaded .gz files
│ ├── dataset/ # extracted videos after running download_kinetics_dataset.py
│ 
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


---

## ⚙️ Environment Setup

### 1️⃣ Create Environment
```bash
conda create -n video_color_ev python=3.10 -y
conda activate video_color_ev
pip install -r requirements.txt


---
## Clone the project Repository
```bash
git clone https://github.com/UF-EEE6778-Fall25/Video-Colorization.git
cd Video-Colorization


