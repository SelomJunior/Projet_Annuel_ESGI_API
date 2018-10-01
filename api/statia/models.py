from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Club(models.Model):
    idclub = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)
    stadename = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    creationdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'club'


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)


class Coach(models.Model):
    idcoach = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, models.DO_NOTHING, db_column='user', blank=True, null=True,related_name='+')
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team', blank=True, null=True,related_name='+')

    class Meta:
        db_table = 'coach'


class Match(models.Model):
    idmatch = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    tournament = models.ForeignKey('Competition', models.DO_NOTHING, db_column='competition', blank=True,null=True, related_name='+')
    day = models.CharField(max_length=45, blank=True, null=True)
    home = models.ForeignKey('Team', models.DO_NOTHING, db_column='home', blank=True, null=True, related_name='+')
    away = models.ForeignKey('Team', models.DO_NOTHING, db_column='away', blank=True, null=True, related_name='+')
    home_goal = models.IntegerField(null=True, default=0)
    away_goal = models.IntegerField(null=True, default=0)
    state = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = 'match'


class League(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)


class Poste(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=30, blank=True, null=True)
    cote = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.role, self.cote)

    class Meta:
        db_table = 'poste'


class Player(models.Model):
    idplayer = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    foot = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    mail = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    incharge_name = models.CharField(max_length=45, blank=True, null=True)
    incharge_phone = models.CharField(max_length=45, blank=True, null=True)
    incharge_mail = models.CharField(max_length=45, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team', blank=True, null=True, related_name='+')
    user = models.OneToOneField(User, models.DO_NOTHING, db_column='user', blank=True, null=True, related_name='+')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


    class Meta:
        db_table = 'player'


class StatiaPlayers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)

    class Meta:
        db_table = 'statia_players'



class StatsPlayerMatch(models.Model):
    idstats_player_match = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='player', blank=True, null=True, related_name='+')
    match = models.ForeignKey(Player, models.DO_NOTHING, db_column='match', blank=True, null=True, related_name='+')

    class Meta:
        db_table = 'stats_player_match'


class Team(models.Model):
    idteam = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    league = models.ForeignKey('League', models.DO_NOTHING, db_column='match', blank=True, null=True, related_name='+')
    club = models.ForeignKey(Club,models.DO_NOTHING,db_column='club',blank=True,null=True,related_name='+')

    def __str__(self):
        return '%s : %s' % (self.name, self.club)

    class Meta:
        db_table = 'team'


class TypeUser(models.Model):
    idtypeuser = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)

    class Meta:
        db_table = 'typeuser'


class Profil(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, models.DO_NOTHING)
    name = models.CharField(max_length=45, blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        db_table = 'profil'


class Video(models.Model):
    idvideo = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=45, blank=True, null=True)
    match = models.ForeignKey(Match, models.DO_NOTHING, db_column='match', blank=True, null=True, related_name='+')

    class Meta:
        db_table = 'video'


class Competition(models.Model):
    idCompetition = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition'



class StatistiquesMatch(models.Model):
    idStatistiquesMatch = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match,models.DO_NOTHING, db_column='match', blank=True, null=True, related_name='+')
    team = models.ForeignKey(Team,models.DO_NOTHING, db_column='team', blank=True, null=True, related_name='+')
    possession = models.DecimalField(max_digits=5, decimal_places=2)
    passe_reussie = models.IntegerField()
    passe_ratee = models.IntegerField()
    duel_gagne = models.IntegerField()
    duel_perdu = models.IntegerField()
    centre_reussi = models.IntegerField()
    centre_rate = models.IntegerField()
    tir_cadre = models.IntegerField()
    tir_hors_cadre = models.IntegerField()
    tir_contre = models.IntegerField()
    corner_obtenu = models.IntegerField()
    ballon_concede = models.IntegerField()
    hors_jeu = models.IntegerField()
    interception = models.IntegerField()
    faute_commise = models.IntegerField()
    penalty_commis = models.IntegerField()
    degagement = models.IntegerField()

    class Meta:
        db_table = 'statsmatch'


class MatchEventPlayer(models.Model):
    idMatchEvent = models.AutoField(primary_key=True)
    statsMatch = models.ForeignKey(StatistiquesMatch,models.DO_NOTHING, db_column='statsMatch', blank=True, null=True,  related_name='+')
    player =  models.ForeignKey(Player,models.DO_NOTHING, db_column='player', blank=True, null=True,  related_name='+')
    minute = models.IntegerField()
    event = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'matcheventplayer'


class StatistiquesPlayer(models.Model):
    idStatistiquesPlayer = models.AutoField(primary_key=True)
    note = models.IntegerField()
    temps_de_jeu = models.IntegerField()
    tirs_cadres = models.IntegerField()
    tirs_tentes = models.IntegerField()
    buts_marques = models.IntegerField()
    passes_decisives = models.IntegerField()
    fautes_commises = models.IntegerField()
    carton_jaune = models.IntegerField
    carton_rouge = models.IntegerField()


    class Meta:
        db_table = 'stats_player'


class Composition(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, models.DO_NOTHING, db_column='team', blank=True, null=True, related_name='+')
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'composition'


class CompositionDetail(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='player', blank=True, null=True, related_name='+')
    button = models.IntegerField(blank=True)
    x = models.FloatField()
    y = models.FloatField()
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE, db_column='composition', blank=True, null=True, related_name='+')
    poste = models.ForeignKey(Poste, on_delete=models.DO_NOTHING, db_column='poste', blank=True, null=True, related_name='+')
    is_sub = models.IntegerField(blank=True, default=0)
    class Meta:
        db_table = 'composition_details'

