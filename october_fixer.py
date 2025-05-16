
from os.path import join
import polars as pl

flights_df: pl.DataFrame = pl.read_csv(join("flight_data", "flights.csv"))
i = 0
print(flights_df.columns)
for grouped_flights in flights_df.unique(
    subset=["FLIGHT_NUMBER", "SCHEDULED_DEPARTURE"]
)[
    [
        "FLIGHT_NUMBER",
        "DISTANCE",
        "SCHEDULED_DEPARTURE",
        "ORIGIN_AIRPORT",
        "DESTINATION_AIRPORT",
    ]
].group_by(
    ["FLIGHT_NUMBER", "DISTANCE"]
):

    print(grouped_flights)
    i += 1
    if i > 100:
        break
