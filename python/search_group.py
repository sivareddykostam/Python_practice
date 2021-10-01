#------------------------------------------------------------------------
#Description : Match groups
#Used to search for partictular pattern
#------------------------------------------------------------------------
import re

match = re.search('(39801 356 222 101)','39801356222101' );
print("Match Group Index 1 position "+match.group(1));
#print("Match Group Index 2 position "+match.group(2));
print(match.groups());
print(match.span());
print(match.start());
print(match.end());
