from django.template.defaultfilters import date as _date
from rest_framework import serializers
from profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'surname', 'type', 'created_at', 'updated_at', )

    def get_created_at(self, obj):
        return _date(obj.created_at, "d F, Y")

    def get_updated_at(self, obj):
        return _date(obj.updated_at, "d F, Y")
