python -m venv .venv

Change directory to 

cd your_main_folder\.venv\Scripts\

and run:
activate

Change directory back to the main_folder
cd ../..

(easy) Start the FastAPI server using:
fastapi dev app/main.py (uses port 8000)

RUN EXTRA SERVERS

cd app

CMD should look like this:

your_main_folder\app>

now run:

uvicorn main:app --reload --port 5001

uvicorn main:app --reload --port 5002

uvicorn main:app --reload --port 5003

Easy access to API endpoints:
http://127.0.0.1:5001/docs


Auto node connecting script:

python scripts/connect_nodes 2

python scripts/connect_nodes 2

add_node input

Node 1:

{
  "nodes": ["http://127.0.0.1:5002"]
}

{
  "nodes": ["http://127.0.0.1:5003"]
}

---

Node 2:

{
  "nodes": ["http://127.0.0.1:5001"]
}

{
  "nodes": ["http://127.0.0.1:5003"]
}

---

Node 3:
{
  "nodes": ["http://127.0.0.1:5001"]
}

{
  "nodes": ["http://127.0.0.1:5002"]
}