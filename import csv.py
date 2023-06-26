import csv
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongodb = os.getenv("mongodb")
username=os.getenv("MONGO_USERNAME")
password=os.getenv("MONGO_PASSWORD")
#Conectamos la base de datos
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.mjbi0oc.mongodb.net/Health_2023?retryWrites=true&w=majority")
db=client["Health_2023"]
collection=db["Sleep"]

#Ruta de acceso a CSV
csv_file=r"C:\Users\Administrador\Downloads\BD.SLEEP.csv"

#leemos el archivo para crear los documentos
with open(csv_file,"r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        document={
            "Person_ID": int(row["Person ID"]),
            "Gender":row["Gender"],
            "Age":int(row["Age"]),
            "Occupation":row["Occupation"],
            "Sleep_Duration":float(row["Sleep Duration"]),
            "Quality_of_Sleep": int(row["Quality of Sleep"]),
            "Physical_Activity_Level": int(row["Physical Activity Level"]),
            "Stress_Level": int(row["Stress Level"]),
            "BMI_Category": row["BMI Category"],
            "Blood_Pressure": row["Blood Pressure"],
            "Heart_Rate": int(row["Heart Rate"]),
            "Daily_Steps": int(row["Daily Steps"]),
            "Sleep_Disorder": row["Sleep Disorder"],
        }
        collection.insert_one(document)

print("Se llenaron todos los documentos")