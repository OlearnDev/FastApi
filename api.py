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

