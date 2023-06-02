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
        print(f"{button_image} is visible and clicked at {location}")
    else:
        print(f"{button_image} not found")
    utl.input_random_sleep()
    return location


# Checks if the image is present on the screen only
def find_image(button_image, region, confidence):
    location = pg.locateOnScreen(button_image, region=region, confidence=confidence)
    if location:
        print(f"{button_image} is present at {location}")
    else:
        print(f"{button_image} isn't present")
    utl.input_random_sleep()
    return location


# Gather if possible
def gather():
    utl.press_button('space')
    utl.input_random_sleep()
    utl.press_button('J')
    utl.input_random_sleep()
    has_all_marches_location = find_image(stp.legion_5_out_of_5, stp.full_screen, stp.more_confidence)
    if has_all_marches_location:
        utl.press_button('esc')
        utl.press_button('space')
        print("All marches in use.")
    else:
        utl.input_random_sleep()
        utl.press_button('esc')
        utl.press_button('F')
        print("Looking for a node to farm.")
        if stp.gathering_target == "wood":
            selected_location = find_image(stp.logging_camp_selected, stp.full_screen, stp.general_confidence)
            unselected_location = find_image(stp.logging_camp_unselected, stp.full_screen, stp.general_confidence)
            if unselected_location:
                find_and_click(stp.logging_camp_unselected, stp.full_screen, stp.general_confidence)
                utl.input_random_sleep()
            elif selected_location:
                print("Camp already selected, proceeding...")
                utl.random_sleep()
                find_and_click(stp.search_button, stp.full_screen, stp.general_confidence)
                utl.random_sleep()
                utl.press_button('K')
                utl.random_sleep()
                find_and_click(stp.gather_button, stp.full_screen, stp.general_confidence)
                utl.random_sleep()
                find_and_click(stp.create_legions, stp.full_screen, stp.general_confidence)
                utl.random_sleep()
                find_and_click(stp.create_legions, stp.full_screen, stp.general_confidence)
                has_deputy = find_image(stp.remove_deputy, stp.full_screen, stp.more_confidence)
                if has_deputy:
                    find_and_click(stp.remove_deputy, stp.full_screen, stp.more_confidence)
                    print("Deputy is removed.")
                utl.random_sleep()
                find_and_click(stp.march, stp.full_screen, stp.general_confidence)
                utl.press_button('space')


# Checks if game crashed
def check_game_crashed():
    print("checking if game crashed")
    utl.input_random_sleep()
    confirm_location = find_image(stp.confirm_button, stp.full_screen, stp.general_confidence)
    if confirm_location:
        utl.long_random_sleep()
        find_and_click(stp.confirm_button, stp.full_screen, stp.general_confidence)
        utl.long_random_sleep()
        find_and_click(stp.start_cod_icon, stp.full_screen, stp.general_confidence)
        utl.long_random_sleep()


# Performs the help action if the notification is visible
def do_help():
    utl.press_button('A')
    utl.random_sleep()
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
    utl.random_sleep()
    donate_button_location = find_image(stp.donate_button, stp.full_screen, stp.more_confidence)
    if donate_button_location:
        find_and_click(stp.donate_button, stp.full_screen, stp.more_confidence)
        print("Donation made.")
    else:
        print("No donations available at the moment.")
    utl.random_sleep()
    utl.press_button('esc')


# Get the gifts received
def get_gifts():
    utl.press_button('G')
    utl.random_sleep()
    rare_selected_location = find_image(stp.rare_gifts_selected, stp.full_screen, stp.more_confidence)
    common_selected_location = find_image(stp.common_gifts_selected, stp.full_screen, stp.more_confidence)
    if rare_selected_location:
        find_and_click(stp.claim_one_button, stp.full_screen, stp.more_confidence)
        print("Rare gift claimed.")
    elif common_selected_location:
        find_and_click(stp.claim_all_icon, stp.full_screen, stp.more_confidence)
        print("All common gifts claimed.")
        utl.press_button('esc')
    utl.random_sleep()
    utl.press_button('esc')


# Opens alliance menu and make donations / get gifts
def open_alliance():
    alliance_icon_location = find_image(stp.alliance_icon, stp.full_screen, stp.general_confidence)
    if alliance_icon_location:
        utl.press_button('C')
        utl.input_random_sleep()
    else:
        utl.press_button('A')
        utl.input_random_sleep()
        utl.press_button('C')
        utl.input_random_sleep()
    make_donation()
    utl.random_sleep()
    get_gifts()
    utl.random_sleep()
    utl.press_button('esc')
