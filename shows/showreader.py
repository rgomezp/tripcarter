import csv

output = open('output.html','w')

with open('shows.csv', 'rb') as csvfile:
  showreader = csv.reader(csvfile.read().splitlines(), delimiter=',')
  for row in showreader:
      date = ""
      dash = False
      for char in row[0]:
          if char == '-' or char == '/':
              dash = True
          if dash:
              date = date+"."
          else:
              date = date+char
          dash = False
      #date
      output.write("<tr>\n\t<td style=\"float:left;\">"+date+"</td>\n")
      #city
      output.write("\t<td>"+row[1]+"</td>\n")
      #url
      output.write("\t<td style = \"float: right; margin-right: 10px;\"><a href=\""+row[2]+"\" style = \"display: inline; border-style: solid; border-width: 2px; width: 100%; margin-left: 15px; color: white; padding:6px; padding-left: 20px; padding-right: 20px;\">Tickets</a></td>\n</tr>")
