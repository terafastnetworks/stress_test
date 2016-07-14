# Continuously enable all ports one by one using snmp interface

while true
do 
   for ingress_port in {1..48}
   do
      num=48
      egress_port=`expr $ingress_port + $num`
      echo "ingress port : " $ingress_port ; echo "egress port : " $egress_port
      snmpset -v 3 -u root -a MD5 -A rootpass -x DES -X rootpass -l noAuthNoPriv -m ALL -t 10 10.99.99.225 polatisOxcPortPatch.$ingress_port u $egress_port
      sleep 1
   done
done
