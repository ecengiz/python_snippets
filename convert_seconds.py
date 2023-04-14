def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes, and {remaining_seconds} seconds"

#print(convert_seconds(123456))
# Output: 1 days, 10 hours, 17 minutes, and 36 seconds
