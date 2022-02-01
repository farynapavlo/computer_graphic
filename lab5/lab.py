def setupForDragonCurve():
       turtle.hideturtle()
       turtle.tracer(1e3, 0)
       turtle.penup()
       turtle.goto(0, -turtle.window_height()/5)
       turtle.pendown()

def generateDragonCurve(n, result='[FX]'):
       for _ in range(n):
           result = result.replace('Y', 'FX-Y')
           result = result.replace('X', 'X+YF')
       return result

def drawDragonCurve(cmds, size):
       stack = []
       for cmd in cmds:
           if cmd=='F':
               turtle.forward(size)
           elif cmd=='-':
               turtle.left(90)
           elif cmd=='+':
               turtle.right(90)
           elif cmd=='X':
               pass
           elif cmd=='Y':
               pass
           elif cmd=='[':
               stack.append((turtle.position(), turtle.heading()))
           elif cmd==']':
               position, heading = stack.pop()
               turtle.penup()
               turtle.setposition(position)
               turtle.setheading(heading)
               turtle.pendown()
           else:
               raise ValueError('Unknown Cmd: {}'.format(ord(cmd)))
       turtle.update()