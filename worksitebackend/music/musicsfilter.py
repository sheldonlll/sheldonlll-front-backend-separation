import django_filters

from music.models import Music


class MusicsFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")  # icontains 表示 包含（忽略大小写）
    class Meta:
        model = Music  # 关联的表
        fields = ["title", ]  # 过滤的字段
