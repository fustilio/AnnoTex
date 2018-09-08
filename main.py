import sys
import json
import pdfannots

if len(sys.argv) > 1:
	filename = sys.argv[1]

# Call Francis script and get json
#"python pdfannots/pdfannots.py #{filename}"
data = json.loads(pdfannots.main(filename))
# Process json
#json_string = raw_input()
#data = json.loads(json_string)
#print(data[0])


# Send json to Wayne to generate tex