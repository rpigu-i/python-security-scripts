# Chapter 4 coding projects

Upgraded to work with Python 3.x

Install scapy with pip3

```
pip3 install scapy

```

## mail_sniffer_one_packet.py

Uses scapy to sniff a single packet
and dump the details to the console

## mail_sniffer.py

Sniffs traffic to POP3 (110), IMAP (143) and SMTP (25)


## arper.py

ARP poisoning script. Produces a PCACP dump.

Start by allowing forwarding e.g.

Mac:
```
sudo sysctl -w net.inet.ip.forwarding=1
```

'Nix:

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

##  pic_carver.py

For cv2

```
pip3 install opencv-python
```

Facial detection training file:

```
curl https://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml -o haarcascade_frontalface_alt.xml
```

