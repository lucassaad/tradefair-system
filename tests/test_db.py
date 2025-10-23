import pytest
from sqlalchemy import select

from tradefair_system.models.user import User


@pytest.mark.asyncio
async def test_create_user(session):
    new_user = User(
        name='lucas',
        email='lucassaadro@gmail.com',
        phone_number='61991052451',
        password='senha',
    )

    session.add(new_user)
    await session.commit()

    user = await session.scalar(
        select(User).where(User.email == 'lucassaadro@gmail.com')
    )

    assert user.name == 'lucas'
    assert user.email == 'lucassaadro@gmail.com'
    assert user.phone_number == '61991052451'
