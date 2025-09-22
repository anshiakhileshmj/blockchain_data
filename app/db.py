import asyncpg
from typing import Optional
from app.config import settings

_pool: Optional[asyncpg.Pool] = None


async def init_db_pool() -> None:
	global _pool
	if _pool is None:
		_pool = await asyncpg.create_pool(dsn=settings.SUPABASE_DB_URL, min_size=1, max_size=10)


async def close_db_pool() -> None:
	global _pool
	if _pool is not None:
		await _pool.close()
		_pool = None


def get_pool() -> asyncpg.Pool:
	if _pool is None:
		raise RuntimeError("Database pool not initialized")
	return _pool
