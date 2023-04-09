import re
import pandas as pd


captured_records = []


class captured_record:
        def __init__(self, url, event_time, hostname):
            self.url = url
            self.event_time = event_time
            self.hostname = hostname

        def print_record(self):
            print("Record content")
            print(self.url)
            print(self.event_time)
            print(self.hostname)


def load_snort_result(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip()

        if(re.search("event second", line) and re.search("event microsecond", line) ):
            event_seconds, event_microseconds = line.split("event second: ")[1].split("	event microsecond: ")
            event_time_tmp = float(event_seconds) + float(event_microseconds) * pow(10, -6)

        if(re.search("HTTP URI", line)):
            url_tmp = line.split("HTTP URI: ")[1]

        if(re.search("HTTP Hostname", line)):
            hostname_tmp = line.split("HTTP Hostname: ")[1]
            captured_records.append(captured_record(url_tmp, event_time_tmp, hostname_tmp))


load_snort_result("log_result.txt")

captured_records_columns = ["full_url", "event_time", "hostname"]
captured_records_df = pd.DataFrame(columns=captured_records_columns)

for record in captured_records:
    row = pd.DataFrame([[record.url, record.event_time, record.hostname]], columns=captured_records_columns)
    captured_records_df = pd.concat([captured_records_df, row], ignore_index=True)

print(captured_records_df)

captured_records_df.to_csv('pandas_df.csv', index=False)