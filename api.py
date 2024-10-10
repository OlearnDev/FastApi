from fastapi import FastAPI
import uvicorn

app=FastAPI()

#--- Simple api REST avec get method
@app.get("/")
async def hello_world():
    return {"hello" : "world"}

#-- Une autre manière de faire est ci-dessous:
#if __name__=='__main__':
#   uvicorn.run(app, host="127.0.0.1", port=8000)
    #app.run(debug=True)

@app.get("/Component/{component_id}") #path parameter
async def get_component(component_id:int):
	# operations
	return {"component_id" : component_id}

@app.get("/component/") #path parameter
async def read_component(number:int, text:str):
	return {"number" : number, "text": text}

#http://127.0.0.1:8000/component/?number=12&text=Le%20contenu%20du%20texte