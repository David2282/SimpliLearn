import pandas as pd
import numpy as np
from src.config import SYNTHETIC_DATA_PATH
from src.config import MONSTER_POOL

COLUMNS = [
    "encounter_id",
    "party_size",
    "party_level",
    "monster_count",
    "monster_name",
    "monster_challenge_rating",
    "encounter_description",
    "feasibility_label",
]

def generate_synthetic_data(num_samples=5000):
    data = []
    for i in range(num_samples):
        encounter_id = f"encounter_{i+1}"
        party_size = np.random.randint(1, 6)
        party_level = np.random.randint(1, 20)
        monster_count = np.random.randint(1, 10)
        monster_pool = np.random.choice(MONSTER_POOL)
        monster_name = monster_pool["name"]
        monster_challenge_rating = monster_pool["challenge_rating"]
        encounter_description = f"A group of {monster_count} {monster_name}(s) confronts a party of {party_size} adventurers at level {party_level}."
        feasibility_label = "Possible" if (party_level * party_size) >= (monster_challenge_rating * monster_count) else "Not Possible"
        
        data.append([
            encounter_id,
            party_size,
            party_level,
            monster_count,
            monster_name,
            monster_challenge_rating,
            encounter_description,
            feasibility_label
        ])
    
    df = pd.DataFrame(data, columns=COLUMNS)
    df.to_csv(SYNTHETIC_DATA_PATH, index=False)
    print(f"Synthetic data generated and saved to {SYNTHETIC_DATA_PATH}")
    return df