from django.db import models

class Image(models.Model):
    pic = models.FileField(upload_to='MiniApp_Images')
