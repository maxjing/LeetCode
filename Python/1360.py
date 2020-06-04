class Solution:

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((date2 - date1).days)