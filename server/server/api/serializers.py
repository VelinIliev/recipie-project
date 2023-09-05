from rest_framework import serializers

from server.recipies.models import Recipie


class RecipieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = ('id', 'title', 'description')
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField()
    # description = serializers.CharField()
    # ingredients = serializers.CharField()
    # preparation = serializers.CharField()
    # preparation_time = serializers.IntegerField()
    # cooking_time = serializers.IntegerField()
    # portions = serializers.IntegerField()
