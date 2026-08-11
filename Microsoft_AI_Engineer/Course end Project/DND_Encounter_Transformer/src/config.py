SYNTHETIC_DATA_PATH = "data/synthetic/encounters.csv"
TRAIN_DATA_PATH = "data/processed/train.csv"
TEST_DATA_PATH = "data/processed/test.csv"

# For Data Exploration
# SYNTHETIC_DATA_PATH = "../data/synthetic/encounters.csv"
# TRAIN_DATA_PATH = "../data/processed/train.csv"
# TEST_DATA_PATH = "../data/processed/test.csv"


TEST_SIZE = 0.2
RANDOM_STATE = 42

VALID_CHALLENGE_RATINGS = [0.25, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MONSTER_NAMES = [
    "Goblin",
    "Orc",
    "Bugbear",
    "Bandit",
    "Dragon"
]

MONSTER_POOL = [
    {"name": "Goblin", "challenge_rating": 0.25},
    {"name": "Orc", "challenge_rating": 0.5},
    {"name": "Bugbear", "challenge_rating": 1},
    {"name": "Ogre", "challenge_rating": 2},
    {"name": "Troll", "challenge_rating": 5},
    {"name": "Young Red Dragon", "challenge_rating": 10}
]