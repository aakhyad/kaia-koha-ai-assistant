from app.koha.patrons import patron_service


async def search_patrons(query: str):

    patrons = await patron_service.search(query)

    if not patrons:
        return f"No patrons found for '{query}'."

    response = f"👥 Found {len(patrons)} patron(s):\n\n"

    for i, patron in enumerate(patrons[:10], start=1):

        response += (
            f"{i}. {patron.get('firstname', '')} "
            f"{patron.get('surname', '')}\n"
            f"   🆔 User ID : {patron.get('userid', 'N/A')}\n"
            f"   🎫 Card No : {patron.get('cardnumber', 'N/A')}\n\n"
        )

    return response
