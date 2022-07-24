from typing import List


class Repo:
    """
    Docs asyncpg: https://magicstack.github.io/asyncpg/current/
    """

    """Db abstraction layer"""

    def __init__(self, conn):
        self.conn = conn

    # users
    async def add_user(self, userid: int):
        """Store user in DB, ignore duplicates"""
        await self.conn.execute(
            "INSERT INTO tg_users(user_id) VALUES ($1) ON CONFLICT DO NOTHING",
            userid
        )

    async def get_user(self, userid: int):
        return await self.conn.fetchrow("SELECT * FROM tg_users WHERE user_id = $1", userid)

    async def change_user_lang(self, userid: int, lang: str):
        await self.conn.execute("UPDATE tg_users SET lang = $1 WHERE user_id = $2", lang, userid)

    async def list_users(self) -> List[int]:
        """List all bot users"""
        return await self.conn.fetch("SELECT user_id FROM tg_users")
