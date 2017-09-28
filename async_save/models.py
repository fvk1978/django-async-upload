from django.db import models


class UploadingFileModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    size = models.IntegerField(null=True)
    # Variable to indicate processing
    # i dont know if it would be better to use
    # something like "chunks left"
    percents = models.IntegerField(null=True)
    characters = models.IntegerField(null=True)
    ready = models.BooleanField(default=False)
