from sqlalchemy.ext.asyncio import AsyncSession

from streetwise_bot.models import User


async def insert_or_ignore_user(
    session: AsyncSession,
    user_id: int,
    first_name: str,
    last_name: None | str = None,
    username: None | str = None,
) -> None:
    user = await session.get(User, user_id)

    if user is None:
        new_user = User(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        session.add(new_user)
        await session.commit()
