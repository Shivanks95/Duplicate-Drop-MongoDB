import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://ershivank1:Eva2022@cluster0.wbwkabe.mongodb.net/")

DATA_FILE_PATH ="C:/Users/User/DAVIS_INDEX_ASSIGNMENT/Prices_Mongo.csv"
DATABASE_NAME="test_pricesheet"
COLLECTION_NAME="prices"

if __name__=="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"\n Rows and Columns: {df.shape}")
    
    print("\n \n Converting CSV records to JSON Records...")
    #Connvert dataframe to json so that we can dump these record in mongo db 
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


db = client.test_pricesheet
collection = db.prices

print(f"\n Total number of documents updated to Mongo DB: {collection.count_documents({})}" )
print(f"\n Documnets added successfully! Initializing code for finding duplicate documents in Mongo DB...")