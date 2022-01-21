from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    port = models.PositiveIntegerField()