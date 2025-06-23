# ⚽ World Cup Tournament Simulator – Python Project

## 🎯 Project Overview

This Python project simulates a mini football (soccer) tournament inspired by World Cup structures. It includes **group stage, knockout rounds, penalty shootouts**, and outputs a detailed match result table to Excel.

The user can **interact by entering scores**, and the simulation handles draws, calculates rankings, and determines the champion through semi-finals and a final match.

This project was created as part of an Introduction to Programming course and demonstrates skills in **control flow, data structures, input validation, and file export**.

---

## 🛠️ Features

- Group stage with automatic group division and match simulation
- Knockout stages (semi-finals and final)
- User score input with validation
- Penalty shootout and random resolution for tied shootouts
- Ranking tables based on **points and goals scored**
- Export match results to Excel (`tournament_results.xlsx`)
- Built using **Python standard libraries + pandas**

---

## 🧩 How It Works

1. The user selects their **favorite team** (optional).
2. The teams are shuffled and divided into **Group A and B**.
3. All teams play round-robin within each group. Top 2 teams from each group proceed.
4. Semi-finals and Final are played, including **penalty shootouts** for draws.
5. Results are saved to an Excel file at the end.
