from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import NewsQa, GalleryQa, ConnectionQa, GovernanceQa, ResolutionQa, ProvisionQa
from .serializers import NewsQaSerializer, GalleryQaSerializer, ConnectionQaSerializer, GovernanceQaSerializer, \
    ResolutionQaSerializer, ProvisionQaSerializer


class CombinedQaSearchView(APIView):
    def get(self, request):
        search_query = request.GET.get('query', '').strip()

        # Search in News
        news_queryset = NewsQa.objects.all()
        if search_query:
            news_queryset = news_queryset.filter(
                Q(title__icontains=search_query) |
                Q(pre_description__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(author_position__icontains=search_query)
            )

        news_serializer = NewsQaSerializer(news_queryset, many=True)

        # Search in Gallery
        gallery_queryset = GalleryQa.objects.all()
        if search_query:
            gallery_queryset = gallery_queryset.filter(
                Q(title__icontains=search_query)
            )

        gallery_serializer = GalleryQaSerializer(gallery_queryset, many=True)

        return Response({
            'news_qa': news_serializer.data,
            'galleries': gallery_serializer.data
        })

    def post(self, request):
        data_type = request.data.get('type')
        if data_type == 'news_qa':
            serializer = NewsQaSerializer(data=request.data)
        elif data_type == 'gallery':
            serializer = GalleryQaSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        data_type = request.data.get('type')
        if data_type == 'news_qa':
            instance = NewsQa.objects.get(pk=pk)
            serializer = NewsQaSerializer(instance, data=request.data)
        elif data_type == 'gallery':
            instance = GalleryQa.objects.get(pk=pk)
            serializer = GalleryQaSerializer(instance, data=request.data)
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        data_type = request.GET.get('type')
        if data_type == 'news_qa':
            NewsQa.objects.get(pk=pk).delete()
        elif data_type == 'gallery':
            GalleryQa.objects.get(pk=pk).delete()
        else:
            return Response({'error': 'Invalid type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ConnectionQaListAPIView(ListAPIView):
    queryset = ConnectionQa.objects.all()
    serializer_class = ConnectionQaSerializer

class LastQaNNewsAPIView(APIView):
    def get(self, request, n, *args, **kwargs):
        """
        Retrieve the last 'n' news_qa articles.
        """
        try:
            n = int(n)  # Ensure 'n' is an integer
            news_queryset = NewsQa.objects.order_by('-added_date')[:n]
            serializer = NewsQaSerializer(news_queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                {"error": "Invalid value for 'n'. Must be an integer."},
                status=status.HTTP_400_BAD_REQUEST
            )


class GovernanceQaListAPIView(ListAPIView):
    queryset = GovernanceQa.objects.all()
    serializer_class = GovernanceQaSerializer


class ResolutionQaListAPIView(ListAPIView):
    queryset = ResolutionQa.objects.all()
    serializer_class = ResolutionQaSerializer


class ProvisionQaListAPIView(ListAPIView):
    queryset = ProvisionQa.objects.all()
    serializer_class = ProvisionQaSerializer

class NewsQaListAPIView(ListAPIView):
    queryset = NewsQa.objects.all()
    serializer_class = NewsQaSerializer

class GalleryQaListAPIView(ListAPIView):
    queryset = GalleryQa.objects.all()
    serializer_class = GalleryQaSerializer
