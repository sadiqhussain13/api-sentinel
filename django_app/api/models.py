from django.db import models

class APIMetric(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class AnomalyDetection(models.Model):
    metric = models.ForeignKey(APIMetric, on_delete=models.CASCADE)
    is_anomalous = models.BooleanField(default=False)
    detected_at = models.DateTimeField(auto_now_add=True)

class AlertRule(models.Model):
    name = models.CharField(max_length=255)
    threshold = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
