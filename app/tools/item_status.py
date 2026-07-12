from app.koha.item_status import item_status_service


async def item_status(barcode: str):

    item = await item_status_service.get(barcode)

    if not item:
        return f"No item found with barcode '{barcode}'."

    status = "Available"

    if item.get("checked_out_date"):
        status = "Issued"

    response = (
        f"📚 Barcode : {item.get('external_id')}\n"
        f"🆔 Item ID : {item.get('item_id')}\n"
        f"📖 Biblio ID : {item.get('biblio_id')}\n"
        f"🏛 Home Library : {item.get('home_library_id')}\n"
        f"📌 Holding Library : {item.get('holding_library_id')}\n"
        f"📍 Status : {status}\n"
        f"📅 Checked Out : {item.get('checked_out_date') or 'N/A'}\n"
        f"📆 Last Seen : {item.get('last_seen_date') or 'N/A'}\n"
    )

    return response
