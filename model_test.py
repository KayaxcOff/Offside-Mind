import joblib
import pandas as pd

model = joblib.load('model/offside_mind_model.pkl')
team_to_id = joblib.load('model/team_to_id.pkl')
id_to_team = joblib.load('model/id_to_team.pkl')

def predict_match(league_id, match_week, home_team, away_team):
    if home_team not in team_to_id or away_team not in team_to_id:
        raise ValueError("One or both teams are not recognized.")

    home_team_id = team_to_id[home_team]
    away_team_id = team_to_id[away_team]

    input_data = pd.DataFrame([{
        'league_id': league_id,
        'match_week': match_week,
        'home_id': home_team_id,
        'away_id': away_team_id
    }])

    pred = model.predict(input_data)[0]

    print(f"+{'-' * 40}+")
    print(f"| {'League ID':<10}: {league_id:<25}  |")
    print(f"| {'Match Week':<10}: {match_week:<25}  |")
    print(f"| {'Home Team':<10}: {home_team:<25}  |")
    print(f"| {'Away Team':<10}: {away_team:<25}  |")
    print(f"| {'Prediction':<10}: {pred:<25}  |")
    print(f"+{'-' * 40}+")

predict_match(6, 14, "Fenerbahçe", "Galatasaray")