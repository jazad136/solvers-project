from django.db import models
# Create your models here.
class MinimaxPack(models.Model):
    inputs = models.CharField
    
    def __repr__(self):
        return '<MinimaxPack object (For inputs [{}])>'.format(self.inputs)

class MinimaxResponse2(models.Model):
    inputs = models.CharField
    answer = models.CharField

    def __repr__(self):
        return '<MinimaxPack object (For inputs [{}]: Output is: {})>'.format(self.inputs, self.answer)
