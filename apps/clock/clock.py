from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

class Clock:
    def __init__(self, tz="Asia/Tokyo", skew_hours=0.0):
        """
        skew_hours: Time drift within the system
        """
        self.tz_name = tz
        self.tz = tz
        self._tz = ZoneInfo(tz)
        self._skew = timedelta(hours=skew_hours)


    def now(self):
        """
        return now time
        """
        return (datetime.now(timezone.utc) - self._skew).astimezone(self._tz)