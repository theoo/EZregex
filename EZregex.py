#Name: Search and Replace
#Info: Apply the regular expression of your dream to your GCode. https://en.wikipedia.org/wiki/Regular_expression
#Depend: GCode
#Type: postprocess
#Param: searchString1(string:^T0$) search 1
#Param: replaceString1(string:T0\nM340 S5.4) replace 1
#Param: searchString2(string:^T1$) search 2
#Param: replaceString2(string:T1\nM340 S8.6) replace 2
#Param: searchString3(string:) search 3
#Param: replaceString3(string:) replace 3
#Param: searchString4(string:) search 4
#Param: replaceString4(string:) replace 4
#Param: searchString5(string:) search 5
#Param: replaceString5(string:) replace 5

__copyright__ = "Copyright (C) 2016 Theo Reichel - Released under terms of the AGPLv3 License"
import re
from Cura.util import profile

searchStrings = [searchString1, searchString2, searchString3, searchString4, searchString5]
replaceStrings = [replaceString1, replaceString2, replaceString3, replaceString4, replaceString5]

with open(filename, "r") as f:
	lines = f.readlines()
	f.close()

with open(filename, "w") as f:
	for lIndex in xrange(len(lines)):
		line = lines[lIndex]
		for i in range(5):
			if searchStrings[i] != None and replaceStrings[i] != None:
				line = re.sub(searchStrings[i], replaceStrings[i], line)
		f.write(line)

	f.close()
