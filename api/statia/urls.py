# create this file
# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url
from rest_framework import routers
from api.statia.views import *

router = routers.DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
#router.register(r'profils', ProfilViewSet)
router.register(r'users',UserViewSet)
router.register(r'matchs',MatchViewSet)
router.register(r'typeuser', TypeUserViewSet)
router.register(r'poste', PosteViewSet)
router.register(r'coachs', CoachViewSet)
router.register(r'compositions', CompositionViewSet)
router.register(r'compositionsdetails', CompositionDetailViewSet)
router.register(r'statsmatch', StatistiquesMatchViewSet)
router.register(r'matcheventplayer', MatchEventPlayerViewSet)
router.register(r'statsinfoplayer', StatistiquesInfoPlayerViewSet)

urlpatterns = [
    url(r'playersbyteam/([0-9]+)$', Playerbyteam.as_view()),
    url(r'teambyClub/([0-9]+)$', TeambyClub.as_view()),
    url(r'login', LoginView.as_view()),
    url(r'matchbyteam/([0-9]+)$', matchByTeam.as_view()),
    url(r'matchbyteamandcompet/([0-9]+)/([0-9]+)$', matchByTeamAndCompetition.as_view()),
    url(r'teambyleague/([0-9]+)$', teamByLeague.as_view()),
    url(r'getcompobyteam/([0-9]+)$', getCompoByTeam.as_view()),
    url(r'getcomposdetails/([0-9]+)$', getCompoDetailByCompo.as_view()),
    url(r'getcompodefault', getComposByDefaut.as_view()),
    url(r'statsinfobyplayer/([0-9]+)$', getStatsInfoByPlayer.as_view())
]

urlpatterns += router.urls