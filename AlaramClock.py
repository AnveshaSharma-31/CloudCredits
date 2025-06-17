import datetime
import time
import winsound  # For Windows beep sound; for other OS, alternatives below

def get_alarm_time():
    print("Set your alarm (24-hour format).")
    year = int(input("Year (e.g., 2025): "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))
    second = int(input("Second (0-59): "))

    try:
        alarm_time = datetime.datetime(year, month, day, hour, minute, second)
        return alarm_time
    except ValueError:
        print("Invalid date/time entered. Please try again.")
        return None

def alarm_clock():
    alarm_time = None
    while alarm_time is None:
        alarm_time = get_alarm_time()

    print(f"Alarm set for: {alarm_time}")
    print("Waiting for alarm...")

    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print("Wake up! Alarm ringing!")
            for _ in range(5):  # Beep 5 times
                winsound.Beep(1000, 500)  # Frequency 1000 Hz, duration 500 ms
                time.sleep(0.5)
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
