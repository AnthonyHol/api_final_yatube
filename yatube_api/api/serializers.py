from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = (
            "id",
            "pub_date",
        )


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = SlugRelatedField(slug_field="username", read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "id",
            "post",
            "created",
        )


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ("__all__",)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = "__all__"
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message=("Подписка уже существует!"),
            ),
        )

    def validate(self, data):
        if data["user"] == data["following"]:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        return data
