nmap -sP 192.168.1.0/24 | grep -B1 "Host is up" | grep -v "Host is up" | grep -v "\-\-" | awk -F "(" '{print $2}' | sed -e "s/)//g"
