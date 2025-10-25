# ⚽ Offside Mind

**Offside Mind** is a simple machine learning project that predicts the outcome of football matches using team and league information.  
It combines a trained `GradientBoostingClassifier` model with a lightweight Python script that makes match predictions based on team IDs and league data.

---

## 🚀 Features

- Predicts match outcomes using pre-trained machine learning model (`offside_mind_model.pkl`)
- Uses team and league mappings for easy input
- Prints prediction results in a clean, formatted output
- Simple and dependency-light setup — only `scikit-learn` and `pandas` are required

---

## 🧠 Model Overview

The model is trained using a **Gradient Boosting Classifier** from `scikit-learn`.  
It uses the following input features:

- `league_id` – numerical ID of the league  
- `match_week` – week number of the match  
- `home_id` – unique ID for the home team  
- `away_id` – unique ID for the away team  

The target variable represents the match result (e.g. win/loss/draw depending on training data).

The model and mappings are stored as:

- `model/offside_mind_model.pkl`
- `model/team_to_id.pkl`
- `model/id_to_team.pkl`

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/KayaxcOff/Offside-Mind.git
   cd offside-mind

2. Install dependencies:
  ```pip install pandas scikit-learn joblib```

Ensure the `model` files are located in the model/ directory:
```
    model/
    ├── offside_mind_model.pkl
    ├── team_to_id.pkl
    └── id_to_team.pkl
