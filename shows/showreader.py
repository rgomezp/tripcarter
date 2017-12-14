import csv

output = open('output.txt','w')

with open('shows.csv', 'rb') as csvfile:
  showreader = csv.reader(csvfile.read().splitlines(), delimiter=',')
  for row in showreader:
      #date
      output.write("<tr>\n\t<td style=\"float:left;\">"+row[0]+"</td>\n")
      #city
      output.write("\t<td>"+row[1]+"</td>\n")
      #url
      output.write("\t<td style = \"float: right; margin-right: 10px;\"><a href=\""+row[2]+" style = \"display: inline; border-style: solid; border-width: 2px; width: 100%; margin-left: 15px; color: white; padding:6px; padding-left: 20px; padding-right: 20px;\">Tickets</a></td>\n</tr>")
