from datetime import time

import  asyncpg

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_names, usernames):
        query = f'''INSERT INTO "user" (user_id, name, username, time) VALUES ({user_id}, '{user_names}','{usernames}', '{time(hour=7, minute=30)}')
        ON CONFLICT (user_id) DO UPDATE SET name='{user_names}', username ='{usernames}', time ='{time(hour=7, minute=30)}';'''
        await self.connector.execute(query)

    async def get_id(self):
        query = f'''SELECT ("user_id", "time") FROM "user"'''
        return await self.connector.fetch(query)

    async def del_time(self, user_id):
        null = 'NULL'
        query = f'''UPDATE "user"  SET  time= {null} WHERE user_id = {user_id} ;'''
        await self.connector.execute(query)

    async def set_time(self, user_id, set_time:str):
        hour, minute = set_time.replace('/set_time','').strip().split('.')

        t = time(hour=int(hour), minute=int(minute))
        query = f'''UPDATE "user"  SET  time= '{t}' WHERE user_id = {user_id} ;'''
        await self.connector.execute(query)

    async def get_user_time(self, user_id):
        query = f'''SELECT  "time" FROM "user" WHERE "user_id" = {user_id}'''
        return await self.connector.fetch(query)