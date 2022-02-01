import sys, time, requests

def downloadFile(url, name) :
    with open(name, 'wb') as f:
        start = time.perf_counter()
        r = requests.get(url, allow_redirects=True, stream=True)
        total_length = r.headers.get('content-length')
        dl = 0
        if total_length is None: # no content length header
            f.write(r.content)
        else:
            for chunk in r.iter_content(1024):
                dl += len(chunk)
                f.write(chunk)
                done = int(50 * dl / int(total_length))
                sys.stdout.write("\r[%s%s] %s bps" % ('=' * done, ' ' * (50-done), dl//(time.perf_counter() - start)))
                print('')
    return (time.perf_counter() - start)

time_elapsed = 0
day, month, year = 6, 12, 2008
while True:
    if month == 13:
        month = 1
        year += 1
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day == 32:
            day = 1
            month += 1
    if month in [4, 6, 9, 11]:
        if day == 31:
            day = 1
            month +=1
    if month == 2:
        if day == 30:
            day = 1
            month +=1
    if year == 2021 and month == 6 and day == 29:
        break
    syear = str(year)
    if day < 10:
        sday = "0" + str(day)
    else:
        sday = str(day)
    if month < 10:
        smonth = "0" + str(month)
    else:
        smonth = str(month)
    url = "http://www.tsetmc.com/tse/data/Export-xls.aspx?a=TradeOneDay&Date=" + syear + smonth + sday
    name = "/Users/omid/Desktop/Stock Data/" + syear + smonth + sday + ".xls"
    try:
        time_elapsed += downloadFile(url, name)
    except:
        continue
    day += 1

#http://www.tsetmc.com/tse/data/Export-xls.aspx?a=TradeOneDay&Date=20081206
        
print("Download complete...")
print("Time Elapsed: " + str(time_elapsed / 60))