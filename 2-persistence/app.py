from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), 'www')), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Define the path to the index.html file
    index_file_path = os.path.join(os.getcwd(), 'www', 'index.html')
    
    # Read the content of the index.html file
    with open(index_file_path, 'r') as file:
        html_content = file.read()
    
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
