from django.conf.urls import url, include
from rest_framework import routers
from accounts import api as accounts_api
from npcs import api as npc_api

router = routers.DefaultRouter()
# router.register(r'players', accounts_api.PlayerViewSet)
router.register(r'characters', npc_api.CharacterViewSet)
router.register(r'charactertypes', npc_api.CharacterTypeViewSet)

urlpatterns = [
    # Include the URLs dynamically generated by the router
    url(r'^', include(router.urls)),
    # Include the ability to log in to the browsable version
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]