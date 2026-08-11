# Project Purpose

   This project builds a Transformer-based D&D encounter difficulty advisor that takes a natural-language encounter description as input and predicts whether the encounter is likely Easy, Medium, Hard, or Deadly. The system is designed to help dungeon masters evaluate encounter balance and eventually provide adjustment recommendations.

## Primary Prediction Labels

    The initial Transformer model will perform binary classification using the following labels:

    - Possible
    - Not Possible

    The purpose of the initial model is to determine whether a combat encounter is likely survivable under standard Dungeons & Dragons 5th Edition core rules assumptions.

    The binary classifier is intended to establish whether the model can successfully learn encounter feasibility relationships from structured encounter data before expanding into more advanced categorical encounter difficulty prediction.

    The purpose of the model is to learn relationships between:
    - enemy composition
    - enemy count
    - encounter descriptions
    - environmental context
    - player party information

    and predict the likely encounter difficulty classification. 

    If the model successfully demonstrates feasibility prediction through binary classification, the prediction system will expand into multi-class encounter difficulty classification categories such as:

    - Easy
    - Medium
    - Hard
    - Deadly

    This phased approach is intended to validate core learning behavior before introducing more complex categorical difficulty prediction.

    Future versions of the project may expand into:
    - encounter recommendations
    - balancing suggestions
    - terrain analysis
    - loot suggestions
    - adaptive DM assistance

## Scope Boundaries

 ### Project Scope
   
    This project is limited to the core Dungeons & Dragons 5th Edition ruleset.

    The initial project scope will use the three primary 5th Edition core rulebooks as the conceptual rules foundation:

    - Player's Handbook
    - Dungeon Master's Guide
    - Monster Manual

    The project will not initially include expanded sourcebooks, optional subclasses, multiclassing complexity, homebrew content, prestige-style systems, or campaign-specific modifications.

    The purpose of this scope boundary is to reduce rule complexity and keep the model focused on a consistent rules foundation.

## Architecture Diagram

    
    Encounter Data
        ↓
    Dataset Builder / CSV Generator
        ↓
    Text Preprocessing
        ↓
    Tokenizer
        ↓
    Transformer Model
        ↓
    Binary Classification Output
        ↓
    Prediction:
    Possible / Not Possible
    

## Technical Stack

    - Language: Python
    - IDE: VS Code
    - Data Handling: pandas
    - Machine Learning / Deep Learning: PyTorch or TensorFlow
    - Documentation: Markdown
    - Version Control: Git / GitHub

## Environment and Dependency Management

    The project will use a dedicated Python virtual environment to isolate project dependencies and maintain reproducible development behavior.

    Project dependencies will be tracked using a frozen `requirements.txt` file generated from the active virtual environment.

    This approach is intended to:
    - improve reproducibility
    - simplify project setup
    - reduce dependency conflicts
    - support consistent execution across environments

## Dataset Structure

    The initial dataset will be a labeled synthetic encounter dataset designed for binary classification.

    Each dataset row will represent one combat encounter scenario. The dataset will include structured party information, enemy information, encounter context, and a target label indicating whether the encounter is considered possible or not possible under core Dungeons & Dragons 5th Edition assumptions.

 ### Initial Columns

      - encounter_id
      - party_size
      - party_level
      - enemy_count
      - enemy_name
      - enemy_challenge_rating
      - encounter_description
      - feasibility_label

 ### Target Label

      The target label for the initial model will be:

      - Possible
      - Not Possible

 ### Example Row

     encounter_id: 001
     party_size: 4
     party_level: 5
     enemy_count: 1
     enemy_name: Ancient Red Dragon
     enemy_challenge_rating: 24
     encounter_description: Four level 5 adventurers face one ancient red dragon in open terrain.
     feasibility_label: Not Possible

## Folder Structure
  ```
  course-end-project/
│
├── docs/
│   ├── project_proposal.md
│   ├── transformer_project_development_roadmap.md
│   └── architecture_notes.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│
├── notebooks/
│   └── dataset_exploration.ipynb
│
├── src/
│   ├── config.py
│   ├── pipeline.py
│   ├── dataset_generator.py
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── tokenizer.py
│   ├── model.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── predictor.py
│
├── outputs/
│   ├── models/
│   ├── metrics/
│   └── charts/
│
├── tests/
│
├── README.md
└── requirements.txt
```