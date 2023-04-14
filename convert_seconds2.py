def convert_seconds(time):
    if isinstance(time, str):
        try:
            seconds = int(time)
        except ValueError:
            return "Invalid input. Please enter a valid integer or string representation of an integer."
    elif isinstance(time, int):
        seconds = time
    else:
        return "Invalid input. Please enter a valid integer or string representation of an integer."
    
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365
    
    result = []
    if years:
        result.append(f"{years} year{'s' if years > 1 else ''}")
    if days % 365:
        result.append(f"{days % 365} day{'s' if days % 365 > 1 else ''}")
    if hours % 24:
        result.append(f"{hours % 24} hour{'s' if hours % 24 > 1 else ''}")
    if minutes % 60:
        result.append(f"{minutes % 60} minute{'s' if minutes % 60 > 1 else ''}")
    if seconds % 60:
        result.append(f"{seconds % 60} second{'s' if seconds % 60 > 1 else ''}")
    
    return ', '.join(result)
  
# >>> convert_seconds(123456)
# '1 day, 10 hours, 17 minutes, 36 seconds'
# 
# >>> convert_seconds("123456")
# '1 day, 10 hours, 17 minutes, 36 seconds'
# 
# >>> convert_seconds("not an integer")
# 'Invalid input. Please enter a valid integer or string representation of an integer.'
