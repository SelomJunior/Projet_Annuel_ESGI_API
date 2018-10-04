# appname/serializers.py, this file was created manually
from rest_framework import serializers
from .models import *
from django.http import JsonResponse




class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'  #('name', 'city', 'department', 'stadename', 'address', 'creationdate')


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    club = ClubSerializer(many=False, read_only=True)
    league = LeagueSerializer(many=False)

    class Meta:
        model = Team
        fields = '__all__'


class TypeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUser
        fields = '__all__'


class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
#        fields = '__all__'
        extra_kwargs = {
            'username': {'validators': []},
        }



class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class PlayerCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    def create(self, validated_data):
        testUser = User.objects.all().filter(username=self.initial_data['mail']).first()

        if testUser is not None:
            player = Player()
            player.position = "duplicata"
            player.user = testUser

            return player

        user = User(last_name=validated_data['user']['last_name'],
                    first_name=validated_data['user']['first_name'],
                    email=validated_data['user']['email'], username=validated_data['user']['email'])

        player = Player(position=validated_data['position'],
                        foot=validated_data['foot'],
                        phone=validated_data['phone'], team=validated_data['team'],birthdate=validated_data['birthdate'])


        user.save()
        player.user = user
        player.save()

        return player

    def update(self, instance, validated_data):
        testUser = User.objects.all().filter(username=validated_data['user']['username']).first()
        if testUser is not None:
            testUser.first_name = validated_data['user']['first_name']
            testUser.last_name = validated_data['user']['last_name']
            testUser.save()

            player = Player.objects.all().filter(user=testUser.id).first()
            player.birthdate = validated_data['birthdate']
            player.phone = validated_data['phone']
            player.position = validated_data['position']
            player.foot = validated_data['foot']
            player.save()
        return player




    class Meta:
        model = Player
        fields = '__all__'


class PlayerUpdateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return validated_data

    class Meta:
        model = Player
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Coach
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    home = TeamSerializer(many=False)
    away = TeamSerializer(many=False)
    tournament = CompetitionSerializer(many=False)

    class Meta:
        model = Match
        fields = '__all__'


class MatchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'


class PlayerCustomSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class CompositionSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)

    class Meta:
        model = Composition
        fields = '__all__'


class CompositionCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        compo = Composition.objects.all().filter(team=validated_data['team']).filter(name=validated_data['name']).first()
        if compo is not None:
            compo.name = ""
            compo.team = None
            return compo
        else:
            compo = Composition(name=validated_data['name'], team=validated_data['team'])
            compo.save()
        return compo

    class Meta:
        model = Composition
        fields = '__all__'


class CompositionDetailSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(many=False)
    composition = CompositionSerializer(many=False)
    poste = PosteSerializer(many=False)

    class Meta:
        model = CompositionDetail
        fields = '__all__'


class CompositinoDetailSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = CompositionDetail
        fields = '__all__'


class AnalystSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Analyst
        fields = '__all__'


class AnalystCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Analyst
        fields = '__all__'

class StatistiquesMatchSerializer(serializers.ModelSerializer):
    match = MatchSerializer(many=False)
    team = TeamSerializer(many=False)
    #analyst = AnalystSerializer(many=False)

    class Meta:
        model = StatistiquesMatch
        fields = '__all__'


class StatistiquesMatchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatistiquesMatch
        fields = '__all__'


class MatchEventPlayerSerializer(serializers.ModelSerializer):
    statsMatch = StatistiquesMatchSerializer(many=False)
    player = PlayerSerializer(many=False)

    class Meta:
        model = MatchEventPlayer
        fields = '__all__'

class MatchEventPlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchEventPlayer
        fields = '__all__'



class StatsMatchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatistiquesMatchInfo
        fields = '__all__'



class CategorieStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategorieStats
        fields = '__all__'


class StatistiqueInfoSerializer(serializers.ModelSerializer):
    categorie = CategorieStatSerializer(many=False)
    class Meta:
        model = StatistiqueInfo
        fields = '__all__'


class StatsMatchInfoSerializerGet(serializers.ModelSerializer):
    statistiques_match = StatistiquesMatchSerializer(many=False)
    stats_info = StatistiqueInfoSerializer(many=False)

    class Meta:
        model = StatistiquesMatchInfo
        fields = '__all__'


class CompositionHistorySerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    match = MatchSerializer(many=False)

    class Meta:
        model = CompositionHistory
        fields = '__all__'


class CompositionHistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompositionHistory
        fields = '__all__'
