def wombat(state, time_left):
    import random
    
    command = random.choice(['turn', 'move', 'shoot'])
    
    if command == 'turn':
        metadata = {
            'direction': random.choice(['right', 'left', 'about-face'])
            }
    else:
        metadata = {}
                
    # Note that the function name MUST be wombat
    return {
        'command': {
            'action': command,
            'metadata': metadata,
        },
        'state': {
            'hello': 'world'
        }
    }
