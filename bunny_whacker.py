# pgzero
import time
import random

WIDTH = 800
HEIGHT = 700


mode = "menu"
timer = 120
level = 0
total_points = 0
ybunny_state = "none"
ybunnys = []
hole1 = "empty"
hole2 = "empty"
hole3 = "empty"
hole4 = "empty"
hole5 = "empty"
locations = [(655, 490), (535, 515), (400, 500), (275, 515), (170, 490)]
bunnys_hit = 0
level_goal = 10
menu = Actor("bunny_whacker_title")
background = Actor("bunny_game_bg")

game_over = Actor("game_over_screen")


def start_game():
    global mode, timer, level, level_goal, ybunnys
    mode = "game"
    level = 0
    timer = 120
    ybunnys.clear()
    clock.unschedule(ybunny_peek)
    clock.unschedule(tick_timer)
    clock.schedule_interval(ybunny_peek, 1.2)
    clock.schedule_interval(tick_timer, 1.0)


def ybunny_peek():
    global ybunny_state, ybunny_visible, ybunnys
    ybunny_state = "peeking"
    pos = random.choice(locations)

    ybunny = Actor("ybunny_exiting")

    clock.schedule_interval(show_or_not, 1)
    ybunny.pos = pos
    ybunnys.append(ybunny)

    clock.schedule_unique(ygone, 2)



def show_or_not():
    global ybunny_state, ybunnys
    for ybunny in ybunnys:
        ybunny.image = "ybunny_showing"
        ybunny_state = "full"


def ygone():
    if ybunnys:
        ybunnys.pop(0)


def ycaught():
    global bunnys_hit
    bunnys_hit += 1
    level_up()

def tick_timer():
    global timer, mode
    if mode != "game":
        return
    timer -= 1

    if timer <= 0:
        mode = "game over"
        clock.unschedule(tick_timer)


def level_up():
    global level, timer, bunnys_hit, level_goal
    if bunnys_hit >= level_goal:
        level += 1
        bunnys_hit = 0
        level_goal += 10
        timer = 120


def draw():
    if mode == "menu":
        menu.draw()
    elif mode == "game":
        background.draw()
        screen.draw.text(str(timer), center=(183, 450), color="yellow", fontsize=30)
        screen.draw.text(
            "Level: " + str(level), center=(645, 450), color="yellow", fontsize=20
        )
        screen.draw.text(
            str(bunnys_hit) + " / " + str(level_goal),
            center=(400, 425),
            color="yellow",
            fontsize=35,
        )
        screen.draw.text(
            "Points: " + str(total_points),
            center=(700, 100),
            color="black",
            fontsize=40,
        )
        for ybunny in ybunnys:
            ybunny.draw()
    elif mode == "game over":
        game_over.draw()
    # if ybunny_state == "peek":
    # ybunny.draw()


def on_key_down(key):
    global mode
    if key == keys.SPACE:
        if mode == "menu" or mode == "game over":
            start_game()
    if key == keys.R:
        if mode == "game over":
            mode = 'menu'

def on_mouse_down(pos, button):
    global mode, total_points, ybunnys
    for ybunny in ybunnys:
        if ybunny.collidepoint(pos):
            total_points += 1
            ycaught()
            ybunnys.remove(ybunny)
            break
