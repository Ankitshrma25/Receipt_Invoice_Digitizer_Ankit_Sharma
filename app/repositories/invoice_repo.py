from app.models import Invoice

def create_invoice(db, data, file_path, user_id):

    invoice = Invoice(
        invoice_number=data.get("invoice_number"),
        vendor_name=data.get("vendor_name"),
        date=data.get("date"),
        total_amount=float(data.get("total_amount", "0").replace("$", "").strip()),
        file_path=file_path,
        user_id=user_id
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice