
import urllib2
import time
import webbrowser
import winsound
import traceback


def get_data():
    url = HOST + "/remind"
    rs = urllib2.urlopen(url).read()
    sns, urges = rs.split("+++")
    sns = eval(sns)
    urges = eval(urges)
    return sns, urges

print "=========Remind Helper v1.0==========="

HOST = "http://sm10.sinaapp.com"

print "Connected to ", HOST, "..."

sn_list, urge_list = get_data()

print "Begin"

while True:

    try:
    
        sns, urges = get_data()

        for sn in sns:
            if sn not in sn_list:
                winsound.MessageBeep(48)
                print "new order:", sn
                webbrowser.open_new_tab(HOST + "/order_search/?sn=" + sn)

        for urge in urges:
            if urge not in urge_list:
                winsound.MessageBeep(48)
                print "new urge:", urge
                webbrowser.open_new_tab(HOST + "/admin_order")


        print "Normal", time.strftime("%Y-%m-%d %H:%M:%S") 

        sn_list, urge_list = sns, urges
        
    except:
        traceback.print_exc()


    time.sleep(60)
