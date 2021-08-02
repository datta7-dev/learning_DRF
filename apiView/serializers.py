from rest_framework import serializers
from apiView.models import Teacher


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        #fields = "__all__"
        fields = ["teacher_id", "name"]
