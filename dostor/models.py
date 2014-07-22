from django.db import models
from django.core.urlresolvers import reverse

class Dostor(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    joined_date = models.timezone
    def __unicode__(self):
        return ' '.join([self.name, self.surname])

    def get_absolute_url(self):
        return reverse('dos-detail', kwargs={'pk': self.id})
# Create your models here.
