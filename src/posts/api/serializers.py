from rest_framework.serializers import (
        ModelSerializer, 
        HyperlinkedIdentityField, 
        SerializerMethodField
        )

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish',
        ]


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
)


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',     # i.e. called markdown in actual code
            'publish',
            'image',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try: 
            image = obj.image.url       # image = obj.image.path // for image path
        except: 
            return 
            image = None
        return image

    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many = True).data
        return comments 


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    # delete_url = HyperlinkedIdentityField(            #for making delete url api
    #     view_name='posts-api:delete',
    #     lookup_field='slug',
    # )
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            # 'slug',
            'content',
            'publish',
            # 'delete_url',
        ]
    

"""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data = {
        "id": 10,
        "title": "DIY",
        "slug": "diy",
        "content": "DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is DIY this is",
        "publish": "2019-03-10"
    }

    obj = Post.objects.get(id=2)

    new_item = PostDetailSerializer(data=data)
    if new_item.is_valid():
        new_item.save()

    else:
        print(new_item.errors)

"""
