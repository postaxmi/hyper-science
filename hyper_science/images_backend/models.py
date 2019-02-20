from django.db import models

import uuid


def uuid_without_hypens():
    return uuid.uuid4().hex


class BaseModelClass(models.Model):
    uuid = models.CharField(
        primary_key=True, default=uuid_without_hypens, editable=False, max_length=32)


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
    category_assigned = models.ForeignKey('CategoryDefinition', on_delete=models.CASCADE)
    confidence = models.FloatField()


class CategoryDefinition(BaseModelClass):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "'{}' ({}, parent: {})".format(self.name, self.uuid,
                                              self.parent.uuid if self.parent else None)


class AttributeDefinition(BaseModelClass):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    _BOOL, _INT, _DOUBLE, _STR = "B", "I", "D", "S"
    _TYPE_CHOICES = (
        (_BOOL, 'Boolean'),
        (_INT, 'Integer'),
        (_DOUBLE, 'Double'),
        (_STR, 'String'),
    )
    # This stores the type of value saved in the InstanceValue instance.
    value_type = models.CharField(max_length=1)


class CategoryDictionary(BaseModelClass):
    """This class is made up of dictionary of attributes linked to categories."""
    category = models.ForeignKey('CategoryDefinition', on_delete=models.CASCADE)
    attribute = models.ForeignKey('AttributeDefinition', on_delete=models.CASCADE)


class InstanceValue(BaseModelClass):
    """Store the actual value for the concept/dictionary in CategoryDictionary."""

    category_dict = models.ForeignKey(CategoryDictionary, on_delete=models.CASCADE)
    # This field stores the actual value the user defines, in JSON format, that we need to validate
    # in the category_dict.attribute_definition.value_type field.
    value = models.TextField()
