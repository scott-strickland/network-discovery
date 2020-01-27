import pandas as pd
import csv
import utils


import_file = 'hosts.csv'
hosts = []

def ios_hosts(host, device_type,  *commands):
    timestamp = utils.timestamp()
    output_file = f"output/{timestamp}-{host.strip()}.xlsx"
    with pd.ExcelWriter(output_file) as writer:
        for command in commands:
            df = pd.DataFrame(utils.ios_connection(host, device_type, command))
            df.to_excel(writer, sheet_name=utils.sheet(command), index=False)


with open(import_file) as f:
    rows = csv.reader(f)
    header_row = next(rows)
    for row in rows:
        host, device_type = row[0], row[1]
        if row[1] == 'cisco_ios':
            ios_hosts(host, device_type, 'show cdp neighbor detail')
        elif row[1] == 'cisco_nxos':
            ios_hosts(host, device_type, 'show cdp neighbor detail')