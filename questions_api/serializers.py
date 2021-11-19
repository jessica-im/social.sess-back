from rest_framework import serializers
from .models import Comment, Question
from .models import UserAccount

from django.contrib.auth.hashers import make_password, check_password

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'username', 'password','comment','question')

    def create(self, validated_data):
        user = UserAccount.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self, instance, validated_data):
        user = UserAccount.objects.get(username=validated_data["username"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','comment','question')
