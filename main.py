from text2sql import Text2Sql
from fastapi import FastAPI, Body
import re
from fastapi.responses import JSONResponse
import torch
import os

app = FastAPI()

@app.post('/')
async def main(input_prompt: str= Body(..., media_type="text/plain")):
    # preprocess = lambda x: "## Provide the documentation of the following code: ## \n\n"+ re.sub(r'\n','new_line',x)
    
    preprocess = lambda x: re.sub(r'\n','\n',x)
    input_prompt = preprocess(input_prompt)
    input_ids = model.tokenize(input_prompt)
    query = model.predict(input_ids)
    query = query.replace('.', '\n')
    # else:
        # query = query.replace(':', '\n')
    query = {'documentation': query}

    torch.cuda.empty_cache()

    print(f"\n\n{query['documentation']}")
    
    return JSONResponse(content= query)

if __name__ == '__main__':
    model = Text2Sql('hypernetwork-tuned-FLAN-T5')
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)