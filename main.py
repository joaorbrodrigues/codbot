import utils as utl
import commons as com

while True:
    utl.long_random_sleep()
    com.set_initial_position()
    com.do_help()
    com.collect_resources()
    com.check_training_camps()
    com.open_alliance()
    com.gather()
    com.check_game_crashed()
