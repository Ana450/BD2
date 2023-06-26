from pymongo import MongoClient
from py2neo import Graph, Node, Relationship

# Conexión a MongoDB
client = MongoClient(f"mongodb+srv://fernandoperalta:Fercho1597530022@cluster0.mjbi0oc.mongodb.net/Health_2023?retryWrites=true&w=majority")
db=client["Health_2023"]
collection=db["Sleep"]

def opcion1():
    pass

def opcion2():
    pass

def opcion3():
    #query opcion3
    pass

def default():
    #codigo caso por defecto
    pass

def switch_case(argument):
    switch={
        "opcion1":opcion1,
        "opcion2":opcion2,
        "opcion3":opcion3
    }

    switch.get(argument,default)()

query = {"BMI_Category":"Obese"}
results = collection.find(query)

# Conexión a Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "123456789"))

for result in results:
    # Crear el nodo Employee
    person_node = Node("Person",
                         Person_id=result["Person_ID"],
                         Gender=result["Gender"],
                         Sleep_duration=result["Sleep_Duration"],
                         Heart_Rate=result["Heart_Rate"],
                         Blood_Pressure=result["Blood_Pressure"],
                         Sleep_Disorder=result["Sleep_Disorder"],
                         BMI_Category=result["BMI_Category"],
                         Daily_Steps=result["Daily_Steps"])
    graph.create(person_node)

    # Crear el nodo de Location si no existe
    Age_node = Node("Age", Age=result["Age"])
    graph.merge(Age_node, "Age", "Age")

    Occupation_node=Node("Occupation",Occupation=result["Occupation"])
    graph.merge(Occupation_node,"Occupation","Occupation")

    QS_Node=Node("Quality_of_Sleep",Quality_of_Sleep=result["Quality_of_Sleep"])
    graph.merge(QS_Node,"Quality_of_Sleep","Quality_of_Sleep")

    PA_node=Node("Physical_Activity_Level",Physical_Activity_Level=result["Physical_Activity_Level"])
    graph.merge(PA_node,"Physical_Activity_Level","Physical_Activity_Level")

    Stress_node=Node("Stress_Level",Stress_Level=result["Stress_Level"])
    graph.merge(Stress_node,"Stress_Level","Stress_Level")

    # Crear la relación entre persona y Location
    relationship = Relationship(person_node, "Edad:", Age_node)
    graph.create(relationship)

    relacion2 = Relationship(person_node,"Trabajo:",Occupation_node)
    graph.create(relacion2)

    relacion3 =Relationship(person_node,"Calidad_de_sueño",QS_Node)
    graph.create(relacion3) 
    
    relacion4 = Relationship(person_node, "Actividad_fisica:", PA_node)
    graph.create(relacion4)

    relacion5 = Relationship(person_node, "Nivel_stress:", Stress_node)
    graph.create(relacion5)


print("consulta para ver toda la base de datos, consultas de cada equipo y que sea automatizada, aprender a manejar mejor los nodos y que cada nodo se controle cuales de los atributos se muestran en los nodos")
