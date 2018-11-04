import httplib
import socket
import sys


try:
    print("""
    * Mass Admin Finder
    * Modified by R Zen
    * Facebook: https://www.facebook.com/profile.php?id=100029290717684

    ######################################################################
    #    Scanning sites without the consent of their owners is illegal,  # 
    #      please use it only for legal purposes such as bug bounty      #
    ######################################################################
""")

    adm1 = 0
    adm2 = 0
    targets = []
    php = open("wordlist.txt", "r").readlines()

    try:
        f = open("sites.txt", 'r')
        targets = f.readlines()
        f.close()
        targets = [x.strip() for x in targets] 
        for target in targets:
                site = target
                site = site.replace("https://","")
                site = site.replace("http://","")
                print ("\tChecking website " + site + "...")
                conn = httplib.HTTPConnection(site)
                conn.connect()
                print ("\t[$] Yes... Server is Online.")

    except (httplib.HTTPResponse, socket.error) as Exit:
       input("\t [!] Oops Error occured, Server offline or invalid URL")
       sys.exit()

    code = input("Press 1 and Enter -- >\n")     
    if code == 1:
        for xxx in targets:
            site = xxx
            print("\t [+] Scanning " + site + "...\n\n")
    for xxx in targets:
        site = xxx
        for admin in php:
                admin = admin.replace("\n","")
                admin = "/" + admin
                host = site + admin
                connection = httplib.HTTPConnection(site)
                connection.request("GET",admin)
                response = connection.getresponse()
                adm2 = adm2 + 1
                if response.status == 200:
                    adm1 = adm1 + 1
                    print("%s %s" % ( "http://" + host, '===> Admin found'))
                    f = open("result.txt", 'a')
                    f.write("found 200 OK")
                    f.write(host)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                elif response.status == 404:
                    f = open("bad.txt", 'a')
                    f.write("404") 
                    f.write(host)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                    print("%s %s %s" % (host, "===> Not found:", response.status))
                elif response.status == 302:
                    f = open("found 302 Redirection", 'a')
                    f.write("302===>")
                    f.write(host)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                    print("%s %s" % ("http://" + host, "===> Admin found\n", response.status))
                else:
                    f = open("bad.txt", 'a')
                    f.write("301")
                    f.write(host)
                    f.write("\n")
                    f.write("\n")
                    f.close()
                    print("%s %s %s" % (host, "===> Interesting response:", response.status))
                connection.close()
 
except (httplib.HTTPResponse, socket.error):
    print("\n\t[!] Session Cancelled; Error occured. Check internet settings")
except (KeyboardInterrupt, SystemExit):
    print("\n\t[!] Session cancelled")
