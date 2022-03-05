# elasticsearch-flooder

A lot of people don't secure by password their elasticsearch servers, and elasticsearch system doesn't have flood protection. Therefore, you can carry out such mini-attacks

This is a script that can create many indexes, thereby clogging the server. All you need is to dump open servers in ip:port format from shodan. By the way, you can do it in the program

![photo](https://i.imgur.com/9pq6EIN.png)

# Usage
```
All arguments:
--shodan_key - set your shodan key
--shodan_dump - dump open servers with shodan


Main usage:
ex of usage: python main.py servers.txt result.txt 25

servers.txt - file where list of servers located(ip:port format)
result.txt - file, where script will write already flooded servers
25 - number of indexes per 1 cycle
```

###### Subscribe pls

https://t.me/termuxqew!
