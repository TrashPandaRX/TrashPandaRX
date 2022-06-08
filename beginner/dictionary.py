player_info = {
    'gamer_tag' : 'wild_nips',
    'first_name' : 'jimmie',
    'last_name' : 'jawns'
}

for key, value in player_info.items():
    print(f"\nKey:  {key}")
    print(f"Value:  {value}")

player_high_scores = {
    'silver_toes': 5835,
    'rippley' : 4325,
    'xxGunzxx' : 2623,
    'jabaldoth' : 3143,
    'profile_yank' :1087
}

myFriends = ['wild_nips', 'jabaldoth']

for player in player_high_scores:
    score = player_high_scores[player]
    if player in myFriends:
        #score = player_high_scores[player]
        print(f"Congrats on a top score {player} with the score, {score}")
    else:
        #score = player_high_scores[player]
        print(f"{player}, got a highscore of {score}")

