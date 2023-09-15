from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rembg import remove
from PIL import Image
import base64
import io
import json
import os

@csrf_exempt
def remove_background(request):
    if request.method == 'POST':
        try:
            # Check if an image file was uploaded in the form data
            if 'image' not in request.FILES:
                return JsonResponse({'error': 'No image file provided in form data'}, status=400)

            # Get the uploaded image file
            uploaded_image = request.FILES['image']

            # Process the image
            input_image = Image.open(uploaded_image)
            output_image = remove(input_image)

            # Specify the output directory for saving the image
            output_directory = '/image'

            # Ensure the output directory exists, create it if necessary
            os.makedirs(output_directory, exist_ok=True)

            # Generate a unique file name for the saved image
            output_image_filename = os.path.join(output_directory, 'output_image.png')

            # Save the processed image to the specified directory
            output_image.save(output_image_filename, format="PNG")

            # Send the path to the saved image in the JSON response
            return JsonResponse({'success': True, 'image_path': output_image_filename}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
