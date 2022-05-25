from rest_framework.renderers import JSONRenderer
from users.api.serializers import UserSerializer
from rest_framework.views import APIView
from django.views.generic import View
from django.http import HttpResponse
from itsdangerous import Serializer
from users.models import User
from yaml import serialize

class UserListAPI (APIView):
    def get(self, reuest):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        # users_json = JSONRenderer().render(serializer.data)     
         
        return HttpResponse (serializer.data)  
    
    def post(self, reuest):

        return Response ("Todo ok")  
     
        