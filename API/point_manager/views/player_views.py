from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PlayerSerializer
from ..models import Player
from ..permissions import IsAdminUser, IsRangerUser

class PlayerHandler(APIView):
    #get
    def get(self, request):
        if 'id' in request.data:
            try:
                player = Player.objects.get(id=request.data['id'])
                serializer = PlayerSerializer(player)
                return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
            except Player.DoesNotExist:
                return Response({'message': 'Player tidak ditemukan.'}, status=status.HTTP_404_NOT_FOUND)
        
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)
    
    #register
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()
    
    #update
    def patch(self, request):
        request_body = request.data
        player_id = request_body['id']
        name = request_body['name']
        get_player_obj = get_object_or_404(Player, pk=player_id)
        get_player_obj.name = name
        get_player_obj.save()
        return Response({
            "message" : str(get_player_obj) + " is successfully edited!",
        }, status=status.HTTP_200_OK)

    #delete
    def delete(self, request):
        request_body = request.data
        player_id = request_body['id']
        get_player_obj = get_object_or_404(Player, pk=player_id)
        get_player_obj.delete()
        return Response({
            "message" : str(get_player_obj) + " is successfully edited!",
        }, status=status.HTTP_200_OK)