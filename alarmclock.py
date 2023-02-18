from playsound import playsound
import time

CLEAR = "\033[2j]"
CLEAR_AND_RETURN = "\033[H]"

def alarm(seconds):
  time_elapsed = 0

  print(CLEAR)
  while time_elapsed < seconds:
    time.sleep(1)
    time_elapsed += 1

    time_left = seconds - time_elapsed
    minutes_left = time_left // 60

    seconds_left = time_left % 60

    print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

  playsound("alarm.wav")

mintues = int(input("How many mintues to wati: "))
seconds = int(input("HOw mnay seconds to wati: "))
total_seconds = mintues * 60 + seconds
alarm(total_seconds)