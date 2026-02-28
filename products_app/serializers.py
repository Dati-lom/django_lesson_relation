from rest_framework import serializers
from .models import Item, Category, Tag


class TagInputSerializer(serializers.Serializer):
    """Plain serializer exercise for creating/updating tags by name."""
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        # TODO: create and return a Tag instance using validated_data
        raise NotImplementedError("Implement Tag creation for the exercise")

    def update(self, instance, validated_data):
        # TODO: update and return the Tag instance
        raise NotImplementedError("Implement Tag update for the exercise")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, source="tags", write_only=True
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "price",
            "active",
            "category",
            "tags",
            "category_id",
            "tag_ids",
        ]

    def create(self, validated_data):
        # TODO: pop nested relation data and create Item with M2M tags
        raise NotImplementedError("Implement Item creation handling category and tags")

    def update(self, instance, validated_data):
        # TODO: update fields and sync many-to-many tags
        raise NotImplementedError("Implement Item update handling category and tags")

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value
