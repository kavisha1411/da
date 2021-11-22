from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer
from .models import Artist, Song, Album


'''class SongList(APIView):

	serializer_class = SongSerializer

	def get(self, request):
		properties = Song.objects.all()
		serializer = SongSerializer(properties, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		name = request.data['name']
		album = request.data['album']
		artist = request.data['artist']
		
		serializer = SongSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):

	serializer_class = SongSerializer
	permission_classes = [AllowAny]
	def get(self, request, id):
		try:
			propertyInstance = Song.objects.get(id=id)
		except:
			raise RuntimeError("Instance not created successfully!")
			
		# propertyInstance = get_object_or_404(PropertyInfo, pk=pk)
		serializer = SongSerializer(propertyInstance)
		return Response(serializer.data)
		
	permission_classes = [IsAuthenticated]
	def put(self, request, id):
		propertyInstance = Song.objects.get(id=id)
		serializer = SongSerializer(instance=propertyInstance, data = request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
		
	permission_classes = [AllowAny]	
	def patch(self, request, id):
		propertyInstance = Song.objects.get(id=id)
		serializer = SongSerializer(instance=propertyInstance, data = request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, id):
		propertyInstance = Song.objects.get(id=id)
		propertyInstance.delete()	
		return Response(status=status.HTTP_200_OK)'''



from rest_framework import viewsets

class SongApi(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

	def perform_create(self, serializer):
		serializer.save()

	def perform_update(self, serializer):
		print("Perform update")

	def perform_destroy(self, instance):
		print("Perform destroy")


class AlbumApi(viewsets.ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer


class ArtistApi(viewsets.ModelViewSet):
	queryset = Artist.artists.all()
	serializer_class = ArtistSerializer