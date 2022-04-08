import curses
from curses import textpad
from random import randint


def main(stdscrn):
    curses.curs_set(0)
    stdscrn.nodelay(1)
    stdscrn.timeout(250)

    sh, sw = stdscrn.getmaxyx()
    box = [[3,3], [sh-3, sh+sh]]
    textpad.rectangle(stdscrn, box[0][0], box[0][1], box[1][0], box[1][1])

    # Snake Initialize State
    snake = [[sh//2, sh+1], [sh//2, sh], [sh//2, sh-1]] # Head @ snake[0]
    direction = curses.KEY_RIGHT # Starts facing / moving right
    
    for y,x in snake:
        stdscrn.addstr(y, x, '#')

    held = [0, 0]
    food = [0, 0]
    score = 0
    alive = True

    while alive:

        # Food generation
        if (food == [0, 0]) or (food in snake):
            while (held == food) or (held in snake):
                food_y = randint(4, sh-4)
                food_x = randint(4, (2*sh)-1)
                held = [food_y, food_x]
            food = held
            stdscrn.addstr(food[0], food[1], 'o')
        stdscrn.addstr(0, 3, "Score: " + str(score))

        # Snake movement
        key = stdscrn.getch()

        if key == curses.KEY_UP and direction != curses.KEY_DOWN:
            direction = key
        elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
            direction = key
        elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
            direction = key
        elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
            direction = key

        head = snake[0]

        if direction == curses.KEY_RIGHT: # Right
            new_head = [head[0], head[1]+1]
        elif direction == curses.KEY_LEFT: # Left
            new_head = [head[0], head[1]-1]
        elif direction == curses.KEY_UP: # Up
            new_head = [head[0]-1, head[1]]
        elif direction == curses.KEY_DOWN: # Down
            new_head = [head[0]+1, head[1]]

        # Checks if snake hits border
        if (new_head[0] in [3, sh-3]) or (new_head[1] in [3, (2*sh)]) or (new_head in snake):
            alive = False
        
        snake.insert(0, new_head)
        stdscrn.addstr(new_head[0], new_head[1], '#')
        
        # Check if snake eats food
        if new_head != food:
            stdscrn.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()
        else:
            score += 1

        stdscrn.refresh()

curses.wrapper(main)
