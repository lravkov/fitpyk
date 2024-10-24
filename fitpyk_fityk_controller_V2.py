from pynput.keyboard import Key, Controller
import time


def create_controller():
    keyboard = Controller()
    return keyboard


def initial_wait(initial_delay_p):
    # initial wait
    time.sleep(initial_delay_p)


def press_windows_key(keyboard_p, delay_p):
    # open windows menu
    keyboard_p.press(Key.cmd)
    keyboard_p.release(Key.cmd)
    time.sleep(delay_p)


def type_fityk_string(keyboard_p, delay_p):
    # type in fityk
    keyboard_p.type('fityk')  # changed to 'fit' because it was going to the cli version, was 'fityk' before
    time.sleep(10 * delay_p)  # changed on 13 Aug 2023 to improve stability [used to be: delay_p]


def press_enter_key(keyboard_p, delay_p):
    # hit enter
    keyboard_p.press(Key.enter)
    keyboard_p.release(Key.enter)
    # give fityk a full second to start up
    time.sleep(10 * delay_p)


def press_tab_key(keyboard_p, delay_p):
    # hit tab twice to get out of the fityk typing field
    keyboard_p.press(Key.tab)
    keyboard_p.release(Key.tab)
    time.sleep(delay_p)
    # keyboard.press(Key.tab)
    # keyboard.release(Key.tab)
    # time.sleep(delay)


def press_ctrl_plus_x(keyboard_p, delay_p):
    # keypress ctrl + x to allow for a script to be run
    with keyboard_p.pressed(Key.ctrl):
        keyboard_p.press('x')
        keyboard_p.release('x')
    time.sleep(delay_p)


def type_sample_name(keyboard_p, sample_name_p, delay_p):
    # type in the name of the script
    keyboard_p.type(sample_name_p)
    keyboard_p.type(".fit")
    time.sleep(delay_p)

# hit enter to run the script
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)


def quit_fityk(delay_p):
    keyboard_p = create_controller()
    # keypress alt + f4 to quit fityk
    with keyboard_p.pressed(Key.alt):
        keyboard_p.press(Key.f4)
        keyboard_p.release(Key.f4)
    time.sleep(delay_p)


def call_script_in_fityk(script_name_p, delay_p, initial_delay_p):
    keyboard_p = create_controller()
    initial_wait(initial_delay_p)
    press_windows_key(keyboard_p, delay_p)
    type_fityk_string(keyboard_p, delay_p)
    press_enter_key(keyboard_p, delay_p)
    time.sleep(12 * delay_p)  # added 15 Aug 2023 for stability
    press_tab_key(keyboard_p, delay_p)
    press_tab_key(keyboard_p, delay_p)
    press_ctrl_plus_x(keyboard_p, delay_p)
    # time.sleep(12 * delay_p)  # Can uncomment this if fityk is not typing the correct script name in
    type_sample_name(keyboard_p, script_name_p, delay_p)
    press_enter_key(keyboard_p, delay_p)


def wait_10_delays(delay_p):
    time.sleep(10*delay_p)


if __name__ == "__main__":
    initial_delay = 1
    delay = 0.1
    script_name = '_script_k_sample'

    call_script_in_fityk(script_name, delay, initial_delay)
