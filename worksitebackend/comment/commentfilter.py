import django_filters

from comment.models import Comment


class CommentFilter(django_filters.rest_framework.FilterSet):
    object_id = django_filters.NumberFilter(field_name="object_id")  # icontains 表示 包含（忽略大小写）
    content_type = django_filters.NumberFilter(field_name="content_type")  # icontains 表示 包含（忽略大小写）
    class Meta:
        model = Comment  # 关联的表
        fields = ["object_id", 'content_type', ]  # 过滤的字段
