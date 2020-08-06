from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'users'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = User # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'username',
            'email',
        ]