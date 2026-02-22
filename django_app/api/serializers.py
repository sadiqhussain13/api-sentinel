from rest_framework import serializers
from .models import APIMetric, AnomalyDetection, AlertRule, UserProfile

class APIMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIMetric
        fields = '__all__'

class AnomalyDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnomalyDetection
        fields = '__all__'

class AlertRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertRule
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'