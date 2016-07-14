# Continuously enable all ports one by one using snmp interface

while true
do 
   for port in {1..96}
   do
      echo "port : " $port
      snmpset -v 3 -u root -a MD5 -A rootpass -x DES -X rootpass -l noAuthNoPriv -m ALL -t 10 10.99.99.225 polatisOxcPortDesiredState.$port i 1
      sleep 1
   done
done
