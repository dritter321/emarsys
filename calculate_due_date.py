from datetime import datetime, timedelta

## CURRENT ISSUE
#The turnaround time is defined in working hours (e.g. 2 days equal 16 hours).
#If a problem was reported at 2:12PM on Tuesday and the turnaround time is
#16 hours, then it is due by 2:12PM on Thursday.

WORK_START = 9
WORK_END = 17
WORK_DAY_HOURS = WORK_END - WORK_START
TIME_ZONE = "X"


def calculate_due_date(submit_datetime, turnaround_time_hours):
    if not (WORK_START <= submit_datetime.hour < WORK_END):
        raise ValueError("Submit time must be within working hours (9AM to 5PM).")

    current_datetime = submit_datetime
    remaining_hours = turnaround_time_hours

    while remaining_hours > 0:
        if WORK_START <= current_datetime.hour < WORK_END:  # Within working hours
            # Calculate hours left in the current workday
            hours_left_today = WORK_END - current_datetime.hour
            if remaining_hours <= hours_left_today:
                # If turnaround fits in the remaining time on the current day
                return current_datetime + timedelta(hours=remaining_hours)
            else:
                # Move to the next day and decrease remaining hours
                remaining_hours -= hours_left_today
                current_datetime = move_to_next_working_day(current_datetime)
        else:
            # Outside working hours, move to start of next working day
            current_datetime = move_to_next_working_day(current_datetime)

    return current_datetime


def move_to_next_working_day(current_datetime):
    # Increment day
    next_day = current_datetime + timedelta(days=1)
    # If weekend, skip to Monday
    while next_day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        next_day += timedelta(days=1)
    # Reset to start of working hours (9AM)
    return next_day.replace(hour=WORK_START, minute=0, second=0, microsecond=0)


if __name__ == "__main__":
    submit_time = datetime(2023, 10, 3, 14, 12)  # Example: Tuesday 2:12PM
    turnaround_time = 16  # 16 working hours
    due_date = calculate_due_date(submit_time, turnaround_time)
    print("Due Date:", due_date)