from lego.apps.content.fields import ContentSerializerField
from lego.apps.files.fields import ImageField
from lego.apps.flatpages.models import Page
from lego.utils.serializers import (
    BasisModelSerializer,
    ObjectPermissionsSerializerMixin,
)


class PageListSerializer(BasisModelSerializer):
    class Meta:
        model = Page
        fields = ("pk", "title", "slug", "category")


class PageDetailSerializer(BasisModelSerializer, ObjectPermissionsSerializerMixin):
    content = ContentSerializerField()
    picture = ImageField(required=False, options={"height": 500})

    class Meta:
        model = Page
        fields = ("pk", "title", "slug", "content", "picture", "category")


class PageDetailAuthSerializer(BasisModelSerializer, ObjectPermissionsSerializerMixin):
    content = ContentSerializerField()
    picture = ImageField(required=False, options={"height": 500})

    class Meta:
        model = Page
        fields = (
            PageDetailSerializer.Meta.fields
            + ObjectPermissionsSerializerMixin.Meta.fields
        )
