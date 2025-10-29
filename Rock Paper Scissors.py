def player(prev_play, opponent_history=[], opponent_patterns={}):
    """
    An adaptive Rock Paper Scissors AI that uses sequence prediction to counter 
    the opponent.

    Args:
        prev_play (str): The opponent's last move ('R', 'P', or 'S').
        opponent_history (list): A list used to track all previous moves by the opponent.
        opponent_patterns (dict): A dictionary used to store sequence counts for prediction.
    
    Returns:
        str: The AI's next move ('R', 'P', or 'S').
    """

    if not prev_play:
        opponent_history.clear()
        opponent_patterns.clear()
        opponent_patterns['5'] = {}
        return 'R'
    
    opponent_history.append(prev_play)

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    sequence_len = 5
    
    if len(opponent_history) > sequence_len:
        recent_sequence = "".join(opponent_history[-sequence_len - 1:-1])
        following_move = opponent_history[-1]

        if recent_sequence not in opponent_patterns['5']:
            opponent_patterns['5'][recent_sequence] = {'R': 0, 'P': 0, 'S': 0}
        
        opponent_patterns['5'][recent_sequence][following_move] += 1
    
    prediction = prev_play 
    
    if len(opponent_history) >= sequence_len:
        current_sequence = "".join(opponent_history[-sequence_len:])
        
        if current_sequence in opponent_patterns['5']:
            counts = opponent_patterns['5'][current_sequence]
            
            prediction = max(counts, key=counts.get)
            
    return ideal_response[prediction]
