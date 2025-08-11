python -m venv .venv

Change directory to 

cd your_main_folder\.venv\Scripts\

and run:
activate

Change directory back to the main_folder
cd ../..

Start the FastAPI server using:
fastapi dev app/main.py

RUN A SECOND SERVER on port 8080
(.venv) C:\Users\elyas\Desktop\- University\= Blockchain and Crypto\Assessment 1\app>uvicorn main:app --reload --port 8080

Easy access to API endpoints:
http://127.0.0.1:8000/docs


add_node input
{
  "nodes": ["http://127.0.0.1:8080"]
}

{
  "nodes": ["http://127.0.0.1:8000"]
}