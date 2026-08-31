def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = (seconds - hours * 3600)- minutes * 60

    if hours < 10:
        hours = str(f'0{hours}')
    if minutes < 10:
        minutes = str(f'0{minutes}')
    if seconds < 10:
        seconds = str(f'0{seconds}')


    return f"{hours}:{minutes}:{seconds}"

def make_readable_opt(seconds):
    hours,rem = divmod(seconds,3600)
    minutes,seconds = divmod(rem, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"