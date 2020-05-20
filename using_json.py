#!/usr/bin/env python3
import json

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-231-662",
            "cell": "21-152-987"
        },
        "department": "IT Infrastructure",
        "role": "System Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
           "office": "951-753645"
         },
         "department": "IT Infrastructure",
         "role": "IT Specialist"

    }

]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json)
