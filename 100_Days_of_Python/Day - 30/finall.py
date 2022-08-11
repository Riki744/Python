highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
#print(highlighted_poems_list)

highlighted_poems_stripped = []
for title in highlighted_poems_list:
  strip_title = title.strip()
  highlighted_poems_stripped.append(strip_title)

#print(highlighted_poems_stripped)

highlighted_poems_details = []
for line in highlighted_poems_stripped:
  new_list = line.split(':')
  highlighted_poems_details.append(new_list)

#print(highlighted_poems_details)
titles = []
poets = []
dates = []


for new in highlighted_poems_details:
  titles.append(new[0])
  poets.append(new[1])
  dates.append(new[2])

#print(titles)
#print(poets)
#print(dates)

#for loop in multiple lists require zip()
# - https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/

for (t,p,d) in zip(titles, poets, dates):
  msg = "The poem {} was published by {} in {}.".format(t, p, d)
  print(msg)
