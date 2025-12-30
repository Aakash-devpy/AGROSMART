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
Class 11th “A”, PM Shri Kendriya Vidyalaya Bairagarh 
email:-
GitHub: [https://github.com/<your-username>](https://github.com/Aakash-devpy)  
Date: 30 Dec 2025

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
- This project uses the pre-trained **PlantVillage CNN model** from [Eshwar7325 / Plant-Disease-Detection](https://github.com/Eshwar7325/Plant-Disease-Detection.git)  
- Huge respect and thanks to the author for sharing the model and making this project possible.

