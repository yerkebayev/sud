from django.urls import path

from .views import CombinedUzSearchView, LastUzNNewsAPIView, ConnectionUzListAPIView, GovernanceUzListAPIView, \
    ResolutionUzListAPIView, ProvisionUzListAPIView, NewsUzListAPIView, GalleryUzListAPIView

urlpatterns = [
    path('api_uz/search/', CombinedUzSearchView.as_view(), name='combined-search'),
    path('api_uz/connections/', ConnectionUzListAPIView.as_view(), name='connection-list'),
    path('api_uz/news/last/<int:n>/', LastUzNNewsAPIView.as_view(), name='last-n-news'),
    path('api_uz/news/', NewsUzListAPIView.as_view(), name='news-list'),
    path('api_uz/gallery/', GalleryUzListAPIView.as_view(), name='gallery-list'),
    path('api_uz/governance/', GovernanceUzListAPIView.as_view(), name='governance-list'),
    path('api_uz/resolutions/', ResolutionUzListAPIView.as_view(), name='resolution-list'),
    path('api_uz/provisions/', ProvisionUzListAPIView.as_view(), name='provision-list'),
]
