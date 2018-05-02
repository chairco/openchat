from datetime import datetime, timedelta, timezone, time
from dateutil.parser import parse
import pytz


def convert_to_utc(talk_time, date_mention=False):
    """Convert the datetime string we get from SUTime to utcnow"""
    local_tz = pytz.timezone('US/Eastern')
    parsed_tt = pytz.utc.localize(parse(talk_time))
    utc_aware_now = datetime.utcnow().replace(tzinfo=pytz.utc)

    # diff needed for time mentions in future extracted with SUTime
    days_diff = (parsed_tt - utc_aware_now).days

    # get local year, month, day 
    local_date = datetime.now(local_tz)
    local_date_str = datetime.strftime(local_date, "%Y %m %d")
    year, month, day = local_date_str.split(" ")

    if date_mention:
        # quick fix to change date to valid pycon date if date not picked up by SUTime
        month, day = date_mention[0].split("/")
        month = "0" + month

    # get SUTime parsed talk time and extract hours, mins
    local_time_str = datetime.strftime(parsed_tt, "%H %M")
    hours, mins = local_time_str.split(" ")

    # build up correct datetime obj, normalize & localize, switch to utc 
    correct_dt = datetime(int(year), int(month), int(day), int(hours), int(mins))
    correct_dt += timedelta(days=days_diff)
    tz_aware_local = local_tz.normalize(local_tz.localize(correct_dt))
    local_as_utc = tz_aware_local.astimezone(pytz.utc)

    return local_as_utc

def get_local_clock_time():
    local_dt = datetime.now(pytz.timezone('US/Pacific'))
    local_clock_time = datetime.strftime(local_dt, "%H:%M")
    return local_clock_time

def check_start_time(talk_time):
    """If time of openspaces talk within next 30 mins return True"""
    time_diff = talk_time - datetime.now(timezone.utc)
    threshold = timedelta(minutes=30)

    if time_diff < threshold:
        return True
    else:
        return False
