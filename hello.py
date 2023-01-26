#!/usr/bin/env python3

import os
import json

print("Content-Type: application/json") # application/json also
print()
print(json.dumps(dict(os.environ)))
#print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")