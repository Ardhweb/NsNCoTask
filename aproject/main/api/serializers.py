from rest_framework import serializers
from main.models import Client ,Artist , Work
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']



class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id','link', 'work_type']



class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'work']