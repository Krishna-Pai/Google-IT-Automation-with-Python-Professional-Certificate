#Following code should be executed on Python shell

import re

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
re.search(r"ticky: INFO: ([\w ]*) ", line)

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)