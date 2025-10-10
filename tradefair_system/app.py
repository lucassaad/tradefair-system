from fastapi import FastAPI

from tradefair_system.routers import token, user

app = FastAPI()

app.include_router(user.router)
app.include_router(token.router)


@app.get('/')
def root():
    return {'project': 'tradefair-system'}
