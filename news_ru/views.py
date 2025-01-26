from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import NewsRu, GalleryRu, ConnectionRu, GovernanceRu, ResolutionRu, ProvisionRu
from .serializers import NewsRuSerializer, GalleryRuSerializer, ConnectionRuSerializer, GovernanceRuSerializer, \
    ResolutionRuSerializer, ProvisionRuSerializer


class CombinedRuSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        # Search in News
        news_queryset = NewsRu.objects.all()
        if search_query:
            news_queryset = news_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        news_serializer = NewsRuSerializer(news_queryset, many=True)

        # Search in Gallery
        gallery_queryset = GalleryRu.objects.all()
        if search_query:
            gallery_queryset = gallery_queryset.filter(
                Q(title__icontains=search_query)
            )

        gallery_serializer = GalleryRuSerializer(gallery_queryset, many=True)

        return Response({
            'news_ru': news_serializer.data,
            'galleries': gallery_serializer.data
        })

    def post(self, request):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            serializer = NewsRuSerializer(data=request.data)
        elif data_type == 'gallery':
            serializer = GalleryRuSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            instance = NewsRu.objects.get(pk=pk)
            serializer = NewsRuSerializer(instance, data=request.data)
        elif data_type == 'gallery':
            instance = GalleryRu.objects.get(pk=pk)
            serializer = GalleryRuSerializer(instance, data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_type = request.GET.get('type')
        if data_type == 'news_ru':
            NewsRu.objects.get(pk=pk).delete()
        elif data_type == 'gallery':
            GalleryRu.objects.get(pk=pk).delete()
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ConnectionRuListAPIView(ListAPIView):
    queryset = ConnectionRu.objects.all()
    serializer_class = ConnectionRuSerializer

class LastRuNNewsAPIView(APIView):
    def get(self, request, n, *args, **kwargs):
        """
        Retrieve the last 'n' news_ru articles.
        """
        try:
            n = int(n)  # Ensure 'n' is an integer
            news_queryset = NewsRu.objects.order_by('-added_date')[:n]
            serializer = NewsRuSerializer(news_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )


class GovernanceRuListAPIView(ListAPIView):
    queryset = GovernanceRu.objects.all()
    serializer_class = GovernanceRuSerializer


class ResolutionRuListAPIView(ListAPIView):
    queryset = ResolutionRu.objects.all()
    serializer_class = ResolutionRuSerializer


class ProvisionRuListAPIView(ListAPIView):
    queryset = ProvisionRu.objects.all()
    serializer_class = ProvisionRuSerializer

class NewsRuListAPIView(ListAPIView):
    queryset = NewsRu.objects.all()
    serializer_class = NewsRuSerializer

class GalleryRuListAPIView(ListAPIView):
    queryset = GalleryRu.objects.all()
    serializer_class = GalleryRuSerializer