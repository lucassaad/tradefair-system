from fastapi import FastAPI

from tradefair_system.routers import auth, product, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(user.router)


@app.get('/')
def root():
    return {'project': 'tradefair-system'}
