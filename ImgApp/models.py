from django.db import models

class MultipleImgModel(models.Model):
    file = models.FileField(upload_to='images/', verbose_name='documents')
    uploaded_at = models.DateTimeField(auto_now_add = True)