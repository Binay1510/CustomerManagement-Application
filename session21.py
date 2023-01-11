#from pymongo import MongoClient
import pymongo


class Customer:

    # Constructor
    def __init__(self, name=None, phone=None, email=None,age=None,gender=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender=gender

class MongoDbHelper:

    def __init__(self):

        client = pymongo.MongoClient("mongodb+srv://aubs:aubs@cluster0.rsgkt2o.mongodb.net/?retryWrites=true&w=majority")

        #print("MongoDb Connection Done")
        #from pymongo import MongoClient
        self.db = client['gw2022pd1']
        self.collections = self.db['customers']

    def insert(self,document):
        result=self.collections.insert_one(document)
        print("Inserted data:",result.inserted_id)

    def fetch(self):
        rows=[]
        documents=self.collections.find()
        print(documents,type(documents))
        for document in documents:
            print(document,type(document))
            rows.append(document)

        return rows

    def fetch_selected(self,query):
        rows = []
        documents = self.collections.find()
        print(documents, type(documents))
        for document in documents:
            print(document, type(document))
            rows.append(document)

        return rows[0]



    def delete(self, query):
        result = self.collections.delete_one(query)
        print(result.deleted_count)

    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collections.update_one(query, update_query)
        print(result.modified_count)




def main():
    db_helper=MongoDbHelper()
    customer1 = Customer(name="Shawn", phone="7777755555",
                         email="shawn@example.com", age=23, gender="male")
    customer1.subjects = [
        {
            "name": "Physics",
            "marks": 90
        },
        {
            "name": "Maths",
            "marks": 90
        }
    ]

    customer_dictionary = vars(customer1)
    print(customer_dictionary, type(customer_dictionary))

    db_helper.insert(document=customer_dictionary)
    #customer1=Customer(name="Sia",phone="888801236",email="kim@gmail.com",age="23",gender="female")
    #customer_dictionary=vars(customer1)
    #print(customer_dictionary,type(customer_dictionary))
    #db_helper.insert(document=customer_dictionary)
    db_helper.fetch()
    #query={"phone":"888801236"}
    #db_helper.fetch_selected(query)


if __name__ == "__main__":
       main()