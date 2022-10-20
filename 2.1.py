now = '2022-09-18 12:41:18+03:00'
date = now.split()[0].split('-')
separator = now[-6]
time = now.split()[1].split(separator)[0].split(':')
tz = [separator] + now.split()[1].split(separator)[1].split(':')
print(date, time, tz, sep='\n')