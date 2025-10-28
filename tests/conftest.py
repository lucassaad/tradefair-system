import factory
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
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


class UserFactory(factory.Factory):  # define uma fabrica para o modelo User
    class Meta:  # classe interna usada para configurar a fabrica
        # define o modelo para o qual a fabrica esta construindo instanciais
        model = User
    # a cada chamada da fabrica o valor "n" incrementado instancias diferentes
    name = factory.Sequence(lambda n: f'test{n}')
    phone_number = factory.Sequence(lambda n: f'119999999{n:02d}')
    email = factory.LazyAttribute(lambda obj: f'{obj.name}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.name}@example.com')


@pytest_asyncio.fixture
async def session():
    engine = create_async_engine(
        'sqlite+aiosqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    # engine.begin() inicia uma transação assíncrona com o banco de dados
    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.create_all)

    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.drop_all)


@pytest_asyncio.fixture
async def user(session):
    user = UserFactory(
        password=get_password_hash('senha'),
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


@pytest_asyncio.fixture
async def other_user(session):
    user = UserFactory(
        password=get_password_hash('senha'),
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token', data={'username': user.email, 'password': 'senha'}
    )
    return response.json()['access_token']
