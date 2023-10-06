import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import csv
import os

nw = os.getcwd()
bias =""
if nw[:-2]!="DB":
    bias = "DB/"

cred = credentials.Certificate("c:\\Users\\User\\Desktop\\firebaseKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

survey = db.collection("survey").stream()

results = {}
for doc in survey:
    results[doc.id] = doc.to_dict()

user = db.collection("user").stream()

users = {}
for doc in user:
    users[doc.id] = doc.to_dict()


with open(bias+"users.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email", "phone"])
    for key, value in users.items():
        writer.writerow([key, value["name"], value["email"], value["phone"]])

with open(bias+"results.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "audio", "answer", "at", "user"])
    for key, value in results.items():
        writer.writerow([key, value["audio"], value["answer"], value["at"], value["user"]])