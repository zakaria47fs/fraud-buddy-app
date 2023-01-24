import uvicorn
from fastapi import FastAPI
import logging

from endpoints.card_validate_endpoint import card_validate_router
from endpoints.campaign_endpoint import campaign_router
from endpoints.rules_endpoint import rules_router


# logging configuration
logging.basicConfig(filename='log_app.log',
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


app = FastAPI()

app.include_router(card_validate_router)
app.include_router(campaign_router)
app.include_router(rules_router)


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
