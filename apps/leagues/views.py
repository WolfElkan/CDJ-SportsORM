# - - - - - IMPORTS - - - - -

from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker
from django.db.models import Q, Count

# - - - - - HELPER FUNCTIONS - - - - -

def team_id(location,team_name):
	query = Q(location=location)&Q(team_name=team_name)
	return Team.objects.get(query).id

def player_id(first_name,last_name):
	query = Q(first_name=first_name)&Q(last_name=last_name)
	return Player.objects.get(query).id	

# - - - - - VIEWS - - - - -

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

# - - - - - QUESTION DIRECTORY - - - - -

def levels(request, level, question):
	if level == "1":
		return L1(request, question)
	elif level == "2":
		return L2(request, question)
	elif level == "3":
		return L3(request, question)
	else:
		print "Only 3 levels"
		return redirect ('/')

def L1(request, question):
	if question == "1":
		return L1Q1(request)
	elif question == "2":
		return L1Q2(request)
	elif question == "3":
		return L1Q3(request)
	elif question == "4":
		return L1Q4(request)
	elif question == "5":
		return L1Q5(request)
	elif question == "6":
		return L1Q6(request)
	elif question == "7":
		return L1Q7(request)
	elif question == "8":
		return L1Q8(request)
	elif question == "9":
		return L1Q9(request)
	elif question == "10":
		return L1Q10(request)
	elif question == "11":
		return L1Q11(request)
	elif question == "12":
		return L1Q12(request)
	elif question == "13":
		return L1Q13(request)
	elif question == "14":
		return L1Q14(request)
	elif question == "15":
		return L1Q15(request)
	elif question == "16":
		return L1Q16(request)
	else:
		print "Only 16 questions in Level 1"
		return redirect ('/')

def L2(request, question):
	if question == "1":
		return L2Q1(request)
	elif question == "2":
		return L2Q2(request)
	elif question == "3":
		return L2Q3(request)
	elif question == "4":
		return L2Q4(request)
	elif question == "5":
		return L2Q5(request)
	elif question == "6":
		return L2Q6(request)
	elif question == "7":
		return L2Q7(request)
	elif question == "8":
		return L2Q8(request)
	else:
		print "Only 8 questions in Level 2"
		return redirect ('/')

def L3(request, question):
	if question == "1":
		return L3Q1(request)
	elif question == "2":
		return L3Q2(request)
	elif question == "3":
		return L3Q3(request)
	elif question == "4":
		return L3Q4(request)
	elif question == "5":
		return L3Q5(request)
	elif question == "6":
		return L3Q6(request)
	elif question == "7":
		return L3Q7(request)
	else:
		print "Only 7 questions in Level 3"
		return redirect ('/')

# - - - - - LEVEL 1 - - - - -

# 1. Find all baseball leagues 
def L1Q1(request):
	context = {
		"leagues": League.objects.filter(sport="Baseball"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 2. Find all womens' leagues 
def L1Q2(request):
	context = {
		"leagues": League.objects.filter(name__icontains="women"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 3. Find all leagues where sport is any type of hockey 
def L1Q3(request):
	context = {
		"leagues": League.objects.filter(name__icontains="hockey"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 4. Find all leagues where sport is something OTHER THAN football 
def L1Q4(request):
	context = {
		"leagues": League.objects.exclude(name__icontains="football"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 5. Find all leagues that call themselves "conferences" 
def L1Q5(request):
	context = {
		"leagues": League.objects.filter(name__contains="Conference"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 6. Find all leagues in the Atlantic region 
def L1Q6(request):
	context = {
		"leagues": League.objects.filter(name__contains="Atlantic"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 7. Find all teams based in Dallas 
def L1Q7(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(location="Dallas"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 8. Find all teams named the Raptors 
def L1Q8(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(team_name="Raptors"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 9. Find all teams whose location includes "City" 
def L1Q9(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(location__icontains="city"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 10. Find all teams whose names begin with "T" 
def L1Q10(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(team_name__startswith="T"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 11. Return all teams, ordered alphabetically by location 
def L1Q11(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.order_by('location'),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 12. Return all teams, ordered by team name in reverse alphabetical order 
def L1Q12(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.order_by('team_name').reverse(),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 13. Find every player with last name "Cooper" 
def L1Q13(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(last_name="Cooper"),
	}
	return render(request, "leagues/index.html", context)

# 14. Find every player with first name "Joshua" 
def L1Q14(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(first_name="Joshua"),
	}
	return render(request, "leagues/index.html", context)

# 15. Find every player with last name "Cooper" EXCEPT FOR Joshua 
def L1Q15(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
	}
	return render(request, "leagues/index.html", context)


# 16. Find all players with first name "Alexander" OR first name "Wyatt" 
def L1Q16(request):
	player_query = Q(first_name="Alexander")|Q(first_name="Wyatt")
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(player_query),
	}
	return render(request, "leagues/index.html", context)

# - - - - - LEVEL 2 - - - - -

# 1. Find all teams in the Atlantic Soccer Conference 
def L2Q1(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 2. Find all (current) players on the Boston Penguins 
def L2Q2(request):
	player_query = Q(curr_team__location="Boston")|Q(curr_team__team_name="Penguins")
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(player_query)
	}
	return render(request, "leagues/index.html", context)

# 3. Find all (current) players in the International Collegiate Baseball Conference 
def L2Q3(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")
	}
	return render(request, "leagues/index.html", context)

# 4. Find all (current) players in the American Conference of Amateur Football with last name "Lopez" 
def L2Q4(request):
	player_query = Q(curr_team__league__name="American Conference of Amateur Football")&Q(last_name="Lopez")
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(player_query)
	}
	return render(request, "leagues/index.html", context)

# 5. Find all football players 
def L2Q5(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(curr_team__league__name__icontains="football")
	}
	return render(request, "leagues/index.html", context)

# 6. Find all teams with a (current) player named "Sophia" 
def L2Q6(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(curr_players__first_name="Sophia"),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 7. Find all leagues with a (current) player named "Sophia" 
def L2Q7(request):
	context = {
		"leagues": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"teams": [" "],
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 8. Find everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders 
def L2Q8(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(last_name="Flores")
		.exclude(curr_team__id=team_id("Washington","Roughriders"))
	}
	return render(request, "leagues/index.html", context)

# - - - - - LEVEL 3 - - - - - 

# 1. Find all teams, past and present, that Samuel Evans has played with 
def L3Q1(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(all_players__id=player_id("Samuel","Evans")),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 2. Find all players, past and present, with the Manitoba Tiger-Cats 
def L3Q2(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(all_teams__id=team_id("Manitoba","Tiger-Cats")),
	}
	return render(request, "leagues/index.html", context)

# 3. Find all players who were formerly (but aren't currently) with the Wichita Vikings
def L3Q3(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(all_teams__id=team_id("Wichita","Vikings"))
		.exclude(curr_team__id=team_id("Wichita","Vikings"))
	}
	return render(request, "leagues/index.html", context)

# 4. Find every team that Jacob Gray played for before he joined the Oregon Colts 
def L3Q4(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.filter(all_players__id=player_id("Jacob","Gray"))
		.exclude(id=team_id("Oregon","Colts")),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 5. Find everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players 
def L3Q5(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.filter(first_name="Joshua")
		.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
	}
	return render(request, "leagues/index.html", context)

# 6. Find all teams that have had 12 or more players, past and present.  
# (HINT: Look up the Django `annotate` function.) 
def L3Q6(request):
	context = {
		"leagues": [" "],
		"teams": Team.objects.annotate(nPlayers=Count('all_players')).filter(nPlayers__gte=12),
		"players": [" "],
	}
	return render(request, "leagues/index.html", context)

# 7. Show all players, sorted by the number of teams they've played for 
def L3Q7(request):
	context = {
		"leagues": [" "],
		"teams": [" "],
		"players": Player.objects.annotate(nTeams=Count('all_teams')).order_by('nTeams')
	}
	return render(request, "leagues/index.html", context)
