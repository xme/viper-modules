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
```viper sample.exe > a1000 -s
[*] Successfully submitted file to A1000, task ID: 393846
viper sample.exe > a1000 -c
[*] DEBUG: ec78ea5bd0e33ae40e53a02f972221bc66399a89 200
[*] Classification
 - Threat statusi : malicious
 - Threat name   : Win32.Trojan.Fareit dw eldorado
 - Trust factor  : 5
 - Threat level  : 2
 - First seen    : 2018-02-09T13:03:26Z
 - Last seen     : 2018-02-09T13:07:00Z
 ```
 
