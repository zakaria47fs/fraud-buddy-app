import uvicorn
from fastapi import FastAPI
import logging

from endpoints.card_validate_endpoint import card_validate_router


# logging configuration
logging.basicConfig(filename='log_app.log',
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


app = FastAPI()
app.include_router(card_validate_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
