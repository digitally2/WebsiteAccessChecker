import urllib


list_of_websites_ext = ["http://www.google.com", "https://www.google.com"]
list_of_websites_int = ["http://www.google.com", "https://www.google.com"]



def external():
   for website in list_of_websites_ext:
      returned_code = urllib.urlopen(website).getcode()
      if returned_code == 200:
         print "GOOD |  %s" % (website)
      else:
         print "FAIL | %s" % (website)
         

def internal():
   for website in list_of_websites_int:
      returned_code = urllib.urlopen(website).getcode()
      if returned_code == 200:
         print "GOOD |  %s" % (website)
      else:
         print "FAIL | %s" % (website)



def main():
   option = raw_input("\n1 - Test Internal Websites\n2 - Test External Websites\n>")

   if option == "1":
      print "you selected 1"
      internal()

   if option == "2":
      print "you selected 2"
      external()


main()

