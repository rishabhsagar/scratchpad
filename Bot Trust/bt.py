class Button:
    def __init__(self, color, position):
        self.color = color
        self.position = position

class Robot:
  def __init__(self, color, position):
    self.color = color
    self.position = position
    
def BuildStack(ip):
    # ip is a string with position and color in pairs.
    # Example ip: B 4 O 1 B 5 B 6 B 2 O 2
    
    x = []                                # x is the list to be returned.
    
    ip = ip.split(' ')

    # Output is a list of buttons,in same order as they appear in the list.
    for i in range(0, len(ip), 2):
        x.append(Button(ip[i], int(ip[i+1])))          # create a new button and append to list.
    
    # Return x
    return x


def PrintStack(stk):
    for elem in stk:
        print elem.color + str(elem.position) ,
    print ""
  
def MoveRobot(robots, stack):
  # Parsed the global move stack and move the robot one step closer to the next (update object)
  # target position.  If there are no more buttons to visit, or if the robot is
  # already at the next target position, then do nothing.
  # Return : updated robot object.

    for robot in robots:
        if ( len(stack) > 0 ):
          if ( robot.color == stack[0].color and robot.position == stack[0].position ):
            print "Robot " + robot.color + " pressed button " + str(stack[0].position)
            stack.pop(0)
            if ( len(stack) > 0 ):
                 PrintStack(stack)
            else:
                 print "Stack empty"
            break                    # Only one operation per step

        targetPosition = 0            # initiliase the target position of the robot to move.

        if ( len(stack) > 0):
          for element in stack:
            if ( robot.color == element.color ):
              targetPosition = int(element.position)
              #print "Robot " + robot.color + " has target position set to " + str(targetPosition)
              break
                
          if ( targetPosition == 0 or targetPosition == robot.position):
            # robot has no buttons to visit or is already @ correct position
            print "Robot " + robot.color + " does not move in this tick"
            pass
          else:
            if ( targetPosition < robot.position ):
              robot.position = robot.position - 1
              print "Robot " + robot.color + " moves to " + str(robot.position)
                  
            if (targetPosition > robot.position):
              robot.position = robot.position + 1
              print "Robot " + robot.color + " moves to " + str(robot.position)

def PressButton(robots, stack):
  # Receives an array of robots, and a stack.
  # Analysed the position of the robots against the next button to be pressed (top of the stack).
  # If robot of correct color is @ the same position as the top of the stack, press that button i.e - pop top of the stack.
  tick = 0                   # Tells if a button was pressed, if yes tick is set to 1.  Caller learns that button was pressed.
  
  for robot in robots:
    if ( len(stack) > 0 ):
      if ( robot.color == stack[0].color and robot.position == stack[0].position ):
        stack.pop(0)
        tick = 1
      
  return tick

def RunTest():
  # Main programm to run the simulation
  tick = 0                    # Simulates clock ticks.
  ip = 'O 5 O 8 B 10'      # Simulated input, in the real problem, this will come from file.
  stk = BuildStack(ip)        # build stack from parsed input.
  
  O = Robot('O', 1)
  B = Robot('B', 1)           # Build the robots
  
  while (len(stk) > 0 ):
    MoveRobot([O, B], stk)
    tick = tick + 1
    print "Current tick : " + str(tick) + "\n"

  print "Total time (in ticks) : " + str(tick)

def RunCase(line):
  tick = 0
  
  #Build stack from inputline.
  stk = BuildStack(line)

  # Build and initialise robots.
  O = Robot('O', 1)
  B = Robot('B', 1)

  while (len(stk) > 0):
    MoveRobot(O, stk)
    MoveRobot(B, stk)
    tick = tick + 1
    print "Current tick : " + str(tick) + "\n"
  
  return tick


def RunSimulation(inputFile, outputFile):
  f = open(inputFile, "r")
  o = open(outputFile, "w")

  testcases = f.readline()
  print "Total number of test cases : " + testcases

  for lines in range(0, int(testcases)):
    inputLine = f.readline()[2:]
    timeTaken = RunCase(inputLine)
    print "Case #" + str((lines + 1)) + ": " + str(timeTaken)
    o.writelines("Case #" + str((lines + 1)) + ": " + str(timeTaken) + "\n")

  f.close()
  o.close()

#RunSimulation("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\Bot Trust\\t1.in", "C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\Bot Trust\\t1.out")
RunTest()
