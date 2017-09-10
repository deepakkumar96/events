from rest_framework import serializers
from events.models import Event, MyUser


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event_name', 'location', 'user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }