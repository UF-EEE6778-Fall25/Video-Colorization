# 🎨 Video Colorization

## 📘 Project Overview
This project implements an **deep learning based video colorization pipeline** that learns to colorize grayscale videos using the large-scale **Kinetics-400** dataset. The system combines **deep learning (CNN/Transformer)** models with **temporal consistency** and a lightweight **Gradio UI** for interactive visualization.

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
│ ├── video_colorization.ipynb # data preprocessing, model training, evaluation & GRADIO Interface
│
├── results/ # sample colorized outputs
│ ├── checkpoints # model best weights' (.pt file)
│ ├── gray_test_videos # test videos downloaded from the internet
│     ├── tv1.mpv4
│     ├── tv2.mpv4
│     └── tv3.mpv4
│ ├── colorized_test_videos # predicted videos (colorized)
│     ├── colorized_tv1.mpv4
│     ├── colorized_tv2.mpv4
│     └── colorized_tv3.mpv4
│ └── gradio # interface screenshots
│     ├── gradio_interface.png
│     ├── test_video_uploaded.png
│     └── test_video_colorized.png
├── docs/ # reports
│ ├── Project_Roadmap.pdf
│ ├── Project_Preliminary_Report.pdf
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
jupyter notebook src/video_colorization_enhanced.ipynb
```

### 5️⃣ Gradio Inference 
```bash
jupyter notebook src/video_colorization.ipynb
# Inline Gradio Interface is provided in the notebook cell.
```

## 🎨 Before vs After – Video Colorization Results

| Grayscale Input | Colorized Output |
|------------------|------------------|
| [Watch Gray Video](https://github.com/UF-EEE6778-Fall25/Video-Colorization/raw/refs/heads/main/assests/tv2.mp4) | [Watch Colorized Video](https://github.com/UF-EEE6778-Fall25/Video-Colorization/raw/refs/heads/main/assests/colorized_tv2.mp4) |

> The model converts grayscale videos into vivid color using a lightweight **U-Net** trained on the **Kinetics dataset**.  
> **Average metrics:** PSNR ≈ 38 dB | SSIM ≈ 0.98




## 📊 Dataset Description
-  Dataset: [Kinetics-400](https://github.com/cvdfoundation/kinetics-dataset) (subset version)
-  Source: DeepMind / Google Research
-  Type: Short human action videos (~10 seconds each)
-  Format: .mp4 compressed clips inside .tar.gz archives
-  Size: ~20–30 GB for 10 subsets (each 2–3 GB)
-  Usage: Used to train models that understand motion, context, and object color cues.

> **Note:** Downloading & extracting the Dataset will take atleast 20 minutes.


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

---

## 👩‍💻 Author
**Santhi Daggubati**  
*M.S. in Applied Data Science, University of Florida*  

📧 **Email:** daggubati.santhi@ufl.edu  
🌐 **Website:** [Protfolio](https://72santhi.github.io/Portfolio/)  
💼 **GitHub:** [72santhi](https://github.com/72santhi)  
🔗 **LinkedIn:** [Santhi Daggubati](https://www.linkedin.com/in/Santhi37911/)
