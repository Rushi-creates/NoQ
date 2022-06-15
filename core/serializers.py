from rest_framework import serializers
from core.models import *


class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta : 
        model = MemberProfile
        fields = '__all__'
        # fields = [ 'id' , 'bio' , 'userName' , 'uid']


class QueueSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Queue
        fields = '__all__'

class QueueUserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = QueueUser
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    # authUser_in_queue_uid = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    # authUser_in_queueUser_uid = serializers.SlugRelatedField(many=True, read_only=True, slug_field='recordTime')
    authUser_in_queue_uid = QueueSerializer( many=True , read_only=True ) 
    authUser_in_queueUser_uid = QueueUserSerializer( many=True , read_only=True ) 

    class Meta:
        model = AuthUser
        fields = [ 'id','email','password','isAdmin','isAdminVerified','authUser_in_queueUser_uid','authUser_in_queue_uid']
        # fields = '__all__'


# class GymTrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GymTrack
#         fields = '__all__'

# class AttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendance
#         fields = '__all__'