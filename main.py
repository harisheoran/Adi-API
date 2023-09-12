from fastapi import FastAPI
from fastapi.params import Body

# create an instance of fastapi
app = FastAPI()

# this is annotation and it is called decorator
# decorator, http request method, route/path/endpoint
@app.get("/")
def root():
    #fastapi will automatically convert this python dictonary into JSON
    return {"message" : "Welcome to my Fast API"}

@app.get("/feed")
def getFeed():
    return [{"name":"Shiva","intro": "Adi Yogi" ,"about": "The Destroyer"}, {"name":"Krishna","intro": "Eigth avatar of Vishnu" ,"about": "कृष्ण"}]

@app.post("/post")
def postFeed(body: dict = Body(...)):         # Body is from Fast api, it'll extract all fields from body and convert into a python distonaries
    print(body)
    return {"message": "Succcessfully created"}