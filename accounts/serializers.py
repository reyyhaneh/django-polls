from rest_framework import serializers 
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # password validator not needed.
    # write_only: only used to accept data during registration, not included in the output.

    # Model related settings.
    class Meta:
        model = User
        fields = ['username', 'password', 'national_id', 'first_name', 'last_name']
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            national_id = validated_data['national_id'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_staff=True, # so the user can login to admin.
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserloginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
