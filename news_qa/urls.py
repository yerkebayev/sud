from django.urls import path

from news_qa.views import CombinedQaSearchView, ConnectionQaListAPIView, LastQaNNewsAPIView, ProvisionQaListAPIView, \
    ResolutionQaListAPIView, GovernanceQaListAPIView, GalleryQaListAPIView, NewsQaListAPIView

urlpatterns = [
    path('api_qa/search/', CombinedQaSearchView.as_view(), name='combined-search'),
    path('api_qa/connections/', ConnectionQaListAPIView.as_view(), name='connection-list'),
    path('api_qa/news/last/<int:n>/', LastQaNNewsAPIView.as_view(), name='last-n-news'),
    path('api_qa/news/', NewsQaListAPIView.as_view(), name='news-list'),
    path('api_qa/gallery/', GalleryQaListAPIView.as_view(), name='gallery-list'),
    path('api_qa/governance/', GovernanceQaListAPIView.as_view(), name='governance-list'),
    path('api_qa/resolutions/', ResolutionQaListAPIView.as_view(), name='resolution-list'),
    path('api_qa/provisions/', ProvisionQaListAPIView.as_view(), name='provision-list'),
]
