# Transformer Project Development Roadmap

# Project Title
Transformer-Based D&D Encounter Difficulty Advisor

---

# Purpose of This Document

This document outlines the major development phases for the Transformer project.

The purpose of this roadmap is to:

- Break the project into manageable engineering milestones
- Track progress throughout development
- Reduce project overwhelm
- Maintain architectural focus
- Provide structure during implementation
- Document development progression for future review

This roadmap is intended to evolve throughout the project lifecycle.

---

# PHASE 1 — PROJECT FOUNDATION

## Goal
Define the project scope, architecture, and technical objectives before implementation.

## Objectives

- Finalize project purpose
- Define primary prediction label
- Define scope boundaries
- Define architecture diagram
- Define dataset structure
- Define folder structure
- Create proposal document
- Establish project roadmap

## Completion Indicator

> "I know exactly what I am building."

## Status Notes

Date Started: 5/19/26

Date Completed: 5/19/26

Additional Notes:

    Added a Technical stack I can update as I go along with Libraries and other tools if needed
    Added Environment and Dependency section

---

# PHASE 2 — DATASET ENGINEERING

## Goal
Create a structured dataset suitable for Transformer training.

## Objectives

- Define encounter template structure
- Define classification labels
- Generate synthetic encounter examples
- Create CSV dataset
- Validate label balance
- Clean formatting inconsistencies
- Split train/test datasets
- Verify dataset quality

## Completion Indicator

> "My model has meaningful data to learn from."

## Status Notes

Date Started: 5/19/26

Date Completed: 5/19/26

Additional Notes:
 - created static CR values, and monster names including only monster names with clean conjugations from singular to plural (5/29/26) 
 - Refactor: MONSTER_POOL holds name, cr in a list of dictionaries (5/29/26)
 - Expanded dataset to 5,000 samples

---

# PHASE 3 — NLP PREPROCESSING

## Goal
Convert natural-language prompts into structured numerical representations.

## Objectives

- Build tokenizer
- Build vocabulary
- Handle unknown tokens
- Implement padding/truncation
- Convert prompts into token IDs
- Create dataset loader
- Create batching pipeline
- Validate preprocessing outputs

## Completion Indicator

> "I can successfully feed structured text into the model."

## Status Notes

Date Started: 5/22/26

Date Completed: 5/22/26

Additional Notes:

---

# PHASE 4 — TRANSFORMER ARCHITECTURE

## Goal
Build the core Transformer encoder architecture.

## Objectives

- Build embedding layer
- Implement positional encoding
- Implement self-attention layer
- Implement multi-head attention
- Build feed-forward block
- Implement residual connections
- Build encoder block
- Build classifier head
- Validate model forward pass

## Completion Indicator

> "I built a functional Transformer architecture."

## Status Notes
- need to wire to pipeline and validate forward pass

Date Started: 5/24/26

Date Completed: 6/4/26

Additional Notes:
- Using pytorch's encoding layer for first pass. Will build custom layer once full system is verified
- Resolved embedding index error by aligning vocabulary size with token ID range and reserved padding token (ID = 0). Updated model initialization to account for padding index when constructing embedding layer.

# PHASE 5 — TRAINING PIPELINE

## Goal
Train, validate, and evaluate the Transformer model.

## Objectives

- Define loss function
- Define optimizer
- Build training loop
- Build validation loop
- Track epoch performance
- Track accuracy metrics
- Detect overfitting
- Save/load trained models
- Evaluate prediction quality

## Completion Indicator

> "The model is successfully learning meaningful patterns."

## Status Notes

Date Started: 6/4/26

Date Completed:

Additional Notes:

---

# PHASE 6 — RECOMMENDATION ENGINE

## Goal
Add contextual D&D recommendation and advisory functionality.

## Objectives

- Generate difficulty explanations
- Create encounter adjustment suggestions
- Add terrain/environment recommendations
- Add loot balancing suggestions
- Add enemy composition guidance
- Add rule-based balancing feedback
- Validate recommendation consistency

## Completion Indicator

> "The system behaves like a contextual DM assistant."

## Status Notes

Date Started:

Date Completed:

Additional Notes:

---

# PHASE 7 — POLISH & PRESENTATION

## Goal
Prepare the project for presentation, submission, and portfolio use.

## Objectives

- Write README documentation
- Create architecture diagrams
- Generate training graphs/charts
- Clean/refactor codebase
- Improve modularity
- Add comments and docstrings
- Organize GitHub repository
- Prepare presentation/demo
- Finalize submission materials

## Completion Indicator

> "This is a professional and explainable engineering project."

## Status Notes

Date Started:

Date Completed:

Additional Notes:

---

# Overall Project Philosophy

This project is intended to be approached as a modular engineering effort rather than a single monolithic task.

Progress should be measured by:

- Completed subsystems
- Validated components
- Architectural clarity
- Incremental engineering milestones

The project incorporates AI-assisted development tools as collaborative engineering aids while maintaining human architectural oversight, validation, and decision-making throughout the development lifecycle.

---

# Final Reminder

Do not measure progress by whether the entire Transformer system is complete.

Measure progress by:

- What subsystem is complete
- What problem has been solved
- What component has been validated
- What engineering milestone has been achieved

Large engineering projects are built incrementally.

