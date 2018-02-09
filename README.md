# viper-modules
Miscellaneous modules for the Viper framework

## a1000.py
Submit samples and get classification from a ReversingLabs A1000 appliance.
### Configuration
Added to your viper.conf:
```[a1000]
base_url=https://a1000_fqdn_or_ip
token=<API Token>
```
### Usage
From an open session:
```viper sample.exe > a1000 -h
usage: a1000 [-h] [-s] [-c]

Submit files and retrieve reports from a ReversingLab A1000

optional arguments:
  -h, --help            show this help message and exit
  -s, --submit          Submit file to A1000
  -c, --classification  Get classification of current file from A1000
  
viper sample.exe > a1000 -s
[*] Successfully submitted file to A1000, task ID: 393846

viper sample.exe > a1000 -c
[*] Classification
 - Threat statusi : malicious
 - Threat name   : Win32.Trojan.Fareit dw eldorado
 - Trust factor  : 5
 - Threat level  : 2
 - First seen    : 2018-02-09T13:03:26Z
 - Last seen     : 2018-02-09T13:07:00Z
 ```
 
