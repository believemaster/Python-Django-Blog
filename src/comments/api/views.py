# django rest api docs
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from comments.models import Comment

from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    create_comment_serializer,
)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = PostCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]    # cz this permissions is in default settings of rest framework setup in project settings

    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
                model_type="post", 
                slug=None, 
                parent_id=None,
                user=self.request.user
                )

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)        #gte greaterthenequal
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # lookup_url_kwarg = 'abc'

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#         # email send_email


# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailSerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]
#     # lookup_url_kwarg = 'abc'


class CommentListAPIView(ListAPIView):  # builtin search
    serializer_class = CommentListSerializer
    # permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    permission_classes = [AllowAny]
    pagination_class = PostLimitOffsetPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):  # q search
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.filter(id__gte=0)  # filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) 
            ).distinct()

        return queryset_list
