from django.urls import path
from .views import ConnectionQqlListAPIView, LastQqlNNewsAPIView, GovernanceQqlListAPIView, \
    ResolutionQqlListAPIView, ProvisionQqlListAPIView, ArchiveQqlListAPIView, \
    SearchArchiveQqlAPIView, ArchiveQqlDetailAPIView, NewsQqlListAPIView, GalleryQqlListAPIView, ArchiveByYearAPIView, \
    ArchiveByYearMonthAPIView

urlpatterns = [
    path('api_qql/archive/', ArchiveQqlListAPIView.as_view(), name='archive-list'),
    path('api_qql/archive/<int:pk>/', ArchiveQqlDetailAPIView.as_view(), name='archive-detail'),
    path('api_qql/archive/date/<int:year>/', ArchiveByYearAPIView.as_view(), name='archive-by-year'),
    path('api_qql/archive/date/<int:year>/<int:month>/', ArchiveByYearMonthAPIView.as_view(), name='archive-by-year-month'),
    path('api_qql/search/', SearchArchiveQqlAPIView.as_view(), name='archive-search'),
    path('api_qql/news/', NewsQqlListAPIView.as_view(), name='news-list'),
    path('api_qql/gallery/', GalleryQqlListAPIView.as_view(), name='gallery-list'),
    path('api_qql/connections/', ConnectionQqlListAPIView.as_view(), name='connection-list'),
    path('api_qql/news/last/<int:n>/', LastQqlNNewsAPIView.as_view(), name='last-n-news'),
    path('api_qql/governance/', GovernanceQqlListAPIView.as_view(), name='governance-list'),
    path('api_qql/resolutions/', ResolutionQqlListAPIView.as_view(), name='resolution-list'),
    path('api_qql/provisions/', ProvisionQqlListAPIView.as_view(), name='provision-list'),
]