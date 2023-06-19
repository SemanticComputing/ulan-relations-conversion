import requests
import os

def execute_query(store, write_file, query, name):
    print("executing query " + name)
    print(query)
    response = requests.post(store,
                             data={'query': query})
    write_file.write(response.text)

q_dir ="queries/"
files = os.listdir(q_dir)

for f_name in files:
    f_path = 'queries/' + f_name
    q_name = f_name.split(".")[0]
    q_file = open(f_path, "r")
    query = q_file.read()
    q_file.close()
    w_file = open("ttl/" + q_name + ".ttl", "w+")
    execute_query("http://vocab.getty.edu/sparql.ttl", w_file, query, f_name)
    w_file.close()
