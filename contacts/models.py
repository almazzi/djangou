from  django.core.urlresolvers import reverse
from django.db import models


class Contact(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )

    telephone_number = models.IntegerField()


    email = models.EmailField()

    def __unicode__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])

    def get_absolute_url(self):
        return reverse('contact-detail' , kwargs={'pk': self.id})
