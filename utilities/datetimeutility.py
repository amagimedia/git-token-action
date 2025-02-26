from datetime import datetime
from datetime import timedelta

def get_current_timestamp():
    current_timestamp = datetime.now().timestamp()
    return current_timestamp


def add_time_to_timestamp(current_timestamp, time_to_add, time_unit="secs"):
    """
    Add time to a timestamp.

    Parameters:
    current_timestamp (float): The starting timestamp.
    time_to_add (int): The time to add.
    time_unit (str, optional): The unit of time to add (months, weeks, days, hrs, mins, secs). Defaults to "secs".

    Returns:
    float: The updated timestamp.

    """
    # Convert the timestamp to a datetime object
    dt = datetime.fromtimestamp(current_timestamp)

    if time_unit=="months":
        dt += timedelta(days=time_to_add*30)
    elif time_unit=="weeks":
        dt += timedelta(weeks=time_to_add)
    elif time_unit=="days":
        dt += timedelta(days=time_to_add)
    elif time_unit=="hrs":
        dt += timedelta(hours=time_to_add)
    elif time_unit=="mins":
        dt += timedelta(minutes=time_to_add)
    elif time_unit=="secs":
        dt += timedelta(seconds=time_to_add)

    # Get the timestamp from the datetime object
    timestamp = dt.timestamp()

    return timestamp