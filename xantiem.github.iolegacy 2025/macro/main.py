with open("econ_concepts.csv") as fp:
    lines = fp.readlines()[2:]

with open("macro.html", "w") as dat:
    dat.write("<h1>Macro terminology</h1>")

    for line in lines:
        data = line.strip("\n").split(";")
        dat.write("<p><b style=\"color: blue;\">{}</b>: {}</p>".format(data[0], data[1]))
        dat.write("<br /><a href="econ_concepts.csv">Download as .CSV</a>")

    
