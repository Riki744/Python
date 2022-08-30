user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#Since key exist, the correct value will be printed
tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)

#Since key does not exist the value will be the one we provided
stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)
