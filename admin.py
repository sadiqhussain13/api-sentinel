from django.contrib import admin
from .models import APIMetric, AnomalyDetection, AlertRule, UserProfile

@admin.register(APIMetric)
class APIMetricAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['name']

@admin.register(AnomalyDetection)
class AnomalyDetectionAdmin(admin.ModelAdmin):
    list_display = ['metric', 'is_anomalous', 'detected_at']
    list_filter = ['is_anomalous', 'detected_at']

@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'threshold', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'notifications_enabled', 'created_at']
    list_filter = ['notifications_enabled', 'created_at']