import re

regex = re.compile("(?:\S+ ){6}(?P<ip>\S+) (?P<in_port>\d+) \S+ (?P<inf>\S+) (?P<out_port>\d+)")

with open('cisco_nat_config.txt') as src:
    for line in src:
        match = regex.search(line)
        print(match.groups())