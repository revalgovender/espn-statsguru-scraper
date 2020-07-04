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
months = [{'date': '1990-01-01', 'max': '31+Jan+1990', 'min': '01+Jan+1990'}, {'date': '1990-02-01', 'max': '28+Feb+1990', 'min': '01+Jan+1990'}, {'date': '1990-03-01', 'max': '31+Mar+1990', 'min': '01+Jan+1990'}, {'date': '1990-04-01', 'max': '30+Apr+1990', 'min': '01+Jan+1990'}, {'date': '1990-05-01', 'max': '31+May+1990', 'min': '01+Jan+1990'}, {'date': '1990-06-01', 'max': '30+Jun+1990', 'min': '01+Jan+1990'}, {'date': '1990-07-01', 'max': '31+Jul+1990', 'min': '01+Jan+1990'}, {'date': '1990-08-01', 'max': '31+Aug+1990', 'min': '01+Jan+1990'}, {'date': '1990-09-01', 'max': '30+Sep+1990', 'min': '01+Jan+1990'}, {'date': '1990-10-01', 'max': '31+Oct+1990', 'min': '01+Jan+1990'}, {'date': '1990-11-01', 'max': '30+Nov+1990', 'min': '01+Jan+1990'}, {'date': '1990-12-01', 'max': '31+Dec+1990', 'min': '01+Jan+1990'}, {'date': '1991-01-01', 'max': '31+Jan+1991', 'min': '01+Jan+1990'}, {'date': '1991-02-01', 'max': '28+Feb+1991', 'min': '01+Jan+1990'}, {'date': '1991-03-01', 'max': '31+Mar+1991', 'min': '01+Jan+1990'}, {'date': '1991-04-01', 'max': '30+Apr+1991', 'min': '01+Jan+1990'}, {'date': '1991-05-01', 'max': '31+May+1991', 'min': '01+Jan+1990'}, {'date': '1991-06-01', 'max': '30+Jun+1991', 'min': '01+Jan+1990'}, {'date': '1991-07-01', 'max': '31+Jul+1991', 'min': '01+Jan+1990'}, {'date': '1991-08-01', 'max': '31+Aug+1991', 'min': '01+Jan+1990'}, {'date': '1991-09-01', 'max': '30+Sep+1991', 'min': '01+Jan+1990'}, {'date': '1991-10-01', 'max': '31+Oct+1991', 'min': '01+Jan+1990'}, {'date': '1991-11-01', 'max': '30+Nov+1991', 'min': '01+Jan+1990'}, {'date': '1991-12-01', 'max': '31+Dec+1991', 'min': '01+Jan+1990'}, {'date': '1992-01-01', 'max': '31+Jan+1992', 'min': '01+Jan+1990'}, {'date': '1992-02-01', 'max': '28+Feb+1992', 'min': '01+Jan+1990'}, {'date': '1992-03-01', 'max': '31+Mar+1992', 'min': '01+Jan+1990'}, {'date': '1992-04-01', 'max': '30+Apr+1992', 'min': '01+Jan+1990'}, {'date': '1992-05-01', 'max': '31+May+1992', 'min': '01+Jan+1990'}, {'date': '1992-06-01', 'max': '30+Jun+1992', 'min': '01+Jan+1990'}, {'date': '1992-07-01', 'max': '31+Jul+1992', 'min': '01+Jan+1990'}, {'date': '1992-08-01', 'max': '31+Aug+1992', 'min': '01+Jan+1990'}, {'date': '1992-09-01', 'max': '30+Sep+1992', 'min': '01+Jan+1990'}, {'date': '1992-10-01', 'max': '31+Oct+1992', 'min': '01+Jan+1990'}, {'date': '1992-11-01', 'max': '30+Nov+1992', 'min': '01+Jan+1990'}, {'date': '1992-12-01', 'max': '31+Dec+1992', 'min': '01+Jan+1990'}, {'date': '1993-01-01', 'max': '31+Jan+1993', 'min': '01+Jan+1990'}, {'date': '1993-02-01', 'max': '28+Feb+1993', 'min': '01+Jan+1990'}, {'date': '1993-03-01', 'max': '31+Mar+1993', 'min': '01+Jan+1990'}, {'date': '1993-04-01', 'max': '30+Apr+1993', 'min': '01+Jan+1990'}, {'date': '1993-05-01', 'max': '31+May+1993', 'min': '01+Jan+1990'}, {'date': '1993-06-01', 'max': '30+Jun+1993', 'min': '01+Jan+1990'}, {'date': '1993-07-01', 'max': '31+Jul+1993', 'min': '01+Jan+1990'}, {'date': '1993-08-01', 'max': '31+Aug+1993', 'min': '01+Jan+1990'}, {'date': '1993-09-01', 'max': '30+Sep+1993', 'min': '01+Jan+1990'}, {'date': '1993-10-01', 'max': '31+Oct+1993', 'min': '01+Jan+1990'}, {'date': '1993-11-01', 'max': '30+Nov+1993', 'min': '01+Jan+1990'}, {'date': '1993-12-01', 'max': '31+Dec+1993', 'min': '01+Jan+1990'}, {'date': '1994-01-01', 'max': '31+Jan+1994', 'min': '01+Jan+1990'}, {'date': '1994-02-01', 'max': '28+Feb+1994', 'min': '01+Jan+1990'}, {'date': '1994-03-01', 'max': '31+Mar+1994', 'min': '01+Jan+1990'}, {'date': '1994-04-01', 'max': '30+Apr+1994', 'min': '01+Jan+1990'}, {'date': '1994-05-01', 'max': '31+May+1994', 'min': '01+Jan+1990'}, {'date': '1994-06-01', 'max': '30+Jun+1994', 'min': '01+Jan+1990'}, {'date': '1994-07-01', 'max': '31+Jul+1994', 'min': '01+Jan+1990'}, {'date': '1994-08-01', 'max': '31+Aug+1994', 'min': '01+Jan+1990'}, {'date': '1994-09-01', 'max': '30+Sep+1994', 'min': '01+Jan+1990'}, {'date': '1994-10-01', 'max': '31+Oct+1994', 'min': '01+Jan+1990'}, {'date': '1994-11-01', 'max': '30+Nov+1994', 'min': '01+Jan+1990'}, {'date': '1994-12-01', 'max': '31+Dec+1994', 'min': '01+Jan+1990'}, {'date': '1995-01-01', 'max': '31+Jan+1995', 'min': '01+Jan+1990'}, {'date': '1995-02-01', 'max': '28+Feb+1995', 'min': '01+Jan+1990'}, {'date': '1995-03-01', 'max': '31+Mar+1995', 'min': '01+Jan+1990'}, {'date': '1995-04-01', 'max': '30+Apr+1995', 'min': '01+Jan+1990'}, {'date': '1995-05-01', 'max': '31+May+1995', 'min': '01+Jan+1990'}, {'date': '1995-06-01', 'max': '30+Jun+1995', 'min': '01+Jan+1990'}, {'date': '1995-07-01', 'max': '31+Jul+1995', 'min': '01+Jan+1990'}, {'date': '1995-08-01', 'max': '31+Aug+1995', 'min': '01+Jan+1990'}, {'date': '1995-09-01', 'max': '30+Sep+1995', 'min': '01+Jan+1990'}, {'date': '1995-10-01', 'max': '31+Oct+1995', 'min': '01+Jan+1990'}, {'date': '1995-11-01', 'max': '30+Nov+1995', 'min': '01+Jan+1990'}, {'date': '1995-12-01', 'max': '31+Dec+1995', 'min': '01+Jan+1990'}, {'date': '1996-01-01', 'max': '31+Jan+1996', 'min': '01+Jan+1990'}, {'date': '1996-02-01', 'max': '28+Feb+1996', 'min': '01+Jan+1990'}, {'date': '1996-03-01', 'max': '31+Mar+1996', 'min': '01+Jan+1990'}, {'date': '1996-04-01', 'max': '30+Apr+1996', 'min': '01+Jan+1990'}, {'date': '1996-05-01', 'max': '31+May+1996', 'min': '01+Jan+1990'}, {'date': '1996-06-01', 'max': '30+Jun+1996', 'min': '01+Jan+1990'}, {'date': '1996-07-01', 'max': '31+Jul+1996', 'min': '01+Jan+1990'}, {'date': '1996-08-01', 'max': '31+Aug+1996', 'min': '01+Jan+1990'}, {'date': '1996-09-01', 'max': '30+Sep+1996', 'min': '01+Jan+1990'}, {'date': '1996-10-01', 'max': '31+Oct+1996', 'min': '01+Jan+1990'}, {'date': '1996-11-01', 'max': '30+Nov+1996', 'min': '01+Jan+1990'}, {'date': '1996-12-01', 'max': '31+Dec+1996', 'min': '01+Jan+1990'}, {'date': '1997-01-01', 'max': '31+Jan+1997', 'min': '01+Jan+1990'}, {'date': '1997-02-01', 'max': '28+Feb+1997', 'min': '01+Jan+1990'}, {'date': '1997-03-01', 'max': '31+Mar+1997', 'min': '01+Jan+1990'}, {'date': '1997-04-01', 'max': '30+Apr+1997', 'min': '01+Jan+1990'}, {'date': '1997-05-01', 'max': '31+May+1997', 'min': '01+Jan+1990'}, {'date': '1997-06-01', 'max': '30+Jun+1997', 'min': '01+Jan+1990'}, {'date': '1997-07-01', 'max': '31+Jul+1997', 'min': '01+Jan+1990'}, {'date': '1997-08-01', 'max': '31+Aug+1997', 'min': '01+Jan+1990'}, {'date': '1997-09-01', 'max': '30+Sep+1997', 'min': '01+Jan+1990'}, {'date': '1997-10-01', 'max': '31+Oct+1997', 'min': '01+Jan+1990'}, {'date': '1997-11-01', 'max': '30+Nov+1997', 'min': '01+Jan+1990'}, {'date': '1997-12-01', 'max': '31+Dec+1997', 'min': '01+Jan+1990'}, {'date': '1998-01-01', 'max': '31+Jan+1998', 'min': '01+Jan+1990'}, {'date': '1998-02-01', 'max': '28+Feb+1998', 'min': '01+Jan+1990'}, {'date': '1998-03-01', 'max': '31+Mar+1998', 'min': '01+Jan+1990'}, {'date': '1998-04-01', 'max': '30+Apr+1998', 'min': '01+Jan+1990'}, {'date': '1998-05-01', 'max': '31+May+1998', 'min': '01+Jan+1990'}, {'date': '1998-06-01', 'max': '30+Jun+1998', 'min': '01+Jan+1990'}, {'date': '1998-07-01', 'max': '31+Jul+1998', 'min': '01+Jan+1990'}, {'date': '1998-08-01', 'max': '31+Aug+1998', 'min': '01+Jan+1990'}, {'date': '1998-09-01', 'max': '30+Sep+1998', 'min': '01+Jan+1990'}, {'date': '1998-10-01', 'max': '31+Oct+1998', 'min': '01+Jan+1990'}, {'date': '1998-11-01', 'max': '30+Nov+1998', 'min': '01+Jan+1990'}, {'date': '1998-12-01', 'max': '31+Dec+1998', 'min': '01+Jan+1990'}, {'date': '1999-01-01', 'max': '31+Jan+1999', 'min': '01+Jan+1990'}, {'date': '1999-02-01', 'max': '28+Feb+1999', 'min': '01+Jan+1990'}, {'date': '1999-03-01', 'max': '31+Mar+1999', 'min': '01+Jan+1990'}, {'date': '1999-04-01', 'max': '30+Apr+1999', 'min': '01+Jan+1990'}, {'date': '1999-05-01', 'max': '31+May+1999', 'min': '01+Jan+1990'}, {'date': '1999-06-01', 'max': '30+Jun+1999', 'min': '01+Jan+1990'}, {'date': '1999-07-01', 'max': '31+Jul+1999', 'min': '01+Jan+1990'}, {'date': '1999-08-01', 'max': '31+Aug+1999', 'min': '01+Jan+1990'}, {'date': '1999-09-01', 'max': '30+Sep+1999', 'min': '01+Jan+1990'}, {'date': '1999-10-01', 'max': '31+Oct+1999', 'min': '01+Jan+1990'}, {'date': '1999-11-01', 'max': '30+Nov+1999', 'min': '01+Jan+1990'}, {'date': '1999-12-01', 'max': '31+Dec+1999', 'min': '01+Jan+1990'}]
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
        runs_column = "5"
        column_name = htmlSoup.select('#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > thead > tr > th:nth-child(2) > a')[0].text
        player_name_in_table = htmlSoup.select('#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > tbody > tr:nth-child(' + rank_as_string + ') > td:nth-child(1)')[0].text
        player_country = player_name_in_table[player_name_in_table.find('(')+1:player_name_in_table.find(')')]

        if ("Span" in column_name):
            runs_column = "6"

        player_name = htmlSoup.select(
            "#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > tbody > tr:nth-child("
            + rank_as_string
            + ") > td.left > a")[0].text
        runs = htmlSoup.select(
            "#ciHomeContentlhs > div.pnl650M > table:nth-child(5) > tbody > tr:nth-child("
            + rank_as_string
            + ") > td:nth-child(" + runs_column + ") > b")[0].text
        players.append({
            FIELD_1: month['date'],
            FIELD_2: player_name,
            FIELD_3: player_country,
            FIELD_4: runs
        })

    print("End processing: " + month['max'])

# Export data to CSV
with open(CSV_WRITE_PATH, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
    writer.writeheader()

    for player in players:
        writer.writerow(player)
