from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from news_oz.models import NewsOz, GalleryOz, ConnectionOz, ResolutionOz, GovernanceOz, ProvisionOz
from news_oz.serializers import NewsOzSerializer, GalleryOzSerializer, ConnectionOzSerializer, ProvisionOzSerializer, \
    ResolutionOzSerializer, GovernanceOzSerializer


class CombinedOzSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        # Search in News
        news_queryset = NewsOz.objects.all()
        if search_query:
            news_queryset = news_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        news_serializer = NewsOzSerializer(news_queryset, many=True)

        # Search in Gallery
        gallery_queryset = GalleryOz.objects.all()
        if search_query:
            gallery_queryset = gallery_queryset.filter(
                Q(title__icontains=search_query)
            )

        gallery_serializer = GalleryOzSerializer(gallery_queryset, many=True)

        return Response({
            'news_ru': news_serializer.data,
            'galleries': gallery_serializer.data
        })

    def post(self, request):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            serializer = NewsOzSerializer(data=request.data)
        elif data_type == 'gallery':
            serializer = GalleryOzSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        data_type = request.data.get('type')
        if data_type == 'news_ru':
            instance = NewsOz.objects.get(pk=pk)
            serializer = NewsOzSerializer(instance, data=request.data)
        elif data_type == 'gallery':
            instance = GalleryOz.objects.get(pk=pk)
            serializer = GalleryOzSerializer(instance, data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_type = request.GET.get('type')
        if data_type == 'news_ru':
            NewsOz.objects.get(pk=pk).delete()
        elif data_type == 'gallery':
            GalleryOz.objects.get(pk=pk).delete()
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ConnectionOzListAPIView(ListAPIView):
    queryset = ConnectionOz.objects.all()
    serializer_class = ConnectionOzSerializer

class LastOzNNewsAPIView(APIView):
    def get(self, request, n, *args, **kwargs):
        """
        Retrieve the last 'n' news_ru articles.
        """
        try:
            n = int(n)  # Ensure 'n' is an integer
            news_queryset = NewsOz.objects.order_by('-added_date')[:n]
            serializer = NewsOzSerializer(news_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )


class GovernanceOzListAPIView(ListAPIView):
    queryset = GovernanceOz.objects.all()
    serializer_class = GovernanceOzSerializer


class ResolutionOzListAPIView(ListAPIView):
    queryset = ResolutionOz.objects.all()
    serializer_class = ResolutionOzSerializer


class ProvisionOzListAPIView(ListAPIView):
    queryset = ProvisionOz.objects.all()
    serializer_class = ProvisionOzSerializer

class NewsOzListAPIView(ListAPIView):
    queryset = NewsOz.objects.all()
    serializer_class = NewsOzSerializer

class GalleryOzListAPIView(ListAPIView):
    queryset = GalleryOz.objects.all()
    serializer_class = GalleryOzSerializer