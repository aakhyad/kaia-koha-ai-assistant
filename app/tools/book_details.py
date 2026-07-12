from app.koha.book_details import book_details_service


async def book_details(biblio_id: int):

    book = await book_details_service.get(biblio_id)

    response = f"""
📖 Title : {book.get('title', 'N/A')}
👤 Author : {book.get('author') or 'Unknown'}
📚 ISBN : {book.get('isbn') or 'N/A'}
🏷️ Biblio ID : {book.get('biblio_id')}
🏢 Publisher : {book.get('publisher') or 'N/A'}
📅 Copyright : {book.get('copyright_date') or 'N/A'}
📄 Pages : {book.get('pages') or 'N/A'}
"""

    return response
