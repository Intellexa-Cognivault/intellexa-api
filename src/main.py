from fastapi import FastAPI
from intellexa.core.utils import validate_input  # Import from core

app = FastAPI()

@app.post("/process")
async def process(data: dict):
    """
    Receives and processes incoming data via a POST request.

    The function validates the input data using a utility function from intellexa core.
    Upon successful validation, it returns a status indicating the data has been processed.

    Args:
        data (dict): The input data to be processed.

    Returns:
        dict: A dictionary containing the status of the processing.
    """

    # Validate the input data using a utility function from intellexa core
    validate_input(data)  
    
    # Return a response indicating the data has been processed
    return {"status": "processed"}
