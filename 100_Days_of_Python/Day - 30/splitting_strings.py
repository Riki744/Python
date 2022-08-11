authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
print(author_names)

author_last_names = []
for i in author_names:
  last_name = i.split()
  author_last_names.append(last_name[-1])
print(author_last_names)
