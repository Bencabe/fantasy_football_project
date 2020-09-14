from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LeagueForm
from django.utils import timezone
from .models import League
from datetime import datetime
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("This is a test page")


def test(request):
    return HttpResponse("This is a test page")

def create_league(request):
    # League.objects.all().delete()
    template_to_include = 'create_league/private_league.html'
    # template = request.GET['template']
    # print(request.GET)
        # print(request.GET['template'])
    # print(template_to_include)
    if request.method == 'POST':
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
            u = User.objects.get(id=1)
            l.players_in_league.add(u)
            l.save()

            return HttpResponse("It Worked " + str(league.id) + " " +str(request.user) + " " + str(request.user.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeagueForm()
    
    return render(request,"create_league/create_league.html",{'template_to_include': template_to_include,'form':form})


def change_template(request,template):
    template = 'create_league/' + template + '.html'
    form = LeagueForm()
    return render(request,template,{'form':form})

def leagues(request):
    leagues = request.user.league_set.all()
    return render(request,'leagues/leagues_main.html',{'leagues':leagues})

def change_template_leagues(request,template,league):
    template = 'leagues/' + template + '.html'
    selected_league = League.objects.get(id=league)
    info = {'id': selected_league.id}
    return render(request,template,{'info':info})