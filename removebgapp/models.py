from django.db import models

class ProcessedImage(models.Model):
    input_image = models.ImageField(upload_to='input_images/')
    output_image = models.ImageField(upload_to='output_images/')
    processed_at = models.DateTimeField(auto_now_add=True)