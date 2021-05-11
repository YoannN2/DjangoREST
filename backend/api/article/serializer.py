from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        read_only_fields = (
            "id",
            "user",
        )

        fields = (
            "id",
            "titre",
            "description",
            "full_text",
            "author",
            "created_at",
        )
