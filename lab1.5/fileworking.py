#!/usr/bin/python3

import glob

list_files = glob.glob("config_files/*.txt")

print(list_files)

ip_list =[]
result_list = []

for test_files in list_files:
    with open(test_files) as text_file:
        for string_in_file in text_file:
            if string_in_file.find('ip address') > 0:
                ip_list.append(string_in_file)
ip_list = list(set(ip_list))
for i in ip_list:
    i = i.replace('ip address', ' ')
    i = i.strip()
    result_list.append(i)

for pr in result_list:
    print(pr)

#if re.match('^([0-9{1,3}]\.?){4}$')