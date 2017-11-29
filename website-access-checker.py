import urllib
import csv

list_of_websites = []



#UPDATE LISTS
def update_lists():
   with open("website-list.tsv", "rU") as csvfile:
      reader = csv.reader(csvfile, dialect='excel-tab')
      for row in reader:
         list_of_websites.append(row[0])
update_lists()


def test_websites_from_list():
   for website in list_of_websites:
      returned_code = urllib.urlopen(website).getcode()
      if returned_code == 200:
         print "GOOD |  %s" % (website)
      else:
         print "FAIL | %s" % (website)
         

def print_list_of_websites():
   for website in list_of_websites:
      print website


def main():
   option = raw_input("\n1 - Test list of websites\n2 - Print list of websites\n>")

   if option == "1":
      print "you selected 1"
      test_websites_from_list()

   if option == "2":
      print "you selected 2"
      print_list_of_websites()


main()

