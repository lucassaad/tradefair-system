from fastapi import FastAPI

from tradefair_system.routers import user

app = FastAPI()

app.include_router(user.router)


@app.get('/')
def root():
    return {'project': 'tradefair-system'}
