import pyautogui as pg
import time
import numpy as np


def escape():
    pg.keyDown('esc')
    time.sleep(np.random.uniform(0.1, 0.3))
    pg.keyUp('esc')


def press_button(button_name):
    pg.keyDown(button_name)
    time.sleep(np.random.uniform(0.05, 0.1))
    pg.keyUp(button_name)
    input_random_sleep()


def random_sleep():
    time.sleep(np.random.uniform(2.6, 3.9))


def input_random_sleep():
    time.sleep(np.random.uniform(0.6, 0.9))


def long_random_sleep():
    time.sleep(np.random.uniform(10.6, 12.9))
