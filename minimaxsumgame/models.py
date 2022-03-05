from django.db import models
# Create your models here.
class MinimaxPack(models.Model):
    inputs = models.CharField

    def __repr__(self):
        return '<MinimaxPack object (For inputs [{}])>'.format(self.inputs)