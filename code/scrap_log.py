import re
import pandas as pd


captured_records = []


class captured_record:
        def __init__(self, url, repeat_count):
            self.url = url
            self.repeat_count = repeat_count

        def print_record(self):
            print("Record content")
            print(self.url)
            print(self.repeat_count)


def load_snort_result(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    repeat_counter = 0
    host_tmp = ''

    for line in lines:
        line = line.rstrip()
        if(re.search("HTTP URI", line)):
            url_tmp = line.split("HTTP URI: ")[1]

        if(re.search("HTTP Hostname", line)):
            tmp = line.split("HTTP Hostname: ")[1]
            if(host_tmp == tmp):
                repeat_counter = repeat_counter + 1
            else:
                host_tmp = tmp
                repeat_counter = 1

            captured_records.append(captured_record(url_tmp, repeat_counter))


load_snort_result("log_result.txt")

captured_records_columns = ["full_url", "repeat_count"]
captured_records_df = pd.DataFrame(columns=captured_records_columns)

for record in captured_records:
    row = pd.DataFrame([[record.url, record.repeat_count]], columns=captured_records_columns)
    captured_records_df = pd.concat([captured_records_df, row], ignore_index=True)

print(captured_records_df)

captured_records_df.to_csv('pandas_df.csv', index=False)