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

	
def MoveRobot(robot, stack):
	# Parsed the global move stack and move the robot one step closer to the next (update object)
	# target position.  If there are no more buttons to visit, or if the robot is
	# already at the next target position, then do nothing.
	# Return : updated robot object.
	
	targetPosition = 0						# initiliase the target position of the robot to move.
	
	for element in stack:
		if ( robot.color == element.color ):
			targetPosition = element.position
			break
	
	if ( targetPosition == 0 ):
		# robot has no buttons to visit
		pass
	else:
		if ( targetPosition < robot.position ):
			robot.position = robot.position - 1
		
		if (targetPosition > robot.position):
				robot.position = robot.position + 1
			
		if (targetPosition == robot.position):
			# robot already @ target position, pass.
			pass