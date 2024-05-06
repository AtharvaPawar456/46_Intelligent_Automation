from datetime import datetime

def calculate_time_difference(checkin, checkout):
    # Parse the checkin and checkout times into datetime objects
    checkin_time = datetime.strptime(checkin, "%H:%M")
    checkout_time = datetime.strptime(checkout, "%H:%M")

    # Calculate the time difference
    time_difference = checkout_time - checkin_time

    # Return the time difference as a timedelta object
    return time_difference

# Example usage
checkin = "9:00"
checkout = "17:00"
time_diff = calculate_time_difference(checkin, checkout)
print("Time difference:", time_diff)
