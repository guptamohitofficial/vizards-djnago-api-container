from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from vizards import views as viz
from user import views as userView
from card import views as cardView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', viz.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('request/token', obtain_auth_token, name='authToken'),
    path('validate/token', viz.WhoUser.as_view(), name='authUser'),
    path('user-auth', userView.userAuth, name="userAuth"),
    path('user-auth/logout', userView.logout, name="userLogout"),
    path('user-auth/login', userView.userAuthLogin.as_view(), name="userAuthLogin"),
    path('user-auth/signup', userView.userAuthSignup.as_view(), name="userAuthSignup"),
    path('logout', userView.logout, name="logout"),
    path('card', cardView.cardList.as_view(), name="cardList"),
    path('card/add-new-visiting-card', cardView.CreateVisitingCard.as_view(), name="CreateVisitingCard"),
    path('card/add-new-meeting-card', cardView.CreateMeetingCard.as_view(), name="CreateMeetingCard"),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]