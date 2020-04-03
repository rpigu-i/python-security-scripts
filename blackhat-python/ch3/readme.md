# Chapter 3

Scripts from Chapter 3 ported to Python 3

## sniffer.py

A simple packet sniffer. 

## sniffer_ip_header_decode.py

Decodes IP header while performing sniffing.
If you have issued with:

```
ValueError: Buffer size too small (20 instead of at least 32 bytes)
```

and

```
struct.error: 'L' format requires 0 <= number <= 4294967295
```

See the following Stack overflow post on changing the struct to
accomodate the packet size on a 32 versus 64 bit system:

https://stackoverflow.com/questions/29306747/python-sniffing-from-black-hat-python-book/29307402


## sniffer_with_icmp.py

Same as sniffer_ip_header_decode.py but decodes ICMP headers too.

