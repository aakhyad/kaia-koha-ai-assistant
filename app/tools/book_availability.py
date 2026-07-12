from app.koha.items import item_service


async def book_availability(biblio_id: int):

    items = await item_service.get_items(biblio_id)

    total = len(items)

    available = 0

    issued = 0

    response = ""

    for item in items:

        is_available = (
            item["checked_out_date"] is None
            and item["lost_status"] == 0
            and item["withdrawn"] == 0
            and item["not_for_loan_status"] == 0
        )

        if is_available:
            available += 1
        else:
            issued += 1

    response += f"📚 Total Copies : {total}\n"
    response += f"✅ Available : {available}\n"
    response += f"📕 Issued : {issued}\n\n"

    for i, item in enumerate(items, start=1):

        status = "Available"

        if item["checked_out_date"]:
            status = "Issued"

        response += (
            f"Copy {i}\n"
            f"Barcode : {item['external_id']}\n"
            f"Library : {item['home_library_id']}\n"
            f"Status : {status}\n\n"
        )

    return response
