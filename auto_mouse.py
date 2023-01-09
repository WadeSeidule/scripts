import time
import datetime
import random
import argparse
import pyautogui as gui

def is_within_time(start_time: datetime.datetime, time: int) -> bool:
    if start_time + datetime.timedelta(minutes=time) < datetime.datetime.now():
        return False

    time_left = (start_time + datetime.timedelta(minutes=time)) - datetime.datetime.now()
    time_left_str = str(time_left).split(".")[0]
    print("time left:", time_left_str, end="\r")
    return True

def random_coord() -> tuple[int,int]:
    return random.randint(600, 700), random.randint(200, 600)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", default=10, type=int)
    args = parser.parse_args()

    run_time = args.time

    start_time = datetime.datetime.now()

    while is_within_time(start_time, run_time):
        x, y = random_coord()
        gui.moveTo(x, y, .5)
        time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()