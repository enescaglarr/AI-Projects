# SemEval-2026 Task 13: Detecting Machine-Generated Code

This repository contains the project implementation for **SemEval-2026 Task 13 (Subtask A)**, developed by Group 18 for the CS 445 course. [cite_start]The project focuses on binary classification to distinguish between human-written and machine-generated source code across multiple programming languages and generation scenarios[cite: 1, 2].

## Authors (Group 18)
* [cite_start]**Barbaros Yahya** (31143) 
* [cite_start]**Enes Çağlar** (31109) 
* [cite_start]**Filiz Ilgaz Sönmez** (32073) 
* [cite_start]**İsa Utku Dursunoğlu** (30881) 
* [cite_start]**Mehmet Barış Baştuğ** (30617) 

---

## Project Overview
[cite_start]With the rise of Large Language Models (LLMs), identifying AI-generated code has become crucial for software security and academic integrity[cite: 204]. [cite_start]This project implements a variety of detection strategies, ranging from traditional machine learning with handcrafted features to state-of-the-art transformer-based models[cite: 206].

### Methodology
[cite_start]Our pipeline involves sophisticated preprocessing and modeling techniques designed to capture semantic and structural patterns rather than surface-level stylistic cues[cite: 207].


#### 1. Preprocessing & Feature Engineering
* [cite_start]**GPTSniffer-inspired Preprocessing:** Masking comments, imports, and whitespace to reduce model bias towards specific generators[cite: 212, 224].
* [cite_start]**Variable Masking:** A custom strategy that masks variable names, string literals, and numeric literals while preserving language-specific keywords to force the model to learn underlying structural patterns[cite: 296, 297].
* [cite_start]**Handcrafted Features:** Extraction of 13 statistical and structural metrics (e.g., AST depth, cyclomatic complexity, maintainability index) using the **Tree-sitter** parsing framework[cite: 232, 234].

#### 2. Models Evaluated
* [cite_start]**Transformer Models:** Fine-tuned encoder-only architectures including **ModernBERT**, **CodeBERT**, **UniXcoder**, and **GraphCodeBERT**[cite: 206, 223].
* [cite_start]**Traditional ML:** **CatBoost** and **XGBoost** classifiers utilizing handcrafted structural and stylistic features[cite: 228, 300].
* [cite_start]**Lexical Baselines:** TF-IDF representations combined with **Multinomial Naive Bayes** and **Linear SVM**[cite: 271, 274, 275].

---

## Performance Results
[cite_start]The models were evaluated using the **Macro F1 score** to ensure a fair comparison across classes and programming languages[cite: 208].

| Model | Validation Macro F1 | Hidden Test Macro F1 |
| :--- | :--- | :--- |
| **ModernBERT** | 0.9970 | 0.28 - 0.35 |
| **GraphCodeBERT** | 0.9950 | 0.2505 |
| **UniXcoder** | 0.9940 | 0.2884 |
| **CatBoost** | 0.9700 | 0.3800 |
| **XGBoost** | 0.9831 | 0.2700 |
| **TF-IDF + SVM** | 0.8500 | **0.4589** |

[cite_start]**Key Finding:** While neural models achieved near-ceiling performance on validation data, simpler lexical models (TF-IDF + SVM) demonstrated significantly better generalization on the unseen hidden test set, highlighting the severity of distribution shift in AI-generated code detection[cite: 339, 341].

