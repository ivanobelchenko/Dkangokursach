from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GetUserView, AuthorViewSet, GetNewsView, NewsViewSet

router = DefaultRouter()
router.register('user', UserViewSet )
router.register('author', AuthorViewSet )
router.register('news', NewsViewSet )

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/filt', GetUserView.as_view()),
    path('api/news/filt', GetNewsView.as_view()),
]