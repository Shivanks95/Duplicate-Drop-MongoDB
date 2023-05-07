from pymongo import MongoClient

# connect to the MongoDB instance
client = MongoClient("mongodb+srv://ershivank1:Eva2022@cluster0.wbwkabe.mongodb.net/")

# select the database and collection
db = client.test_pricesheet
collection = db.prices

# specify the fields to check for duplicates

print("\n\n Looking for duplicate documents in Mongo DB...")
unique_fields = ['status', 'startDate', 'dpc_number', 'new_price_value', 'prior_price_value']

num_duplicates = {}
for doc in collection.find({"status": "Published"}):
    unique_tuple = tuple(doc[field] for field in unique_fields)
    num_duplicates[unique_tuple] = num_duplicates.get(unique_tuple, 0) + 1

# print the number of duplicates for each unique tuple
total_duplicates = 0
for unique_tuple, count in num_duplicates.items():
    if count > 1:
        print(f"Found {count} duplicates for {unique_tuple}")
        total_duplicates += count

print(f"\n Total number of duplicates found: {total_duplicates}, Now dropping {int(total_duplicates/2)} documents...")

# delete duplicates

total_duplicates = 0
for unique_tuple, count in num_duplicates.items():
    if count > 1:
        query = {field: value for field, value in zip(unique_fields, unique_tuple)}
        duplicates = collection.find({"status": "Published", **query}).sort('startDate', -1)[1:]
        for duplicate in duplicates:
            collection.delete_one({'_id': duplicate['_id']})
            total_duplicates += 1

print(f"\n Total number of duplicates deleted: {total_duplicates}")

print(f"\n Total number of unique records after dropping duplicates: {collection.count_documents({})}")