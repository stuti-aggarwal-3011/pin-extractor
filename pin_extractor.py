def pin_extractor(poems):
    secret_codes = []
    
    # Loop through each poem in the list
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        
        # Loop through each line with its index number
        for line_index, line in enumerate(lines):
            words = line.split()
            
            # If the word exists at the current index, add its length to the PIN
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            # If the line is too short, add a '0' as a placeholder
            else:
                secret_code += '0'
                
        secret_codes.append(secret_code)
        
    return secret_codes        

# --- Test Data ---
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Extract and print the secret PINs
print(pin_extractor([poem, poem2, poem3]))
