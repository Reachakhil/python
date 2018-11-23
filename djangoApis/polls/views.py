from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from .models import Poll,Choice
from .serializers import PollSerializer,ChoiceSerializer,UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from rest_framework import generics,status
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



# 3RD WAY ! USING GENERIC VIEWS normal crud
						#get and post
# class PollList(generics.ListCreateAPIView): 
# 	queryset = Poll.objects.all()
# 	serializer_class = PollSerializer


									#get and delete
# class PollDetail(generics.RetrieveDestroyAPIView): #retrievedestroy means del and get
# 	queryset = Poll.objects.all()
# 	serializer_class = PollSerializer


#2nd WAY WITHOUT THE GENERIC VIEWS when you wanna customize the apis
class PollList(APIView):
	
	def get(self, request):
		polls = Poll.objects.all()[:20]
		serializedata = PollSerializer(polls, many=True)
		return Response(serializedata.data)
	def post(self,request,format=None):
		serializer=PollSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class PollDetail(APIView):

	

	def get(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		serializedata = PollSerializer(poll)
		return Response(serializedata.data)

	def put(self,request,pk,format=None):
		poll=get_object_or_404(Poll,pk=pk)
		serializer=PollSerializer(poll,data=request.data)
		if serializer.is_valid():
			serializer.save()
			data=serializer.data
			return Response({"message":"succesfully changed data","data":data})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		poll=get_object_or_404(Poll,pk=pk)
		poll.delete()
		data="deleted succesfully"
		return Response({"data":data})

	




class ChoiceList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
		return queryset
	serializer_class = ChoiceSerializer


# class CreateVote(APIView):
# 	def post(self, request, pk, choice_pk):
# 		voted_by = request.data.get("voted_by")
# 		print(vote)
# 		data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
# 		serializer = VoteSerializer(data=data)
# 		if serializer.is_valid():
# 			vote = serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollViewSet(viewsets.ModelViewSet):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer



class UserCreate(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer


class LoginView(APIView):
	permission_classes = ()
	def post(self, request,):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)
		if user:
			token, _ = Token.objects.get_or_create(user=user)#two variables the
			#second variable is a bolean value.
			print(username)
			return Response({"token": token.key})
		else:
			return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class SuperUser(APIView):
	def post(self,request):
		username = request.data.get("username")
		password = request.data.get("password")


class AllUsers(APIView):
	def get(self,request,format=None):
		user=User.objects.all()
		serializer=UserSerializer(user,many=True)
		return Response(serializer.data)

class LogoutUser(APIView): #simply delete the token to force a login
	def get(self, request, format=None):
		request.user.auth_token.delete() 
		return Response({"message":"logout"})




































#  1ST WAY NORMAL DJANGO VIEWS, 
# def polls_list(request):
# 	MAX_OBJECTS = 20
# 	polls = Poll.objects.all()[:MAX_OBJECTS]
# 	data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
# 	# return HttpResponse(polls)
# 	return JsonResponse(data)

# def polls_detail(request, pk):
# 	poll = get_object_or_404(Poll, pk=pk)
# 	data = {"results": {
# 	"question": poll.question,
# 	"created_by": poll.created_by.username,
# 	"pub_date": poll.pub_date
# 	}}
# 	return JsonResponse(data)


