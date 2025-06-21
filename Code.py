import time
import os
import platform

WORK_DURATION = 3 * 60
SHORT_BREAK = 2 * 60
LONG_BREAK = 1 * 60
SESSIONS_BEFORE_LONG_BREAK = 4

def alert():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        print('\a')

def countdown(seconds, label):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{label} - {mins:02d}:{secs:02d}"
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print(f"{label} completed!{' ' * 20}")
    alert()

def start_pomodoro():
    session_count = 0
    while True:
        session_count += 1
        print(f"\nStarting Work Session {session_count}")
        countdown(WORK_DURATION, "Work")

        if session_count % SESSIONS_BEFORE_LONG_BREAK == 0:
            print("Long Break Time!")
            countdown(LONG_BREAK, "Long Break")
        else:
            print("Short Break Time!")
            countdown(SHORT_BREAK, "Short Break")

        user_input = input("Continue to next session? (y/n): ").strip().lower()
        if user_input != 'y':
            print("Pomodoro session ended.")
            break


start_pomodoro()
