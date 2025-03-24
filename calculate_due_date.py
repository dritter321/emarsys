from datetime import datetime, timedelta


WORK_START = 9
WORK_END = 17
WORK_DAY_HOURS = WORK_END - WORK_START

def calculate_due_date(submit_datetime, turnaround_time_hours):
    if not (WORK_START <= submit_datetime.hour < WORK_END):
        raise ValueError("Submit time must be within working hours (9AM to 5PM).")

    resolved_datetime = submit_datetime
    remaining_minutes = turnaround_time_hours * 60  # Turnaround in minutes

    while remaining_minutes > 0:
        # Same day calculations
        if WORK_START <= resolved_datetime.hour < WORK_END:
            end_of_workday = resolved_datetime.replace(hour=WORK_END, minute=0, second=0, microsecond=0)
            minutes_left_today = int((end_of_workday - resolved_datetime).total_seconds() / 60)
            if remaining_minutes <= minutes_left_today:
                # Same day finishing
                return resolved_datetime + timedelta(minutes=remaining_minutes)
            else:
                # Moving over the time to next day
                remaining_minutes -= minutes_left_today
                resolved_datetime = move_to_next_working_day(resolved_datetime)
    return resolved_datetime


def move_to_next_working_day(current_datetime):
    next_day = current_datetime + timedelta(days=1)
    # If weekend, skip to Monday
    while next_day.weekday() >= 5:
        next_day += timedelta(days=1)
    return next_day.replace(hour=WORK_START, minute=0, second=0, microsecond=0)


if __name__ == "__main__":
    # Example usage
    submit_time = datetime(2023, 10, 3, 14, 12)  # Example: Tuesday 2:12PM
    turnaround_time = 16
    due_date = calculate_due_date(submit_time, turnaround_time)
    print("Due Date:", due_date)