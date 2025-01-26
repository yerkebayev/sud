from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from news_uz.models import NewsUz, GalleryUz, ConnectionUz, ResolutionUz, GovernanceUz, ProvisionUz
from news_uz.serializers import NewsUzSerializer, GalleryUzSerializer, ConnectionUzSerializer, ProvisionUzSerializer, \
    ResolutionUzSerializer, GovernanceUzSerializer


class CombinedUzSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        # Search in News
        news_queryset = NewsUz.objects.all()
        if search_query:
            news_queryset = news_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        news_serializer = NewsUzSerializer(news_queryset, many=True)

        # Search in Gallery
        gallery_queryset = GalleryUz.objects.all()
        if search_query:
            gallery_queryset = gallery_queryset.filter(
                Q(title__icontains=search_query)
            )

        gallery_serializer = GalleryUzSerializer(gallery_queryset, many=True)

        return Response({
            'news_ru': news_serializer.data,
            'galleries': gallery_serializer.data
        })

    def post(self, request):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            serializer = NewsUzSerializer(data=request.data)
        elif data_type == 'gallery':
            serializer = GalleryUzSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            instance = NewsUz.objects.get(pk=pk)
            serializer = NewsUzSerializer(instance, data=request.data)
        elif data_type == 'gallery':
            instance = GalleryUz.objects.get(pk=pk)
            serializer = GalleryUzSerializer(instance, data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_type = request.GET.get('type')
        if data_type == 'news_ru':
            NewsUz.objects.get(pk=pk).delete()
        elif data_type == 'gallery':
            GalleryUz.objects.get(pk=pk).delete()
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ConnectionUzListAPIView(ListAPIView):
    queryset = ConnectionUz.objects.all()
    serializer_class = ConnectionUzSerializer

class LastUzNNewsAPIView(APIView):
    def get(self, request, n, *args, **kwargs):
        """
        Retrieve the last 'n' news_ru articles.
        """
        try:
            n = int(n)  # Ensure 'n' is an integer
            news_queryset = NewsUz.objects.order_by('-added_date')[:n]
            serializer = NewsUzSerializer(news_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )


class GovernanceUzListAPIView(ListAPIView):
    queryset = GovernanceUz.objects.all()
    serializer_class = GovernanceUzSerializer


class ResolutionUzListAPIView(ListAPIView):
    queryset = ResolutionUz.objects.all()
    serializer_class = ResolutionUzSerializer


class ProvisionUzListAPIView(ListAPIView):
    queryset = ProvisionUz.objects.all()
    serializer_class = ProvisionUzSerializer

class NewsUzListAPIView(ListAPIView):
    queryset = NewsUz.objects.all()
    serializer_class = NewsUzSerializer

class GalleryUzListAPIView(ListAPIView):
    queryset = GalleryUz.objects.all()
    serializer_class = GalleryUzSerializer