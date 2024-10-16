
#move() and turn_left().
#Either the test front_is_clear() 
#or wall_in_front(), right_is_clear() 
#or wall_on_right(), and at_goal().
#How to use a while loop and if/elif/else statements.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()            
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear():
        move()
