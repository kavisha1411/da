from django.core.exceptions import PermissionDenied
from rest_framework import serializers
from .models import Song, Album, Artist

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
	songs = SongSerializer(many=True)

	def create(self, validated_data):
		songs_data = validated_data.pop('songs')
		album = Album.objects.create(**validated_data)
		for song_data in songs_data:
			Song.objects.create(album=album, **song_data)
		return album

	def update(self, instance, validated_data):
		song = instance.songs
		instance.name = validated_data.get('name', instance.name)
		instance.number_songs = validated_data.get('number_songs', instance.number_songs)
		instance.artist = validated_data.get('artist', instance.artist)
		instance.save()
		song.save()
		return instance

	def post(self, instance, validated_data):
		song = instance.songs

		pass

	def delete(self, instance, validated_data):
		if self.user.is_authenticated:
			instance.delete()
		else:
			raise PermissionDenied("Current user cannot delete.")


	class Meta:
		model = Album
		fields = ['id', 'name', 'number_songs', 'artist', 'songs']


class ArtistSerializer(serializers.ModelSerializer):
	songs = SongSerializer(many=True)
	music_album_related = AlbumSerializer(many=True)

	class Meta:
		model = Artist
		fields = ['name', 'surname', 'status', 'songs', 'music_album_related']
			
