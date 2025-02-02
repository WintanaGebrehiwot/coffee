from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm  # Create this form
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os
from .load_model import load_trained_model
from django.conf import settings
from django.urls import reverse

# Load the model once when **the server starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'final_code.keras')
model = load_model(MODEL_PATH)

# Define class labels (adjust based on your model)
CLASS_LABELS = {
    0: 'Cercospora',
    1: 'Healthy',
    2: 'Leaf Rust',
    3: 'Phoma'
}

def predict_disease(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            uploaded_image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_image.name)
            
            # Save the image to the server
            with open(image_path, 'wb+') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            # Construct the image URL
            image_url = os.path.join(settings.MEDIA_URL, 'uploads', uploaded_image.name)

            # Preprocess and predict as before
            image = Image.open(image_path).convert('RGB')
            image = image.resize((256, 256))  # Resize to model input size
            image_array = img_to_array(image)
            image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
            image_array = image_array / 255.0  # Normalize pixel values

            predictions = model.predict(image_array)
            predicted_class = np.argmax(predictions, axis=1)[0]
            disease_name = CLASS_LABELS[predicted_class]

            recommendations = {
                'Healthy': "No action needed. Your plant is healthy!",
                'Phoma': "Use fungicides to treat Phoma disease.",
                'Cercospora': "Ensure proper air circulation and apply fungicides.",
                'Leaf Rust': "Remove infected leaves and consider resistant varieties."
            }
            recommendation = recommendations.get(disease_name, "No recommendation available.")

            return render(request, 'predict_result.html', {
                'disease': disease_name,
                'recommendation': recommendation,
                'image_url': image_url  # Use the correct image URL here
            })
    else:
        form = ImageUploadForm()

    return render(request, 'predict.html', {'form': form})  # Ensure a response is returned in all cases