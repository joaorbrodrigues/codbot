import utils as utl
import commons as com

from pyclick import HumanClicker
hc = HumanClicker()

while True:
    utl.long_random_sleep()
    com.do_help()
    utl.random_sleep()
    com.collect_resources()
    utl.random_sleep()
    com.open_alliance()
    utl.random_sleep()
    com.gather()
    utl.random_sleep()
    com.check_game_crashed()
    utl.random_sleep()

    # hc.move((1280, 720), 2)
    # hc.click()

