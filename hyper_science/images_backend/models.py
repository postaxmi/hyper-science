from django.db import models

import uuid


class BaseModelClass(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Detector(BaseModelClass):
    pass


class Person(Detector):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    institution = models.CharField(max_length=100, null=True, blank=True)


class Instrument(BaseModelClass):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Acquisition(BaseModelClass):
    date = models.DateTimeField()
    instrument_used = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    image_source = models.ForeignKey('Image', on_delete=models.CASCADE)
    persons = models.ManyToManyField(Person)


class Image(BaseModelClass):
    name = models.CharField(max_length=100)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    url = models.URLField()


# class DataContainer(BaseModelClass):
#     fileFormat = models.CharField(max_length=10)
#     formatIdentifier = models.CharField(max_length=20)
#     formatVersion = models.CharField(max_length=20)
#     url = models.URLField()
#     image = models.ForeignKey('Image', related_name='files', on_delete=models.CASCADE)


class Algorithm(Detector):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)


class Article(BaseModelClass):
    title = models.CharField(max_length=100)
    persons = models.ManyToManyField(Person)
    images = models.ManyToManyField(Image)


class Classification(BaseModelClass):
    image_classified = models.ForeignKey('Image', on_delete=models.CASCADE)
    detector_analyzer = models.ForeignKey('Detector', on_delete=models.CASCADE)
    category_assigned = models.ForeignKey('Category', on_delete=models.CASCADE)
    confidence = models.FloatField()


class Category(BaseModelClass):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE)


class AttributeDefinition(BaseModelClass):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class InstanceValues(BaseModelClass):
    # instance is the actual category with specific values.
    instance = models.ForeignKey('Category', on_delete=models.CASCADE)
    attribute = models.ForeignKey('AttributeDefinition', on_delete=models.CASCADE)
    value = models.CharField(max_length=100)  # this should be a jolly tpye
