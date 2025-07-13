import datetime

def time_until_next_5_minute_interval():
  """
  Calculates the time remaining until the next 5-minute interval.

  Returns:
    A timedelta object representing the time until the next 5-minute mark.
  """
  now = datetime.datetime.now()
  minutes_to_add = 5 - (now.minute % 5)
  next_interval = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=minutes_to_add)
  wait_time = int((next_interval - now).total_seconds())
  return wait_time

# Example usage:
time_left = time_until_next_5_minute_interval()
print(f"Time until next 5-minute interval: {time_left}")