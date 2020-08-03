from rest_framework import serializers

from identity.models import User


class CandidateListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    pollData = serializers.SerializerMethodField()

    def get_pollData(self, obj):
        return obj.polling.all()

    class Meta:
        model = User
        fields = ("first_name", 'last_name', 'email', 'pollData')


class PollingSerializer(serializers.Serializer):
    id = serializers.CharField()
    datastructure = serializers.CharField(allow_null=True)
    algorithm = serializers.CharField(allow_null=True)
    cplusplus = serializers.CharField(allow_null=True)
    python = serializers.CharField(allow_null=True)
    java = serializers.CharField(allow_null=True)
