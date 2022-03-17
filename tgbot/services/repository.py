from typing import List


class Repo:
    """
    Docs asyncpg: https://magicstack.github.io/asyncpg/current/
    """
    
    """Db abstraction layer"""

    def __init__(self, conn):
        self.conn = conn

    # users
    async def add_user(self, user_id, phone) -> None:
        """Store user in DB, ignore duplicates"""
        await self.conn.execute(
            "INSERT INTO tg_users(userid, phone) VALUES($1,$2) ON CONFLICT DO NOTHING",
            user_id,
            phone
        )
        return

    async def list_users(self) -> List[int]:
        """List all bot users"""
        return await self.conn.execute("select userid from tg_users")
