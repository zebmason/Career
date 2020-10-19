import sys, markdown
import datetime

tags = sys.argv[1:]
print("using tags: ", tags)

body = open("body.md", "r")
lines = body.readlines()
body.close()

alltags = set()

assembled = ""
for line in lines:
  line = line.rstrip()
  if line[-1:] == "}":
    index = line.rfind("{")
    options = line[index:]
    line = line[:index]
    options = options[1:-1].split()
    for tag in options:
      alltags.add(tag)
    for tag in options:
      if tag in tags or "everything" in tags:
        assembled += line + "\n"
        break
  else:
    assembled += line + "\n"
    
assembled = markdown.markdown(assembled)
assembled = assembled.replace("<h2>", "\n<h2>")

template = open("template.html", "r")
temp = template.read()
template.close()

assembled = temp.replace("[[body]]", assembled)

fileName = "tailored"
if "everything" in tags:
  fileName = "everything"

date = str(datetime.datetime.now()).split()[0].replace("-", "")
assembled = assembled.replace("[[date]]", date)
fileName += date + ".html"

omitted = set()
for tag in alltags:
  if not tag in tags:
    omitted.add(tag)

keys = ""
if "everything" in tags:
  keys = ", ".join(sorted(alltags))
else:
  keys = ", ".join(sorted(tags))
assembled = assembled.replace("[[used]]", keys)

if "everything" in tags:
  keys = "[none]"
else:
  keys = ", ".join(sorted(omitted))
assembled = assembled.replace("[[omitted]]", keys)

output = open(fileName, "w")
output.write(assembled)
output.close()

print("omitted tags: ", sorted(omitted))
print("available tags: ", sorted(alltags))