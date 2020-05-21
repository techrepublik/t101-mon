from django.db import models
from django.urls import reverse


class Client(models.Model):
    client_no       = models.CharField(max_length=50)
    client_name     = models.CharField(max_length=150)
    client_address  = models.CharField(max_length=200)
    client_email    = models.CharField(max_length=100)
    client_registered = models.DateField(auto_now_add=False)
    client_active   = models.BooleanField(default=False)
    client_ip       = models.CharField(default="0.0.0.0", max_length=20)

    def __str__(self):
        return  "{0} - {1}".format(self.client_no, self.client_name)
    
    def get_absolute_url(self):
        return reverse("update_client", kwargs={"pk": self.pk})

class Status(models.Model):
    OFF     = 'OFFLINE'
    RTO     = 'TIMED-OUT'
    INT     = 'INTERMITENT'
    ON      = 'ONLINE'
    STATUS    = (
        (OFF, 'Offline'), 
        (RTO, 'Time out'),
        (INT, 'Intermitent'),
        (ON, 'Online'),
    )
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    status_date     = models.DateField(auto_now_add=True)
    status_time     = models.TimeField(auto_now_add=True)
    status_note     = models.CharField(max_length=200)
    status_type     = models.CharField(max_length=11, choices=STATUS, default=OFF)

    class Meta:
        indexes     = [models.Index(fields=['status_date'])]
        ordering    = ['-status_date']
        verbose_name= 'status'
        verbose_name_plural = 'statuses'