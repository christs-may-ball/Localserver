from django.db import models

class Ticket(models.Model):
    time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1)
    crsid = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
    	if self.time:
    		return str(self.pk) + ': ' + self.status + ', ' + self.first_name + ' ' + self.last_name + ', ' + self.crsid + ', ' + self.time.strftime
    	else:
    		return str(self.pk) + ': ' + self.status + ', ' + self.first_name + ' ' + self.last_name + ', ' + self.crsid