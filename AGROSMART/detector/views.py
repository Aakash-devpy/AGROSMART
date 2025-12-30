import os
import json
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load disease steps
DISEASE_STEPS_PATH = os.path.join(settings.BASE_DIR, 'detector', 'disease_steps.json')
with open(DISEASE_STEPS_PATH, 'r', encoding='utf-8') as f:
    disease_steps = json.load(f)


# Paths to model and class mapping
MODEL_PATH = os.path.join(settings.BASE_DIR,'Plant-Disease-Detection-main',
    'trained_model.h5')
CLASS_PATH = os.path.join(settings.BASE_DIR, 'detector', 'classes.json')

# Load the model (once)
model = load_model(MODEL_PATH)
model.summary()


# Load class labels
with open(CLASS_PATH, 'r') as f:
    class_labels = json.load(f)
print("TOTAL CLASSES:", len(class_labels))




def preprocess_image(img_path, target_size=(128,128)):
    """
    Load and preprocess image for CNN prediction.
    """
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize
    return img_array

def predict_disease(img_path):
    processed_image = preprocess_image(img_path, target_size=(128, 128))
    preds = model.predict(processed_image)[0]  # shape: (38,)

    # Get top 3 predictions
    top_indices = preds.argsort()[-3:][::-1]
    top_results = []
    for i in top_indices:
        top_results.append({
            "disease": class_labels[i],  # use integer index, not str
            "confidence": float(preds[i]) * 100
        })

    return top_results




from django.http import HttpResponse

def test_view(request):
    return HttpResponse("AGROSMART CNN model loaded successfully! 🚀")

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect

@csrf_exempt
def upload_and_predict(request):
    if request.method == 'POST' and request.FILES.get('leaf_image'):
        leaf_image = request.FILES['leaf_image']

        # Save uploaded image temporarily
        save_path = os.path.join(settings.BASE_DIR, 'temp_leaf.jpg')
        with open(save_path, 'wb+') as f:
            for chunk in leaf_image.chunks():
                f.write(chunk)

        # Get top 3 predictions
        top_predictions = predict_disease(save_path)
        top_disease_name = top_predictions[0]['disease']

        # Get steps for the top disease
        step_data = disease_steps.get(top_disease_name, None)
        steps = None
        if step_data:
            # Prepare combined structure for template
            steps = []
            for category in step_data['en']:
                steps.append({
                    'category': category,
                    'pairs': list(zip(step_data['en'][category], step_data['hi'][category]))
                })


        # Delete temp file
        os.remove(save_path)

        # Save in session for PRG
        request.session['top_predictions'] = top_predictions
        request.session['steps'] = steps

        return redirect('upload_and_predict')

    # GET request
    top_predictions = request.session.pop('top_predictions', None)
    steps = request.session.pop('steps', None)
    return render(request, 'upload.html', {
        'top_predictions': top_predictions,
        'steps': steps
    })

from django.shortcuts import render, redirect
from django.contrib import messages


# VISION PAGE
def vision(request):
    return render(request, "vision.html")


# ABOUT PAGE
def about(request):
    return render(request, "about.html")


# FEEDBACK PAGE
def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # later: save to DB or send email
        messages.success(request, "Thank you for your feedback! 🌱")

        return redirect("feedback")  # PRG pattern

    return render(request, "feedback.html")