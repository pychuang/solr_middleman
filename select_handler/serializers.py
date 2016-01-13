from rest_framework import serializers
from .models import Query


class QuerySerializer(serializers.ModelSerializer):

   class Meta:
        model = Query
        fields = ('q',)


class SolrResultSerializer(serializers.Serializer):
#    id = serializers.CharField(max_length=255)
    doi = serializers.CharField(max_length=255)
#    incol = serializers.BooleanField()
#    title = serializers.CharField(max_length=255)
#    venue = serializers.CharField(max_length=255)
#    abstract = serializers.TextField()
#    ncites = serializers.IntegerField()
#    scites = serializers.IntegerField()
#    year = serializers.IntegerField()
    author = serializers.ListField(
        child = serializers.CharField(max_length=255)
    )
#    vtime = serializers.IntegerField()

    def __init__(self, **kwargs):
        self.doi = kwargs['doi']
        #self.author = kwargs['author']
