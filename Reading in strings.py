home_team = input("Please enter what the home team is called: ").upper()
away_team = input("Please write what the away team is called: ").upper()

print("First leg")
print(home_team, "against", away_team)
print(home_team[0], home_team[1], home_team[2], ":", away_team[0], away_team[1], away_team[2])

temp_home_team = home_team # temp_home_team = banana
home_team = away_team # home_team = apple
away_team = temp_home_team # away_team = banana

print("Return leg")
print(home_team, "against", away_team)
print(home_team[0], home_team[1], home_team[2], ":", away_team[0], away_team[1], away_team[2])




