from datetime import datetime
import time
import winsound  # Windows only, for playing sound

def set_alarm():
    try:
        alarm_time_str = input("Enter the alarm time (HH:MM AM/PM): ")
        alarm_time = datetime.strptime(alarm_time_str, "%I:%M %p")
        return alarm_time
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM AM/PM.")
        return set_alarm()

def alarm_clock(alarm_time):
    while True:
        current_time = datetime.now().strftime("%I:%M %p")
        if current_time == alarm_time.strftime("%I:%M %p"):
            print("Alarm! Wake up!")
            play_alarm_sound()
            break
        time.sleep(1)

def play_alarm_sound():
    try:
        winsound.Beep(1000, 2000)  # Windows only, plays a beep sound for 2 seconds
    except AttributeError:
        print("Beep sound not supported on this platform.")

def main():
    print("Welcome to the Alarm Clock Program!")

    alarm_time = set_alarm()

    print(f"Alarm set for {alarm_time.strftime('%I:%M %p')}")
    alarm_clock(alarm_time)

if __name__ == "__main__":
    main()
