#Top 10 districts with maximum identities generated from both male and female.

#!/usr/bin/python

import sys
from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + "\t" + str(self.user_id)


users = []

try:
   for line in sys.stdin:
    data = line.strip().split('\t')
    users.append(User(data[0],int(data[-1])))
except ValueError:
   pass

for user in sorted(users, key=attrgetter('user_id'), reverse=True)[:10]:
    print(user)



