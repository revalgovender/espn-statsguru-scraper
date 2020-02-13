import requests
from bs4 import BeautifulSoup
import csv

# Config.
BASE_URL = 'http://stats.espncricinfo.com/ci/engine/stats/index.html'
CSV_WRITE_PATH = 'data/top_test_run_scores.csv'
FIELD_1 = 'date'
FIELD_2 = 'name'
FIELD_3 = 'category'
FIELD_4 = 'value'
CSV_FIELDS = [FIELD_1, FIELD_2, FIELD_3, FIELD_4]

# Data.
RANKS_AS_STRINGS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                    "19", "20"]
months = [
    {
        "date": "2010-01-01",
        "max": "31+Jan+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-02-01",
        "max": "28+Feb+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-03-01",
        "max": "31+Mar+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-04-01",
        "max": "30+Apr+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-05-01",
        "max": "31+May+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-06-01",
        "max": "30+Jun+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-07-01",
        "max": "31+Jul+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-08-01",
        "max": "31+Aug+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-09-01",
        "max": "30+Sep+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-10-01",
        "max": "31+Oct+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-11-01",
        "max": "30+Nov+2010",
        "min": "01+Jan+2010",
    },
    {
        "date": "2010-12-01",
        "max": "31+Dec+2010",
        "min": "01+Jan+2010",
    },
]
players = []

for month in months:
    print("Start processing: " + month['max'])

    # Fetch data.
    QUERY_PARAMETERS = '?class=1;spanmax2=' \
                       + month['max'] \
                       + ';spanmin2=' \
                       + month['min'] \
                       + ';spanval2=span;template=results;type=batting'

    print("Make request to: " + BASE_URL + QUERY_PARAMETERS)

    response = requests.get(BASE_URL + QUERY_PARAMETERS)
    htmlSoup = BeautifulSoup(response.content, 'html.parser')

    # Parse data.
    for rank_as_string in RANKS_AS_STRINGS:
        print("Parsing rank: " + rank_as_string)

        player_name = htmlSoup.select(
            "#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > tbody > tr:nth-child("
            + rank_as_string
            + ") > td.left > a")[0].text
        runs = htmlSoup.select(
            "#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > tbody > tr:nth-child("
            + rank_as_string
            + ") > td:nth-child(5) > b")[0].text
        players.append({
            FIELD_1: month['date'],
            FIELD_2: player_name,
            FIELD_3: player_name,
            FIELD_4: runs
        })

    print("End processing: " + month['max'])

# Export data to CSV
with open(CSV_WRITE_PATH, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
    writer.writeheader()

    for player in players:
        writer.writerow(player)
