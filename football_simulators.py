import random
import pandas as pd

teams = ["Brazil", "Argentina", "France", "Germany", "Spain", "England", "Portugal", "Italy"]
match_results = []

# Function to test the score input is valid or not
def get_valid_score(team):
    while True:
        try:
            score = int(input(f"Enter goals for {team}: "))
            if score >= 0:
                return score
            print("Score cannot be negative!")
        except ValueError:
            print("Please enter a valid number!")

# Function to simulate a match between two teams
def play_match(team1, team2, round_name):
    print(f"\nMatch: {team1} vs {team2}")
    score1 = get_valid_score(team1)
    score2 = get_valid_score(team2)
    
    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2
    else:
        winner = None
    
    match_results.append({
        "Round": round_name,
        "Team 1": team1,
        "Team 2": team2,
        "Score 1": score1,
        "Score 2": score2,
        "Winner": winner
    })
    
    # Handle draw with penalty shootout
    if score1 == score2:
        print("Draw! Enter penalty shootout scores.")
        pen_score1 = get_valid_score(team1)
        pen_score2 = get_valid_score(team2)
        if pen_score1 > pen_score2:
            winner = team1
        elif pen_score2 > pen_score1:
            winner = team2
        else:
            print("The result of penalty shootout is a tie! Let fate decide who wins (random)")
            winner = random.choice([team1, team2])
        match_results[-1]["Winner"] = winner
    
    return winner

# Function to save results table to Excel
def save_to_excel():
    df = pd.DataFrame(match_results)
    df.to_excel("tournament_results.xlsx", index=False)
    print("\nResults saved to tournament_results.xlsx")

# Function to simulate group stage
def play_group_stage(teams):
    random.shuffle(teams)
    group_a = teams[0:4]  # First 4 teams
    group_b = teams[4:8]  # Last 4 teams
    
    print("\n=== Group Stage ===")
    print("Group A: ", end="")
    for i in range(len(group_a)):
        if i > 0:
            print(", ", end="")
        print(group_a[i], end="")
    print("\nGroup B: ", end="")
    for i in range(len(group_b)):
        if i > 0:
            print(", ", end="")
        print(group_b[i], end="")
    print()

    def calculate_group(group, group_name):
        # Initialize points and goals
        points = {}
        goals_scored = {}
        for team in group:
            points[team] = 0
            goals_scored[team] = 0
        
        # Play matches
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                winner = play_match(group[i], group[j], f"Group Stage - {group_name}")
                points[winner] = points[winner] + 3
                goals_scored[group[i]] = goals_scored[group[i]] + match_results[-1]["Score 1"]
                goals_scored[group[j]] = goals_scored[group[j]] + match_results[-1]["Score 2"]
        
        # Create ranking list
        rankings = []
        for team in group:
            rankings.append([team, points[team], goals_scored[team]])
        
        # Simple sort by points
        for i in range(len(rankings)):
            for j in range(i + 1, len(rankings)):
                if rankings[i][1] < rankings[j][1]:
                    rankings[i], rankings[j] = rankings[j], rankings[i]
                elif rankings[i][1] == rankings[j][1] and rankings[i][2] < rankings[j][2]:
                    rankings[i], rankings[j] = rankings[j], rankings[i]
        
        # Print formatted table
        print(f"\n{group_name} Rankings:")
        print("-" * 40)
        print("Team            Points    Goals Scored")
        print("-" * 40)
        for team, pts, goals in rankings:
            print(f"{team:<15} {pts:<10} {goals:<12}")
        print("-" * 40)
        
        return [rankings[0][0], rankings[1][0]]  # Return top 2 teams

    top_a = calculate_group(group_a, "Group A")
    top_b = calculate_group(group_b, "Group B")
    print("\nTop 2 teams from Group A: ", end="")
    for i in range(len(top_a)):
        if i > 0:
            print(", ", end="")
        print(top_a[i], end="")
    print("\nTop 2 teams from Group B: ", end="")
    for i in range(len(top_b)):
        if i > 0:
            print(", ", end="")
        print(top_b[i], end="")
    print()
    
    return top_a + top_b

# Function to simulate knockout stage
def simulate_knockout(teams, round_name):
    winners = []
    random.shuffle(teams)
    print(f"\n=== {round_name} ===")
    for i in range(0, len(teams), 2):
        winner = play_match(teams[i], teams[i + 1], round_name)
        winners.append(winner)
        print(f"Winning team: {winner}")
    return winners

# Main program
if __name__ == "__main__":
    # Select favorite team
    favorite_team = input("Enter your favorite team: ")
    if favorite_team not in teams:
        print("Your chosen team is not in the list, proceeding anyway!")
    else:
        print(f"You selected: {favorite_team}")

    # Start the tournament
    print("\nStarting the tournament...")
    remaining_teams = play_group_stage(teams)

    # Semi-finals
    remaining_teams = simulate_knockout(remaining_teams, "Semi-finals")

    # Final
    print("\n=== Final ===")
    winner = play_match(remaining_teams[0], remaining_teams[1], "Final")
    print(f"\nChampion: {winner}!")
    if winner == favorite_team:
        print("Congratulations! Your favorite team won!")

    # Save results to Excel
    save_to_excel()
