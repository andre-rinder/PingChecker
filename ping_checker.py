import os
from csv import DictWriter


def ping_checker(hostlist):
    """ Takes a list of strings of hostnames [hostname1, hostname2] and gives back a list of dicts which contains ping results {"Hostname" : "host1, "Pingresult": True}"""
    responses = []
    for host in hostlist:
        response = (os.system("ping -n 1 " + host))
        if response == 0:
            responses.append({"Hostname": host, "Pingresult": True})
        else:
            responses.append({"Hostname": host, "Pingresult": False})
    return responses


# hostlist = ["www.google.com", "asdfmaöselkirfj"]
hostlist = []

with open("hostlist.txt", "r", encoding="UTF-8") as file:
    for line in file:
        hostlist.append(line.rstrip())

responses = ping_checker(hostlist)
with open("pingresults.csv", "w", encoding="UTF-8") as file:
    fieldnames = ["Hostname", "Pingresult"]
    writer = DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for host in responses:
        writer.writerow(host)
