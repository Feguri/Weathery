import os
import requests
from collections import defaultdict, Counter
from datetime import datetime


class ForecastData:
    def __init__(self, lat, lon):

        self.ApiKey = os.getenv(
            'OPENWEATHER_API_KEY',
            '1e9e9de5ee2fe2c660df35054541f17c'
        )

        endpoint = "https://api.openweathermap.org/data/2.5/forecast"

        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.ApiKey,
            "units": "metric"
        }

        resp = requests.get(endpoint, params=params)
        resp.raise_for_status()

        data = resp.json()

        # Aggregate 3-hour samples into daily groups
        days = defaultdict(lambda: {"temps": [], "conds": []})

        for item in data.get("list", []):
            ts = item.get("dt")
            if not ts:
                continue

            day_key = datetime.utcfromtimestamp(ts).date()

            temp = item["main"].get("temp")
            if temp is not None:
                days[day_key]["temps"].append(temp)

            condition = item["weather"][0].get("main")
            if condition:
                days[day_key]["conds"].append(condition)

        ordered_dates = sorted(days.keys())

        max_c = []
        min_c = []
        conds = []

        for d in ordered_dates:
            temps = days[d]["temps"]

            if temps:
                max_c.append(int(round(max(temps))))
                min_c.append(int(round(min(temps))))
            else:
                max_c.append(None)
                min_c.append(None)

            if days[d]["conds"]:
                dominant = Counter(days[d]["conds"]).most_common(1)[0][0]
                conds.append(dominant)
            else:
                conds.append(None)

        # Pad to 8 days to preserve legacy UI expectations
        def pad(lst, size=8):
            if not lst:
                return [None] * size
            while len(lst) < size:
                lst.append(lst[-1])
            return lst[:size]

        self.MaxTempListC = pad(max_c)
        self.MinTempListC = pad(min_c)
        self.ConditionsList = pad(conds)

        names = ("Zero","One","Two","Three","Four","Five","Six","Seven")

        for i in range(8):
            setattr(self, f"Max{names[i]}C", self.MaxTempListC[i])
            setattr(self, f"Min{names[i]}C", self.MinTempListC[i])

        def c_to_f(c):
            return int(round((c * 9/5) + 32)) if c is not None else None

        for i in range(8):
            setattr(self, f"Max{names[i]}F", c_to_f(self.MaxTempListC[i]))
            setattr(self, f"Min{names[i]}F", c_to_f(self.MinTempListC[i]))

        # ConditionOne..ConditionSeven
        cond_names = ("One","Two","Three","Four","Five","Six","Seven")

        for i in range(1, 8):
            setattr(self, f"Condition{cond_names[i-1]}",
                    self.ConditionsList[i])