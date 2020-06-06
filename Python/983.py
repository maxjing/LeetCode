class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_dict = Counter(days)
        print(days_dict)
        # create days table from day 0 to last day plus one
        table = [0 for i in range(0, days[-1] + 1)]
        for i in range(0, days[-1] + 1):
            # If the current day is not present in the travel days dictionary, it takes the previous value
            if i not in days_dict:
                table[i] = table[i - 1]
            else:
                # Used max to identify if the index exists
                # it's a minimum of yesterday's cost plus single-day ticket, or cost for 8 days ago plus 7-day pass, or cost 31 days ago plus 30-day pass.
                table[i] = min(
                    table[max(0, i - 1)] + costs[0],  # per days value
                    table[max(0, i - 7)] + costs[1],  # per week value
                    table[max(0, i - 30)] + costs[2]  # per year value
                )

        return table[-1]