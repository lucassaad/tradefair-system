import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from tradefair_system.app import app
from tradefair_system.database import get_session
from tradefair_system.models.registry import table_registry
from tradefair_system.models.user import User
from tradefair_system.security import get_password_hash


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        # substitui a funcao 'get_session' que usamos para a aplicacao
        # real, pela nossa funcao que retorna a fixture de testes
        app.dependency_overrides[get_session] = get_session_override
        yield client

    # limpa a sobrescrita que fizemos no app para usar a fixture de session
    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def user(session):
    user = User(
        name='Teste',
        phone_number='00000000000',
        email='teste@teste.com',
        password=get_password_hash('senha'),
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': 'senha'}
    )
    return response.json()['access_token']
