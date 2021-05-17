from datetime import date
from calendar import monthrange


class MeetupDayException(Exception):
    pass


def meetup(year: int, month: int, week: str, day_of_week: str):
    indices = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}
    dates = [date(year, month, i) for i in range(1, monthrange(year, month)[
        1]+1) if date(year, month, i).strftime('%A') == day_of_week]

    if week in indices:
        try:
            Date = dates[indices[week]]
        except IndexError:
            raise MeetupDayException('Incorrect input for day of week')
    elif week == 'teenth':
        Date = [Date for Date in dates if 13 <= Date.day <= 19][0]
    else:
        raise ValueError('Incorrect input for week of month')

    return Date
