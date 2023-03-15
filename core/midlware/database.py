from typing import Callable, Awaitable, Dict, Any
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from core.utils.db_connect import Request

class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            hendler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str,Any]
    ) -> Any:
        async with self.connector.acquire() as connect:
            data['request'] = Request(connect)
            return await hendler(event, data)
