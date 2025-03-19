from django.db import models


class Shipment(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=100)
    current_status = models.CharField(max_length=50, default='')
    receiver_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_number
