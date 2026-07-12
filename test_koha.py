import asyncio
from app.koha.biblios import biblios_service

async def main():
    books = await biblios_service.search("ai")
    print(books)

asyncio.run(main())
