from django.urls import path
from .views import ConnectionUzListAPIView, LastUzNNewsAPIView, GovernanceUzListAPIView, \
    ResolutionUzListAPIView, ProvisionUzListAPIView, ArchiveUzListAPIView, \
    SearchArchiveUzAPIView, ArchiveUzDetailAPIView, NewsUzListAPIView, GalleryUzListAPIView, ArchiveByYearAPIView, \
    ArchiveByYearMonthAPIView

urlpatterns = [
    path('api_uz/archive/', ArchiveUzListAPIView.as_view(), name='archive-list'),
    path('api_uz/archive/<int:pk>/', ArchiveUzDetailAPIView.as_view(), name='archive-detail'),
    path('api_uz/archive/date/<int:year>/', ArchiveByYearAPIView.as_view(), name='archive-by-year'),
    path('api_uz/archive/date/<int:year>/<int:month>/', ArchiveByYearMonthAPIView.as_view(), name='archive-by-year-month'),
    path('api_uz/search/', SearchArchiveUzAPIView.as_view(), name='archive-search'),
    path('api_uz/news/', NewsUzListAPIView.as_view(), name='news-list'),
    path('api_uz/gallery/', GalleryUzListAPIView.as_view(), name='gallery-list'),
    path('api_uz/connections/', ConnectionUzListAPIView.as_view(), name='connection-list'),
    path('api_uz/news/last/<int:n>/', LastUzNNewsAPIView.as_view(), name='last-n-news'),
    path('api_uz/governance/', GovernanceUzListAPIView.as_view(), name='governance-list'),
    path('api_uz/resolutions/', ResolutionUzListAPIView.as_view(), name='resolution-list'),
    path('api_uz/provisions/', ProvisionUzListAPIView.as_view(), name='provision-list'),
]