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
    home_goal = models.IntegerField(null=True)
    away_goal = models.IntegerField(null=True)
    state = models.IntegerField(null=True)

    class Meta:
        db_table = 'match'


class League(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'statia_league'


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
    birthdate = models.DateField(blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True, null=True)
    foot = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    postal_code = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    incharge_name = models.CharField(max_length=45, blank=True, null=True)
    incharge_phone = models.CharField(max_length=45, blank=True, null=True)
    incharge_mail = models.CharField(max_length=45, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='team', blank=True, null=True, related_name='+')
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user', blank=True, null=True, related_name='+')
    name = ""
    firstname = ""

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
    fautes_subie = models.IntegerField()
    penaltys_obtenue = models.IntegerField()
    corners_obtenue = models.IntegerField()
    ballons_concedes = models.IntegerField()
    hors_jeux = models.IntegerField()
    nombre_tirs = models.IntegerField()
    tirs_cadres = models.IntegerField()
    tirs_contres = models.IntegerField()
    buts_inscrits = models.IntegerField()
    buts_jeux = models.IntegerField()
    buts_penalty = models.IntegerField()
    buts_arretes = models.IntegerField()
    passes_tente = models.IntegerField()
    passe_reussis = models.IntegerField()
    centre_tente = models.IntegerField()
    centre_reussis = models.IntegerField()

    class Meta:
        db_table = 'stats_match'


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
    player = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='player', blank=True, null=True, related_name='+')
    button = models.IntegerField(blank=True)
    x = models.FloatField()
    y = models.FloatField()
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE, db_column='composition', blank=True, null=True, related_name='+')
    poste = models.ForeignKey(Poste, on_delete=models.DO_NOTHING, db_column='poste', blank=True, null=True, related_name='+')
    is_sub = models.IntegerField(blank=True, default=0)
    class Meta:
        db_table = 'composition_details'

