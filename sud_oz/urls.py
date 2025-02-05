from django.urls import path
from .views import ConnectionOzListAPIView, LastOzNNewsAPIView, GovernanceOzListAPIView, \
    ResolutionOzListAPIView, ProvisionOzListAPIView, ArchiveOzListAPIView, \
    SearchArchiveOzAPIView, ArchiveOzDetailAPIView, NewsOzListAPIView, GalleryOzListAPIView, ArchiveByYearAPIView, \
    ArchiveByYearMonthAPIView

urlpatterns = [
    path('api_oz/archive/', ArchiveOzListAPIView.as_view(), name='archive-list'),
    path('api_oz/archive/<int:pk>/', ArchiveOzDetailAPIView.as_view(), name='archive-detail'),
    path('api_oz/archive/date/<int:year>/', ArchiveByYearAPIView.as_view(), name='archive-by-year'),
    path('api_oz/archive/date/<int:year>/<int:month>/', ArchiveByYearMonthAPIView.as_view(), name='archive-by-year-month'),
    path('api_oz/search/', SearchArchiveOzAPIView.as_view(), name='archive-search'),
    path('api_oz/news/', NewsOzListAPIView.as_view(), name='news-list'),
    path('api_oz/gallery/', GalleryOzListAPIView.as_view(), name='gallery-list'),
    path('api_oz/connections/', ConnectionOzListAPIView.as_view(), name='connection-list'),
    path('api_oz/news/last/<int:n>/', LastOzNNewsAPIView.as_view(), name='last-n-news'),
    path('api_oz/governance/', GovernanceOzListAPIView.as_view(), name='governance-list'),
    path('api_oz/resolutions/', ResolutionOzListAPIView.as_view(), name='resolution-list'),
    path('api_oz/provisions/', ProvisionOzListAPIView.as_view(), name='provision-list'),
]