from django.urls import path,include
from . views import PollList, PollDetail,ChoiceList,UserCreate,LoginView,AllUsers,LogoutUser
from rest_framework.routers import DefaultRouter
from . views import PollViewSet

# router = DefaultRouter()
# router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
path("polls/", PollList.as_view(), name="polls_list"),
path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
# path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
path("users/", UserCreate.as_view(), name="user_create"),
path("login/", LoginView.as_view(), name="login"),
path('allusers/',AllUsers.as_view(),name="allusers"),
path('logout/',LogoutUser.as_view(),name="logout"),

]

# urlpatterns += router.urls #other choice for line 10,11