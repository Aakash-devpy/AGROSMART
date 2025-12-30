# AGROSMART 

AGROSMART is an AI-powered **Crop Disease Detection System** built using Django and a Convolutional Neural Network (CNN). It allows users to **identify diseases in plants** from leaf images and provides **step-by-step treatment guidance** in both **English and Hindi**. The system is designed to be **user-friendly, interactive, and informative**, helping farmers and plant enthusiasts maintain healthy crops.

---

## Features
- Detects diseases from plant leaf images.
- Provides **top-3 predictions** with confidence scores.
- Displays **treatment steps** for the top-1 disease.
- Supports **English and Hindi** languages.
- Drag-and-drop image upload with preview and removal.
- Animated UI and alert-based disease color coding.
- Session-safe submission using Post/Redirect/Get (PRG) pattern.
- Clean separation of HTML, CSS, and JS for easy maintenance.

---

## Made By
**Aakash Singh**  
Class 11th “A” (2025-26), PM Shri Kendriya Vidyalaya Bairagarh
GitHub: [https://github.com/<your-username>](https://github.com/Aakash-devpy)  
Date: 30 Dec 2025

---

## Model Dependency
This project requires an external pre-trained CNN model.

Before running AGROSMART, download the following repository and extract the trained model files as required:

- **Plant Disease Detection (CNN Model)**  
  https://github.com/Eshwar7325/Plant-Disease-Detection

Make sure the model files are placed in the correct directory expected by the Django application before starting the server.

---
## Steps
1. Create virtual environment named venv and install Django,pillow,numpy and tensorflow:-
     - here are the list of cmd step-by-step  in AGROSMART (for windows) :-
               ```bash
                     python -m venv venv
                     cd venv/scripts
                     activate
                     pip install Django
                     pip install pillow
                     pip install tensorflow
                     pip install numpy
                     cd..
                     cd..
                     cd AGROSMART
                     python manage.py runserver 8000
       
---


## Credits / Acknowledgements
- This project uses a pre-trained **PlantVillage CNN model** sourced from  
  **Eshwar7325 / Plant-Disease-Detection**  
  https://github.com/Eshwar7325/Plant-Disease-Detection
- All credit for the original model architecture and training goes to the original author.
- The model is used here strictly for **educational and demonstration purposes**.
- This project does not claim ownership of the original dataset or trained model.


