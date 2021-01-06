from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .forms import LeagueForm, JoinLeagueForm
from django.utils import timezone
from .models import League, Team, DraftZone
from epl_players.models import Player
from datetime import datetime
from django.contrib.auth.models import User
import pytz
import json
# import asyncio

# for now just working with irish timezones
loc_timezone = pytz.timezone('Europe/Dublin')

def index(request):
    return HttpResponse("This is a test page")


def test(request):
    return HttpResponse("This is a test page")

def create_league(request):
    # function to create a new league
    template_to_include = 'create_league/private_league.html'
    if request.method == 'POST':
        print('team_name',request.POST['team_name'])
        # creating mutable post object so that we can modify datetime format to be compatible with the model
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['draft_date'] = request.POST['draft_date'].replace('T',' ')
        request.POST._mutable = mutable

        # create a form instance and populate it with data from the request:
        form = LeagueForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # create league with current date as the start date and user who created the league as league rep
            league = form.save(commit=False)
            league.league_rep = request.user
            league.start_date = timezone.now()
            l_id = league.id
            league.save()

            # add league rep as a member of the league
            l = League.objects.get(id=l_id)
            u = User.objects.get(id=request.user.id)
            l.players_in_league.add(u)
            l.save()
            # create league rep's team
            team = Team()
            team.name = request.POST['team_name']
            team.league = l
            team.user = u
            team.save()
            # create the draft zone
            dz = DraftZone()
            dz.league = l
            dz.save()

            return HttpResponse("It Worked " + str(league.id) + " " +str(request.user) + " " + str(request.user.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeagueForm()
        join_form = JoinLeagueForm()
    
    return render(request,"create_league/create_league.html",{'template_to_include': template_to_include,'form':form,'join_form':join_form})


def change_template(request,template):
    # function to return the correct template in the Create/Join League page
    template = 'create_league/' + template + '.html'
    form = LeagueForm()
    join_form = JoinLeagueForm()
    return render(request,template,{'form':form,'join_form':join_form})

def leagues(request):
    leagues = League.objects.filter(players_in_league=request.user)
    return render(request,'leagues/leagues_main.html',{'leagues':leagues})

def change_template_leagues(request,template,league):
     # function to return the correct template in the Leagues page
    template = 'leagues/' + template + '.html'
    # get league info
    selected_league = League.objects.get(id=league)
    draft_zone = DraftZone.objects.get(league=selected_league)

    # getting team players for team template
    user_team = Team.objects.get(user=request.user,league=league)
    team_players = user_team.players_chosen.all()
    info = {'id': selected_league.id}
    return render(request,template,{'info':info,'team_players':team_players})

def process_join_form(request):
    # function to process a user's request to join a private league
    if request.method == 'POST':
        team = Team()
        league = League.objects.get(id=request.POST['league'])
        user = User.objects.get(id=request.user.id)
        ''' add team based on form data. not using from.is_valid() & form.save()
        because I ran into problems around the form needing to be populated with a
        league instance instead of league id. Wasn't sure how to fix so did this but it's
        a bit hacky '''
        team.name = request.POST['team_name']
        team.league = league
        team.user = user
        team.save()

        league.players_in_league.add(user)
        league.save()
        return redirect('/draft/leagues/')

    message = "Didin't work"
    return HttpResponse("Didn't Work")

def draft_zone(request,league,player):
    # function to handle requests in the draft zone subsection of the leagues page

    # for not just working with irish timezone
    selected_league = League.objects.get(id=league)
    draft_zone = DraftZone.objects.get(league=selected_league)
    draft_date = draft_zone.league.draft_date

    if player != 'NA':
        selected_player = Player.objects.get(id=player)
        # if a player was picked in the draft zone add it to the list of selected players in the draft zone
        draft_zone.players_chosen.add(selected_player)
        draft_zone.save()
        # if a player was picked in the draft zone add it to the user's selected players
        user_team = Team.objects.get(user=request.user,league=league)
        user_team.players_chosen.add(selected_player)
        user_team.save()

    players_chosen = list(draft_zone.players_chosen.all().values_list('id',flat=True))
    print(draft_date,datetime.now(loc_timezone))
    print(draft_date<datetime.now(loc_timezone))
    if draft_date < datetime.now(loc_timezone):
        has_started = True
    else:
        has_started = False
    # create a dictionary with all data needed to render the template
    players = Player.objects.all()
    draft_date = draft_date.strftime("%b %d %Y %H:%M:%S")
    dz_data = {'players':players,
    'draft_zone':draft_zone,
    'players_chosen':players_chosen,
    'draft_date':draft_date,
    'has_started':has_started}

    return render(request,'leagues/draft_zone.html',{'dz_data':dz_data})


def check_data(request):
    league = request.GET['league']
    # function to handle requests in the draft zone subsection of the leagues page
    # first get the relevant league and a player selected by the user if appropriate
    selected_league = League.objects.get(id=league)
    # find relevant draft zone and add selected player to players chosen if appropriate
    draft_zone = DraftZone.objects.get(league=selected_league)
    players_chosen = draft_zone.players_chosen.all().values_list('id',flat=True)
    data = {'players_chosen':list(players_chosen)}
    return JsonResponse(data)