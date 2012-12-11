class Button:
    def __init__(self, color, position):
        self.color = color
        self.position = position

def BuildStack(ip):
    # ip is a string with position and color in pairs.  no seperators.
    # Example ip: B4O1B5B6B2O2
    
	x = []                                        # x is the list to be returned.  Initialise
	
    # Output is a list of buttons,in same order as they appear in the list.
    for i in range(0, len(ip) / 2):
        x.append(Button(ip[0], ip[1]))            # create a new button and append to list.
        ip = ip[2:]                               # trim the ip to remove the last two bits
    
    # Return x
    return x
        