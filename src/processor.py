def process_orders(data):

    total_orders = len(data)

    delivered_orders = 0
    cancelled_orders = 0
    rejected_orders = 0

    total_revenue = 0
    total_distance = 0
    total_kpt = 0
    total_rating = 0

    rating_count = 0

    for row in data:

        status = row.get("Order Status")

        if status == "Delivered":
            delivered_orders += 1

        elif status == "Cancelled":
            cancelled_orders += 1

        elif status == "Rejected":
            rejected_orders += 1

        total = row.get("Total")

        if total is not None:
            total_revenue += total

        distance = row.get("Distance")

        if distance is not None:
            total_distance += distance

        kpt = row.get("KPT duration (minutes)")

        if kpt is not None:
            total_kpt += kpt

        rating = row.get("Rating")

        if rating is not None:
            total_rating += rating
            rating_count += 1

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    average_distance = (
        total_distance / total_orders
        if total_orders > 0
        else 0
    )

    average_kpt = (
        total_kpt / total_orders
        if total_orders > 0
        else 0
    )

    average_rating = (
        total_rating / rating_count
        if rating_count > 0
        else 0
    )

    return {
        "total_orders": total_orders,
        "delivered_orders": delivered_orders,
        "cancelled_orders": cancelled_orders,
        "rejected_orders": rejected_orders,
        "total_revenue": round(total_revenue, 2),
        "average_order_value": round(average_order_value, 2),
        "average_distance": round(average_distance, 2),
        "average_kpt": round(average_kpt, 2),
        "average_rating": round(average_rating, 2)
    }