def sample_response(input_text):
    user_message = str(input_text).lower()
    
    if(user_message is 'hello'):
        return 'hello!'
    
    return 'I do not understand'