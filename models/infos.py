from mongoengine import Document, FloatField, DateField, connect

connect('smart_grou')


class InfoModel(Document):
    meta = {'collection': 'cmsPage'}
    temp = FloatField()
    wet = FloatField()
    time = DateField()
