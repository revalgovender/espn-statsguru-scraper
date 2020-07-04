start_of_range_date_espn_format = "01+Jan+1990"
month_formats = [
    {"month_as_espn_format": "31+Jan+", "month_as_standard_date": "-01-01"},
    {"month_as_espn_format": "28+Feb+", "month_as_standard_date": "-02-01"},
    {"month_as_espn_format": "31+Mar+", "month_as_standard_date": "-03-01"},
    {"month_as_espn_format": "30+Apr+", "month_as_standard_date": "-04-01"},
    {"month_as_espn_format": "31+May+", "month_as_standard_date": "-05-01"},
    {"month_as_espn_format": "30+Jun+", "month_as_standard_date": "-06-01"},
    {"month_as_espn_format": "31+Jul+", "month_as_standard_date": "-07-01"},
    {"month_as_espn_format": "31+Aug+", "month_as_standard_date": "-08-01"},
    {"month_as_espn_format": "30+Sep+", "month_as_standard_date": "-09-01"},
    {"month_as_espn_format": "31+Oct+", "month_as_standard_date": "-10-01"},
    {"month_as_espn_format": "30+Nov+", "month_as_standard_date": "-11-01"},
    {"month_as_espn_format": "31+Dec+", "month_as_standard_date": "-12-01"},
]
months = []

for year in range(1990, 2000):
    year_as_string = str(year)

    for month_format in month_formats:
        months.append({
            "date": year_as_string + month_format['month_as_standard_date'],
            "max": month_format['month_as_espn_format'] + year_as_string,
            "min": start_of_range_date_espn_format,
        })

print(months)