import os
import sys

script_dir = sys.path[0]

# -------------------------------------------------

# Screen Size
height = 1440
width = 2560

# -------------------------------------------------

# Targets
# Inside Castle Resources, Help and Alliance
help_icon = os.path.join(script_dir, '.\\images\\help.png')
gold_icon = os.path.join(script_dir, '.\\images\\gold.png')
mana_icon = os.path.join(script_dir, '.\\images\\mana.png')
wood_icon = os.path.join(script_dir, '.\\images\\wood.png')
ore_icon = os.path.join(script_dir, '.\\images\\ore.png')
alliance_icon = os.path.join(script_dir, '.\\images\\alliance_icon.png')

# Training camps
celestial_temple = os.path.join(script_dir, '.\\images\\celestial_temple.png')
celestial_train = os.path.join(script_dir, '.\\images\\celestial_train.png')
abbey = os.path.join(script_dir, '.\\images\\abbey.png')
abbey_train = os.path.join(script_dir, '.\\images\\abbey_train.png')
ballista_factory = os.path.join(script_dir, '.\\images\\ballista_factory.png')
ballista_train = os.path.join(script_dir, '.\\images\\ballista_train.png')
knight_camp = os.path.join(script_dir, '.\\images\\knight_camp.png')
knight_train = os.path.join(script_dir, '.\\images\\knight_train.png')
swordsmen_camp = os.path.join(script_dir, '.\\images\\swordsmen_camp.png')
swordsmen_train = os.path.join(script_dir, '.\\images\\swordsmen_train.png')

# Alliance Menu
donate_button = os.path.join(script_dir, '.\\images\\donate.png')
common_gifts_selected = os.path.join(script_dir, '.\\images\\common_gifts_selected.png')
common_gifts_unselected = os.path.join(script_dir, '.\\images\\common_gifts_unselected.png')
rare_gifts_selected = os.path.join(script_dir, '.\\images\\rare_gifts_selected.png')
claim_all_icon = os.path.join(script_dir, '.\\images\\claim_all.png')
claim_one_button = os.path.join(script_dir, '.\\images\\claim_one.png')
gifts_notification = os.path.join(script_dir, '.\\images\\gifts_notification.png')
technology_notification = os.path.join(script_dir, '.\\images\\technology_notification.png')


# Outside Castle/Gathering
wood_unselected = os.path.join(script_dir, '.\\images\\loggin_camp_unselected.png')
wood_selected = os.path.join(script_dir, '.\\images\\loggin_camp_selected.png')
mana_unselected = os.path.join(script_dir, '.\\images\\mana_pool_unselected.png')
mana_selected = os.path.join(script_dir, '.\\images\\mana_pool_selected.png')
ore_unselected = os.path.join(script_dir, '.\\images\\ore_mine_unselected.png')
ore_selected = os.path.join(script_dir, '.\\images\\ore_mine_selected.png')
gold_unselected = os.path.join(script_dir, '.\\images\\gold_mine_unselected.png')
gold_selected = os.path.join(script_dir, '.\\images\\gold_mine_selected.png')
march = os.path.join(script_dir, '.\\images\\march.png')
legion_overview = os.path.join(script_dir, '.\\images\\legion_overview.png')
remove_deputy = os.path.join(script_dir, '.\\images\\remove_deputy.png')
create_legions = os.path.join(script_dir, '.\\images\\create_legions.png')
gather_button = os.path.join(script_dir, '.\\images\\gather.png')
search_button = os.path.join(script_dir, '.\\images\\search.png')
legion_5_out_of_5 = os.path.join(script_dir, '.\\images\\5_marches.png')
returning_march = os.path.join(script_dir, '.\\images\\returning_march.png')
marching_to_gather = os.path.join(script_dir, '.\\images\\marching_to_gather.png')

# General
confirm_button = os.path.join(script_dir, '.\\images\\confirm.png')
start_cod_icon = os.path.join(script_dir, '.\\images\\start_cod.png')
map_icon = os.path.join(script_dir, '.\\images\\map_icon.png')
profile = os.path.join(script_dir, '.\\images\\profile.png')

# -------------------------------------------------

# Region
full_screen = (0, 0, width, height)

# -------------------------------------------------

# Confidence
general_confidence = 0.8
more_confidence = 0.9
most_confidence = 0.99

# -------------------------------------------------

# Gathering
gathering_target = "ore"
allow_deputy = False
