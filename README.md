# Rock-Paper-Scissors
---

Introduction

This project features an intelligent Rock Paper Scissors AI designed to defeat opponents by learning and predicting their repeating patterns and sequences of moves. The AI uses a dictionary-based memory to track move frequencies, turning a game of chance into a game of data analysis.

---

The Core Strategy: Sequence Prediction

Instead of choosing a move randomly, this AI operates on the assumption that most human players fall into predictable habits.

- Pattern Recognition: The AI constantly tracks the opponent's last 5 moves (the sequence).
- Prediction: It looks up this 5-move sequence in its memory to determine which move (R, P, or S) the opponent is most likely to play next.
- Counter Play: Once the next move is predicted, the AI plays the move that beats that prediction (e.g., if it predicts 'P', it plays 'S').

This creates a self-improving opponent that gets smarter the longer you play against it.

---
How the AI Thinks

The main logic resides in the player function, which is stateful (it remembers history across turns).


Learning Phase (First few turns)
- Initialization: On the very first turn, the AI plays 'R' and clears its memory to start fresh.
- Building Memory: The AI spends the first few turns simply recording the opponent's moves until it has a sequence long enough to start recognizing patterns (a minimum of 6 moves are required to record the first 5-move sequence and the move that followed it).



Prediction Phase (Ongoing)
1. Track the New Data: After every opponent move, the AI updates its memory, incrementing the count for the move that followed the last recorded 5-move sequence.
2. Identify Current Sequence: The AI looks at the opponent's most recent 5 moves.
3. Lookup and Predict: It searches its memory for this current 5-move sequence:
   - If the sequence is found, it looks at the recorded history to see which move ('R', 'P', or 'S') came next most frequently. This is the prediction.
   - If the sequence is new, it falls back to the opponent's last move as a simple, short-term prediction.

4. Execute Counter: It selects the mathematically perfect counter to the predicted move and plays it.

---

The Key Function

The entire logic is contained within the single, recursive player function

<img width="593" height="257" alt="image" src="https://github.com/user-attachments/assets/498d3967-3390-4ba8-831e-c8ee20e65a80" />

---

