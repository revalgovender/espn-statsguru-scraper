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
months = [{'date': '2010-01-01', 'max': '31+Jan+2010', 'min': '01+Jan+2010'}, {'date': '2010-02-01', 'max': '28+Feb+2010', 'min': '01+Jan+2010'}, {'date': '2010-03-01', 'max': '31+Mar+2010', 'min': '01+Jan+2010'}, {'date': '2010-04-01', 'max': '30+Apr+2010', 'min': '01+Jan+2010'}, {'date': '2010-05-01', 'max': '31+May+2010', 'min': '01+Jan+2010'}, {'date': '2010-06-01', 'max': '30+Jun+2010', 'min': '01+Jan+2010'}, {'date': '2010-07-01', 'max': '31+Jul+2010', 'min': '01+Jan+2010'}, {'date': '2010-08-01', 'max': '31+Aug+2010', 'min': '01+Jan+2010'}, {'date': '2010-09-01', 'max': '30+Sep+2010', 'min': '01+Jan+2010'}, {'date': '2010-10-01', 'max': '31+Oct+2010', 'min': '01+Jan+2010'}, {'date': '2010-11-01', 'max': '30+Nov+2010', 'min': '01+Jan+2010'}, {'date': '2010-12-01', 'max': '31+Dec+2010', 'min': '01+Jan+2010'}, {'date': '2011-01-01', 'max': '31+Jan+2011', 'min': '01+Jan+2010'}, {'date': '2011-02-01', 'max': '28+Feb+2011', 'min': '01+Jan+2010'}, {'date': '2011-03-01', 'max': '31+Mar+2011', 'min': '01+Jan+2010'}, {'date': '2011-04-01', 'max': '30+Apr+2011', 'min': '01+Jan+2010'}, {'date': '2011-05-01', 'max': '31+May+2011', 'min': '01+Jan+2010'}, {'date': '2011-06-01', 'max': '30+Jun+2011', 'min': '01+Jan+2010'}, {'date': '2011-07-01', 'max': '31+Jul+2011', 'min': '01+Jan+2010'}, {'date': '2011-08-01', 'max': '31+Aug+2011', 'min': '01+Jan+2010'}, {'date': '2011-09-01', 'max': '30+Sep+2011', 'min': '01+Jan+2010'}, {'date': '2011-10-01', 'max': '31+Oct+2011', 'min': '01+Jan+2010'}, {'date': '2011-11-01', 'max': '30+Nov+2011', 'min': '01+Jan+2010'}, {'date': '2011-12-01', 'max': '31+Dec+2011', 'min': '01+Jan+2010'}, {'date': '2012-01-01', 'max': '31+Jan+2012', 'min': '01+Jan+2010'}, {'date': '2012-02-01', 'max': '28+Feb+2012', 'min': '01+Jan+2010'}, {'date': '2012-03-01', 'max': '31+Mar+2012', 'min': '01+Jan+2010'}, {'date': '2012-04-01', 'max': '30+Apr+2012', 'min': '01+Jan+2010'}, {'date': '2012-05-01', 'max': '31+May+2012', 'min': '01+Jan+2010'}, {'date': '2012-06-01', 'max': '30+Jun+2012', 'min': '01+Jan+2010'}, {'date': '2012-07-01', 'max': '31+Jul+2012', 'min': '01+Jan+2010'}, {'date': '2012-08-01', 'max': '31+Aug+2012', 'min': '01+Jan+2010'}, {'date': '2012-09-01', 'max': '30+Sep+2012', 'min': '01+Jan+2010'}, {'date': '2012-10-01', 'max': '31+Oct+2012', 'min': '01+Jan+2010'}, {'date': '2012-11-01', 'max': '30+Nov+2012', 'min': '01+Jan+2010'}, {'date': '2012-12-01', 'max': '31+Dec+2012', 'min': '01+Jan+2010'}, {'date': '2013-01-01', 'max': '31+Jan+2013', 'min': '01+Jan+2010'}, {'date': '2013-02-01', 'max': '28+Feb+2013', 'min': '01+Jan+2010'}, {'date': '2013-03-01', 'max': '31+Mar+2013', 'min': '01+Jan+2010'}, {'date': '2013-04-01', 'max': '30+Apr+2013', 'min': '01+Jan+2010'}, {'date': '2013-05-01', 'max': '31+May+2013', 'min': '01+Jan+2010'}, {'date': '2013-06-01', 'max': '30+Jun+2013', 'min': '01+Jan+2010'}, {'date': '2013-07-01', 'max': '31+Jul+2013', 'min': '01+Jan+2010'}, {'date': '2013-08-01', 'max': '31+Aug+2013', 'min': '01+Jan+2010'}, {'date': '2013-09-01', 'max': '30+Sep+2013', 'min': '01+Jan+2010'}, {'date': '2013-10-01', 'max': '31+Oct+2013', 'min': '01+Jan+2010'}, {'date': '2013-11-01', 'max': '30+Nov+2013', 'min': '01+Jan+2010'}, {'date': '2013-12-01', 'max': '31+Dec+2013', 'min': '01+Jan+2010'}, {'date': '2014-01-01', 'max': '31+Jan+2014', 'min': '01+Jan+2010'}, {'date': '2014-02-01', 'max': '28+Feb+2014', 'min': '01+Jan+2010'}, {'date': '2014-03-01', 'max': '31+Mar+2014', 'min': '01+Jan+2010'}, {'date': '2014-04-01', 'max': '30+Apr+2014', 'min': '01+Jan+2010'}, {'date': '2014-05-01', 'max': '31+May+2014', 'min': '01+Jan+2010'}, {'date': '2014-06-01', 'max': '30+Jun+2014', 'min': '01+Jan+2010'}, {'date': '2014-07-01', 'max': '31+Jul+2014', 'min': '01+Jan+2010'}, {'date': '2014-08-01', 'max': '31+Aug+2014', 'min': '01+Jan+2010'}, {'date': '2014-09-01', 'max': '30+Sep+2014', 'min': '01+Jan+2010'}, {'date': '2014-10-01', 'max': '31+Oct+2014', 'min': '01+Jan+2010'}, {'date': '2014-11-01', 'max': '30+Nov+2014', 'min': '01+Jan+2010'}, {'date': '2014-12-01', 'max': '31+Dec+2014', 'min': '01+Jan+2010'}, {'date': '2015-01-01', 'max': '31+Jan+2015', 'min': '01+Jan+2010'}, {'date': '2015-02-01', 'max': '28+Feb+2015', 'min': '01+Jan+2010'}, {'date': '2015-03-01', 'max': '31+Mar+2015', 'min': '01+Jan+2010'}, {'date': '2015-04-01', 'max': '30+Apr+2015', 'min': '01+Jan+2010'}, {'date': '2015-05-01', 'max': '31+May+2015', 'min': '01+Jan+2010'}, {'date': '2015-06-01', 'max': '30+Jun+2015', 'min': '01+Jan+2010'}, {'date': '2015-07-01', 'max': '31+Jul+2015', 'min': '01+Jan+2010'}, {'date': '2015-08-01', 'max': '31+Aug+2015', 'min': '01+Jan+2010'}, {'date': '2015-09-01', 'max': '30+Sep+2015', 'min': '01+Jan+2010'}, {'date': '2015-10-01', 'max': '31+Oct+2015', 'min': '01+Jan+2010'}, {'date': '2015-11-01', 'max': '30+Nov+2015', 'min': '01+Jan+2010'}, {'date': '2015-12-01', 'max': '31+Dec+2015', 'min': '01+Jan+2010'}, {'date': '2016-01-01', 'max': '31+Jan+2016', 'min': '01+Jan+2010'}, {'date': '2016-02-01', 'max': '28+Feb+2016', 'min': '01+Jan+2010'}, {'date': '2016-03-01', 'max': '31+Mar+2016', 'min': '01+Jan+2010'}, {'date': '2016-04-01', 'max': '30+Apr+2016', 'min': '01+Jan+2010'}, {'date': '2016-05-01', 'max': '31+May+2016', 'min': '01+Jan+2010'}, {'date': '2016-06-01', 'max': '30+Jun+2016', 'min': '01+Jan+2010'}, {'date': '2016-07-01', 'max': '31+Jul+2016', 'min': '01+Jan+2010'}, {'date': '2016-08-01', 'max': '31+Aug+2016', 'min': '01+Jan+2010'}, {'date': '2016-09-01', 'max': '30+Sep+2016', 'min': '01+Jan+2010'}, {'date': '2016-10-01', 'max': '31+Oct+2016', 'min': '01+Jan+2010'}, {'date': '2016-11-01', 'max': '30+Nov+2016', 'min': '01+Jan+2010'}, {'date': '2016-12-01', 'max': '31+Dec+2016', 'min': '01+Jan+2010'}, {'date': '2017-01-01', 'max': '31+Jan+2017', 'min': '01+Jan+2010'}, {'date': '2017-02-01', 'max': '28+Feb+2017', 'min': '01+Jan+2010'}, {'date': '2017-03-01', 'max': '31+Mar+2017', 'min': '01+Jan+2010'}, {'date': '2017-04-01', 'max': '30+Apr+2017', 'min': '01+Jan+2010'}, {'date': '2017-05-01', 'max': '31+May+2017', 'min': '01+Jan+2010'}, {'date': '2017-06-01', 'max': '30+Jun+2017', 'min': '01+Jan+2010'}, {'date': '2017-07-01', 'max': '31+Jul+2017', 'min': '01+Jan+2010'}, {'date': '2017-08-01', 'max': '31+Aug+2017', 'min': '01+Jan+2010'}, {'date': '2017-09-01', 'max': '30+Sep+2017', 'min': '01+Jan+2010'}, {'date': '2017-10-01', 'max': '31+Oct+2017', 'min': '01+Jan+2010'}, {'date': '2017-11-01', 'max': '30+Nov+2017', 'min': '01+Jan+2010'}, {'date': '2017-12-01', 'max': '31+Dec+2017', 'min': '01+Jan+2010'}, {'date': '2018-01-01', 'max': '31+Jan+2018', 'min': '01+Jan+2010'}, {'date': '2018-02-01', 'max': '28+Feb+2018', 'min': '01+Jan+2010'}, {'date': '2018-03-01', 'max': '31+Mar+2018', 'min': '01+Jan+2010'}, {'date': '2018-04-01', 'max': '30+Apr+2018', 'min': '01+Jan+2010'}, {'date': '2018-05-01', 'max': '31+May+2018', 'min': '01+Jan+2010'}, {'date': '2018-06-01', 'max': '30+Jun+2018', 'min': '01+Jan+2010'}, {'date': '2018-07-01', 'max': '31+Jul+2018', 'min': '01+Jan+2010'}, {'date': '2018-08-01', 'max': '31+Aug+2018', 'min': '01+Jan+2010'}, {'date': '2018-09-01', 'max': '30+Sep+2018', 'min': '01+Jan+2010'}, {'date': '2018-10-01', 'max': '31+Oct+2018', 'min': '01+Jan+2010'}, {'date': '2018-11-01', 'max': '30+Nov+2018', 'min': '01+Jan+2010'}, {'date': '2018-12-01', 'max': '31+Dec+2018', 'min': '01+Jan+2010'}, {'date': '2019-01-01', 'max': '31+Jan+2019', 'min': '01+Jan+2010'}, {'date': '2019-02-01', 'max': '28+Feb+2019', 'min': '01+Jan+2010'}, {'date': '2019-03-01', 'max': '31+Mar+2019', 'min': '01+Jan+2010'}, {'date': '2019-04-01', 'max': '30+Apr+2019', 'min': '01+Jan+2010'}, {'date': '2019-05-01', 'max': '31+May+2019', 'min': '01+Jan+2010'}, {'date': '2019-06-01', 'max': '30+Jun+2019', 'min': '01+Jan+2010'}, {'date': '2019-07-01', 'max': '31+Jul+2019', 'min': '01+Jan+2010'}, {'date': '2019-08-01', 'max': '31+Aug+2019', 'min': '01+Jan+2010'}, {'date': '2019-09-01', 'max': '30+Sep+2019', 'min': '01+Jan+2010'}, {'date': '2019-10-01', 'max': '31+Oct+2019', 'min': '01+Jan+2010'}, {'date': '2019-11-01', 'max': '30+Nov+2019', 'min': '01+Jan+2010'}, {'date': '2019-12-01', 'max': '31+Dec+2019', 'min': '01+Jan+2010'}]
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
