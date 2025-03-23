import datetime
import random

def generate_delayed_random_event_time(original_time):
    current_time = datetime.datetime.now()

    # Convert the original event_time from string to datetime
    original_datetime = datetime.datetime.strptime(original_time, "%Y-%m-%d %H:%M:%S")

    # Ensure the new timestamp falls between now and the original time
    random_time_delta = datetime.timedelta(seconds=random.randint(0, int((current_time - original_datetime).total_seconds())))
    return (current_time - random_time_delta).strftime("%Y-%m-%d %H:%M:%S")