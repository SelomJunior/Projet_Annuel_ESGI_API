# appname/serializers.py, this file was created manually
from rest_framework import serializers
from .models import *


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


class ProfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class PlayerCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(last_name=validated_data['lastname'],
                    first_name=validated_data['firstname'],
                    email=validated_data['mail'], username=validated_data['mail'])

        player = Player(position=validated_data['position'],
                        foot=validated_data['foot'],
                        phone=validated_data['phone'], team=validated_data['team'])

        user.save()
        player.user = user
        player.save()

        return player

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
