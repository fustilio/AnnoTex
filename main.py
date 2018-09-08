import sys
import json
import pdfannots
import maketex

if len(sys.argv) > 1:
	filename = sys.argv[1]

# Call Francis script and get json
#"python pdfannots/pdfannots.py #{filename}"
data = json.loads(pdfannots.main(filename))
# Process json
#json_string = raw_input()
#data = json.loads(json_string)
#print(data[0])
maketex.createLatexPDF(data)

# Send json to Wayne to generate tex