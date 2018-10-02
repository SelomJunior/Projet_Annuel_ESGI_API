from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse ,Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from django.db.models import Q


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return PlayerCreateSerializer
        else:
            return PlayerSerializer


class TypeUserViewSet(viewsets.ModelViewSet):
    queryset = TypeUser.objects.all()
    serializer_class = TypeUserSerializer

    def get_queryset(self):
        return TypeUser.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnalystViewSet(viewsets.ModelViewSet):
    queryset = Analyst.objects.all()
    serializer_class = AnalystSerializer

    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return AnalystCreateSerializer
        else:
            return AnalystSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return MatchCreateSerializer
        else:
            return MatchSerializer


class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer


class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class StatistiquesMatchViewSet(viewsets.ModelViewSet):
    queryset = StatistiquesMatch.objects.all()
    serializer_class = StatistiquesMatchSerializer

    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return StatistiquesMatchCreateSerializer
        else:
            return StatistiquesMatchSerializer

class MatchEventPlayerViewSet(viewsets.ModelViewSet):
    queryset = MatchEventPlayer.objects.all()
    serializer_class = MatchEventPlayerSerializer

    def create(self, request, *args, **kwargs):
        if type(request.data) is list:
            for data in request.data:
                data['player'] = Player(idplayer=data['player'])
                data['statsMatch'] = StatistiquesMatch(idStatistiquesMatch=data['statsMatch'])
                event = MatchEventPlayer(**data)
                event.save()
            return JsonResponse(status=200, data=True, safe=False)
    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return MatchEventPlayerCreateSerializer
        else:
            return MatchEventPlayerSerializer

class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return CompositionCreateSerializer
        else:
            return CompositionSerializer


class CompositionDetailViewSet(viewsets.ModelViewSet):
    queryset = CompositionDetail.objects.all()
    serializer_class = CompositionDetailSerializer

    def create(self, request, *args, **kwargs):
        compodetail = CompositionDetail.objects.all().filter(composition=request.data["composition"]).filter(button=request.data["button"]).first()
        playertoadd = Player()
        if compodetail:
            if request.data["player"] != "":
                playertoadd = Player.objects.all().filter(idplayer=request.data["player"]).first()
                playertoadd.save()
                compodetail.player = playertoadd
            else:
                compodetail.player = None
            if request.data["poste"] != "":
                poste = Poste.objects.all().filter(id=request.data["poste"]).first()
                poste.save()
                compodetail.poste = poste
            else:
                compodetail.poste = None

            compodetail.x = request.data["x"]
            compodetail.y = request.data["y"]
            compodetail.is_sub = request.data["is_sub"]
            compodetail.save()
            return JsonResponse(status=200, data=CompositionDetailSerializer(compodetail, many=False).data, safe=False)
        else:
            compo = Composition.objects.all().filter(id=request.data["composition"]).first()
            compod = CompositionDetail(x=request.data["x"], y=request.data["y"],composition=compo,
                                       button=request.data["button"], is_sub=request.data["is_sub"])
            if request.data["player"] != "":
                playertoadd = Player.objects.all().filter(idplayer=request.data["player"]).first()
                playertoadd.save()
                compod.player = playertoadd

            if request.data["poste"] != "":
                poste = Poste.objects.all().filter(id=request.data["poste"]).first()
                poste.save()
                compod.poste = poste
            compod.save()
            return  JsonResponse(status=200, data=CompositionDetailSerializer(compod, many=False).data, safe=False)

    def get_serializer_class(self):
        if self.action == "post" or self.action == "create" or self.action == "update":
            return CompositinoDetailSerializerCreate
        else:
            return CompositionDetailSerializer


class SettingsBackend:

    def authenticate(self, request, username=None, password=None):
        username = request.data["username"]
        user = User.objects.get(email=username)

        if user is not None:
            if user.check_password(request.data["password"]):
                return user
            else:
                return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



class LoginView(APIView):

    def post(self, request, fortmat=None):
        data = request.data
        print(data['username'])
        print(data['password'])
        try:
            user = SettingsBackend.authenticate(self=self, request=request, username=data['username'], password=data['password'])
        except Exception as e:
            return JsonResponse(status=400, data=False, safe=False)
        
        print(user.id)
        if user is not None:
            try:
                analyst = Analyst.objects.all().get(user=user.id)
                if analyst is not None:
                    print("here ?")
                    serializer = AnalystSerializer(analyst, many=False)
                    return JsonResponse(serializer.data, safe=False)
                else:
                    return JsonResponse(status=200, data=False, safe=False)
            except:
                try:
                    coach = Coach.objects.all().get(user=user.id)
                    if coach is not None:
                        print("here 2 ?")
                        serializer = CoachSerializer(coach, many=False)
                        return JsonResponse(serializer.data, safe=False)
                    else:
                        return JsonResponse(status=200, data=False, safe=False)
                except:
                    try:
                        player = Player.objects.all().get(user=user.id)
                        if player is not None:
                            serializer = PlayerSerializer(player, many=False)
                            return JsonResponse(serializer.data, safe=False)
                        else:
                            return JsonResponse(status=200, data=False, safe=False)
                    except:
                        return JsonResponse(status=401, data=False, safe=False)
        else:
            return JsonResponse(status=402, data=False, safe=False)


class Playerbyteam(APIView):
    def get_object(self, pk):
        try:
            #player = Player.objects.raw('SELECT * FROM player WHERE team = %s', [pk])
            # Player.objects.all().filter(team=pk)
            return Player.objects.all().filter(team=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = PlayerCustomSerializer(player, many=True)
        return Response(serializer.data)


class TeambyClub(APIView):
    def get_object(self, pk):
        try:
            #teams = Team.objects.raw('SELECT * FROM team WHERE club  = %s', [pk])
            # Player.objects.all().filter(team=pk)
            return Team.objects.all().filter(club=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)


class matchToAnalyze(APIView):
    def get(self,request, format=None):
        match = Match.objects.all().filter(state=0).order_by('date')
        serializer = MatchSerializer(match, many=True)
        return Response(serializer.data)

class matchByTeam(APIView):
    def get(self,request, pk, format=None):
        match = Match.objects.all().filter(Q(home=pk) | Q(away=pk)).order_by('date')
        serializer = MatchSerializer(match, many=True)
        return Response(serializer.data)


class matchByTeamAndCompetition(APIView):
    def get(self,request, idteam, idcompet, format=None):
        match = Match.objects.all().filter(Q(home=idteam) | Q(away=idteam)).filter(tournament=idcompet).order_by('date')
        serializers = MatchSerializer(match, many=True)
        return Response(serializers.data)


class teamByLeague(APIView):
    def get(self,request, idLeague, format=None):
        team = Team.objects.all().filter(league=idLeague)
        serializers = TeamSerializer(team, many=True)
        return Response(serializers.data)


class getCompoByTeam(APIView):
    def get(self, request, idTeam, Format=None):
        compo = Composition.objects.all().filter(team=idTeam)
        serializers = CompositionSerializer(compo, many=True)
        return Response(serializers.data)


class getCompoDetailByCompo(APIView):
    def get(self, request, idCompo, Format=None):
        compodetail = CompositionDetail.objects.all().filter(composition=idCompo)
        serializers = CompositionDetailSerializer(compodetail, many=True)
        return Response(serializers.data)