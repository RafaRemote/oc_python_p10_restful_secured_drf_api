from rest_framework import serializers
from contributor.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
