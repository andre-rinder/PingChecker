# Pingchecker

Pingchecker is a Python Script which takes a list of hostnames, pings the hosts and writes the results in a .csv file. 

I use it in combination with a PowerShell script. The powershell scripts gets the hostlist.txt from the Active Directory. So I can see, which computers might not be in use anymore. 

### Example

hostlist.txt 
google.com
klsadflkasd

results.csv
google.com, True
klsadflkasd, False

### Prerequisites

Tested in Python 3.6