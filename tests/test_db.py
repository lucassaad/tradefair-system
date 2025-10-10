from sqlalchemy import select

from tradefair_system.models.user import User


def test_create_user(session):
    new_user = User(
        name='lucas',
        phone_number='61991052451',
        email='lucassaadro@gmail.com',
        password='senha',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.name == 'lucas'))

    assert user.name == 'lucas'
