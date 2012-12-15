class Button:
    def __init__(self, color, position):
        self.color = color
        self.position = position

class Robot:
	def __init__(self, color, position):
		self.color = color
		self.position = position
		
def BuildStack(ip):
    # ip is a string with position and color in pairs.  no seperators.
    # Example ip: B4O1B5B6B2O2
    
    x = []                                        # x is the list to be returned.  Initialise
    
    # Output is a list of buttons,in same order as they appear in the list.
    for i in range(0, len(ip) / 2):
        x.append(Button(ip[0], int(ip[1])))            # create a new button and append to list.
        ip = ip[2:]                                    # trim the ip to remove the last two bits
    
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
			targetPosition = int(element.position)
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

def PressButton(robots, stack):
	# Receives an array of robots, and a stack.
	# Analysed the position of the robots against the next button to be pressed (top of the stack).
	# If robot of correct color is @ the same position as the top of the stack, press that button i.e - pop top of the stack.
	tick = 0								# Tells if a button was pressed, if yes tick is set to 1.  Caller learns that button was pressed.
	
	for robot in robots:
		if ( robot.color == stack[0].color and robot.position == stack[0].position ):
			print "Robot @ " + str(robot.position) + " press button in " + stack[0].color + " position."
			stack.pop(0)
			tick = 1
			
	return tick
	
# Main programm to run the simulation
tick = 0				# Simulates clock ticks.
ip = 'O2B1B2O4'			# Simulated input, in the real problem, this will come from file.
stk = BuildStack(ip)	# build stack from parsed input.

O = Robot('O', 1)
B = Robot('B', 1)		# Build the robots

while (len(stk) > 0 ):
	MoveRobot(B,stk)
	MoveRobot(O, stk)
	tick = tick + 1 + PressButton([B,O], stk)
	print "Tick"