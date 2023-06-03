import pyautogui as pg
import numpy as np
import setup as stp
import utils as utl


# Clicks a button based on an image received as parameter
def find_and_click(button_image, region, confidence):
    location = pg.locateOnScreen(button_image, region=region, confidence=confidence, grayscale=True)
    if location:
        x, y = pg.center(location)
        x = x * np.random.uniform(0.99, 1.01)
        y = y * np.random.uniform(0.99, 1.01)
        pg.click(x, y)
        print(f"{button_image} is visible and clicked at {location}.")
    else:
        print(f"{button_image} wasn't found.")
    utl.input_random_sleep()
    return location


# Checks if the image is present on the screen only
def find_image(button_image, region, confidence):
    location = pg.locateOnScreen(button_image, region=region, confidence=confidence)
    if location:
        print(f"{button_image} is visible at {location}.")
    else:
        print(f"{button_image} isn't visible.")
    utl.input_random_sleep()
    return location


# Checks if all marches are in use
def check_marches():
    utl.press_button('J')
    utl.input_random_sleep()
    has_at_least_one_march = find_image(stp.legion_overview, stp.full_screen, stp.more_confidence)
    has_returning_march = find_image(stp.returning_march, stp.full_screen, stp.more_confidence)
    is_marching_to_gather = find_image(stp.marching_to_gather, stp.full_screen, stp.more_confidence)
    if has_returning_march:
        has_all_marches_location = True
        print("There's a march returning, let's wait for it.")
        utl.press_button('space')
        return has_all_marches_location
    elif is_marching_to_gather:
        has_all_marches_location = True
        print("There's a march going to its destination, let's wait for it.")
        utl.press_button('space')
        return has_all_marches_location
    elif has_at_least_one_march:
        has_all_marches_location = find_image(stp.legion_5_out_of_5, stp.full_screen, stp.more_confidence)
        if has_all_marches_location:
            utl.press_button('space')
            print("All marches in use.")
        else:
            utl.press_button('space')
            print("At least one march is free. Proceed.")
        return has_all_marches_location
    else:
        has_all_marches_location = False
        print("No marches in use. Proceed.")
        return has_all_marches_location


# Switch to the given resource (if unselected, tap on the icon)
def switch_resource(target):
    target_selected = None
    target_unselected = None
    match target:
        case "wood":
            target_selected = stp.wood_selected
            target_unselected = stp.wood_unselected
        case "ore":
            target_selected = stp.ore_selected
            target_unselected = stp.ore_unselected
        case "mana":
            target_selected = stp.mana_selected
            target_unselected = stp.mana_unselected
        case "gold":
            target_selected = stp.gold_selected
            target_unselected = stp.gold_unselected

    selected_location = find_image(target_selected, stp.full_screen, stp.general_confidence)
    unselected_location = find_image(target_unselected, stp.full_screen, stp.general_confidence)
    if unselected_location:
        find_and_click(target_unselected, stp.full_screen, stp.general_confidence)
        utl.input_random_sleep()
        print(f"{target} selected, proceed.")
    elif selected_location:
        print(f"{target} selected, proceed.")


# Gather if possible
def gather():
    utl.input_random_sleep()
    has_all_marches_location = check_marches()
    if not has_all_marches_location:
        utl.press_button('space')
        utl.press_button('F')
        print("Looking for a node to farm.")
        switch_resource(stp.gathering_target)
        print("Searching for a node...")
        find_and_click(stp.search_button, stp.full_screen, stp.general_confidence)
        utl.press_button('K')
        find_and_click(stp.gather_button, stp.full_screen, stp.general_confidence)
        create_legions_location = find_and_click(stp.create_legions, stp.full_screen, stp.general_confidence)
        if create_legions_location:
            if not stp.allow_deputy:
                has_deputy = find_image(stp.remove_deputy, stp.full_screen, stp.more_confidence)
                if has_deputy:
                    find_and_click(stp.remove_deputy, stp.full_screen, stp.more_confidence)
                    print("Deputy is removed.")
            find_and_click(stp.march, stp.full_screen, stp.general_confidence)
            utl.press_button('space')
        else:
            utl.press_button('esc')
            utl.press_button('space')


# Checks if game crashed
def check_game_crashed():
    print("Checking if the game has crashed.")
    utl.input_random_sleep()
    confirm_location = find_image(stp.confirm_button, stp.full_screen, stp.general_confidence)
    if confirm_location:
        utl.long_random_sleep()
        find_and_click(stp.confirm_button, stp.full_screen, stp.general_confidence)
        utl.long_random_sleep()
    start_location = find_image(stp.start_cod_icon, stp.full_screen, stp.general_confidence)
    if start_location:
        find_and_click(stp.start_cod_icon, stp.full_screen, stp.general_confidence)
        utl.long_random_sleep()


# Performs the help action if the notification is visible
def do_help():
    utl.press_button('A')
    # utl.random_sleep()
    help_location = find_image(stp.help_icon, stp.full_screen, stp.general_confidence)
    if help_location:
        utl.press_button('B')
    else:
        print("No help requested.")


# Collects the resources based on their images
def collect_resources():
    find_and_click(stp.gold_icon, stp.full_screen, stp.general_confidence)
    find_and_click(stp.mana_icon, stp.full_screen, stp.general_confidence)
    find_and_click(stp.ore_icon, stp.full_screen, stp.general_confidence)
    find_and_click(stp.wood_icon, stp.full_screen, stp.general_confidence)
    print("All resources collected.")


# Makes a donation if an opportunity exists
def make_donation():
    utl.press_button('T')
    # utl.random_sleep()
    donate_button_location = find_image(stp.donate_button, stp.full_screen, stp.more_confidence)
    if donate_button_location:
        find_and_click(stp.donate_button, stp.full_screen, stp.more_confidence)
        print("Donation made.")
    else:
        print("No donations available at the moment.")
    utl.input_random_sleep()
    utl.press_button('esc')


# Get the gifts received
def get_gifts():
    utl.press_button('G')
    rare_selected_location = find_image(stp.rare_gifts_selected, stp.full_screen, stp.more_confidence)
    common_selected_location = find_image(stp.common_gifts_selected, stp.full_screen, stp.more_confidence)
    if rare_selected_location:
        find_and_click(stp.claim_one_button, stp.full_screen, stp.more_confidence)
        print("A rare gift was claimed.")
    elif common_selected_location:
        find_and_click(stp.claim_all_icon, stp.full_screen, stp.more_confidence)
        print("All common gifts were claimed.")
        utl.press_button('esc')
    utl.input_random_sleep()
    utl.press_button('esc')


# Opens alliance menu and make donations / get gifts
def open_alliance():
    alliance_icon_location = find_image(stp.alliance_icon, stp.full_screen, stp.general_confidence)
    if alliance_icon_location:
        utl.press_button('C')
    else:
        utl.press_button('A')
        utl.press_button('C')
    if check_tech_notification():
        make_donation()
    utl.input_random_sleep()
    if check_gift_notification():
        get_gifts()
    utl.input_random_sleep()
    utl.press_button('esc')


# Checks if there's a gift notification
def check_gift_notification():
    gift_notification_location = find_image(stp.gifts_notification, stp.full_screen, stp.more_confidence)
    return gift_notification_location


# Checks if there's a technology donation notification
def check_tech_notification():
    tech_notification_location = find_image(stp.technology_notification, stp.full_screen, stp.more_confidence)
    return tech_notification_location


# Set the initial position in case the bot gets lost:
def set_initial_position():
    map_icon_location = find_image(stp.map_icon, stp.full_screen, stp.more_confidence)
    profile_location = find_image(stp.profile, stp.full_screen, stp.more_confidence)
    if map_icon_location:
        print("Initial position already set.")
        return None
    elif profile_location:
        print("Oops, we are inside the profile page, let's fix it...")
        utl.press_button('esc')
        map_icon_location = find_image(stp.map_icon, stp.full_screen, stp.more_confidence)
        if map_icon_location:
            print("Initial position set.")
            return None
        else:
            utl.press_button('space')
            print("Initial position set.")
            return None
    else:
        utl.press_button('space')
        print("Initial position set.")
        return None


# Train Angels is possible
def train_angels():
    utl.press_button('K')
    find_and_click(stp.celestial_train, stp.full_screen, stp.general_confidence)
    train_location = find_image(stp.train_button, stp.full_screen, stp.general_confidence)
    if train_location:
        find_and_click(stp.train_button, stp.full_screen, stp.general_confidence)
        print("Training more angels...")
        utl.press_button('esc')
    else:
        print("No angels to train now. Skipping...")
        utl.press_button('esc')


# Train Knights is possible
def train_knights():
    utl.press_button('D')
    find_and_click(stp.knight_train, stp.full_screen, stp.general_confidence)
    train_location = find_image(stp.train_button, stp.full_screen, stp.general_confidence)
    if train_location:
        find_and_click(stp.train_button, stp.full_screen, stp.general_confidence)
        print("Training more knights...")
        utl.press_button('esc')
    else:
        print("No knights to train now. Skipping...")
        utl.press_button('esc')


# Train Ballistas is possible
def train_ballistas():
    utl.press_button('L')
    find_and_click(stp.ballista_train, stp.full_screen, stp.general_confidence)
    train_location = find_image(stp.train_button, stp.full_screen, stp.general_confidence)
    if train_location:
        find_and_click(stp.train_button, stp.full_screen, stp.general_confidence)
        print("Training more ballistas...")
        utl.press_button('esc')
    else:
        print("No ballistas to train now. Skipping...")
        utl.press_button('esc')


# Train Vestals is possible
def train_vestals():
    utl.press_button('I')
    find_and_click(stp.abbey_train, stp.full_screen, stp.general_confidence)
    train_location = find_image(stp.train_button, stp.full_screen, stp.general_confidence)
    if train_location:
        find_and_click(stp.train_button, stp.full_screen, stp.general_confidence)
        print("Training more vestals...")
        utl.press_button('esc')
    else:
        print("No vestals to train now. Skipping...")
        utl.press_button('esc')


# Train Swordsmen is possible
def train_swordsmen():
    utl.press_button('E')
    find_and_click(stp.swordsmen_train, stp.full_screen, stp.general_confidence)
    train_location = find_image(stp.train_button, stp.full_screen, stp.general_confidence)
    if train_location:
        find_and_click(stp.train_button, stp.full_screen, stp.general_confidence)
        print("Training more swordsmen...")
        utl.press_button('esc')
    else:
        print("No swordsmen to train now. Skipping...")
        utl.press_button('esc')


# Checks training camps
def check_training_camps():
    set_initial_position()
    train_angels()
    train_knights()
    train_ballistas()
    train_vestals()
    train_swordsmen()
