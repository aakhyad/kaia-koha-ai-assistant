from app.koha.checkouts import checkout_service


async def current_checkouts():

    checkouts = await checkout_service.list()

    if not checkouts:
        return "No books are currently issued."

    response = f"📚 Current Checkouts ({len(checkouts)})\n\n"

    for i, checkout in enumerate(checkouts, start=1):

        response += (
            f"{i}.\n"
            f"👤 Patron ID : {checkout.get('patron_id')}\n"
            f"📖 Item ID : {checkout.get('item_id')}\n"
            f"📅 Issued : {checkout.get('checkout_date')}\n"
            f"📆 Due : {checkout.get('due_date')}\n\n"
        )

    return response
