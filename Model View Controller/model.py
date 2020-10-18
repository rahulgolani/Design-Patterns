# It calls for a method, which fetches all the records of the Person table in database. The records are presented in JSON format.

import json
class Person:

    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def name(self):
        return f"Name is {self.firstname} {self.lastname}"

    @classmethod
    def getAll(cls):
        with open('db.txt','r') as f:
            data=f.read()
        data=json.loads(data)
        data=data['persons']
        # print(type(data))
        result=[]
        for item in data:
            # print(item)
            # print(item['first_name'],item['last_name'])
            person=Person(item['first_name'],item['last_name'])
            result.append(person)
        return result

# if __name__ == '__main__':
#     obj=Person('1','2')
#     result=obj.getAll()
