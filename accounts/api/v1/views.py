from rest_framework import generics ,status
from . serializers import RgisterApiSerializer,CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token 


class RgisterApiViews(generics.GenericAPIView):
    serializer_class = RgisterApiSerializer

    def post(self, request, *args, **kwargs):
        serializer = RgisterApiSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {"email": serializer.validated_data["email"]}
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    

class CustomObtainAuthToken(ObtainAuthToken):
        serializer_class = CustomAuthTokenSerializer
        def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })