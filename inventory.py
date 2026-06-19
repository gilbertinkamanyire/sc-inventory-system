from math import ceil


def calculate_restock_order(
    current_stock: int,
    reorder_point: int,
    max_capacity: int,
    supplier_batch_size: int,
    high_velocity: bool = False,
) -> int:
    """
    Calculate the quantity to reorder.

    Args:
        current_stock: Current inventory level.
        reorder_point: Inventory threshold for reordering.
        max_capacity: Desired maximum stock level.
        supplier_batch_size: Supplier shipment batch size.
        high_velocity: Whether item is high demand.

    Returns:
        Quantity to order.

    Raises:
        TypeError:
            If integer parameters are not integers.
        ValueError:
            If values violate business rules.
    """

    integer_values = {
        "current_stock": current_stock,
        "reorder_point": reorder_point,
        "max_capacity": max_capacity,
        "supplier_batch_size": supplier_batch_size,
    }

    for name, value in integer_values.items():
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer.")

    if current_stock < 0:
        raise ValueError("current_stock cannot be negative.")

    if reorder_point < 0:
        raise ValueError("reorder_point cannot be negative.")

    if max_capacity < 0:
        raise ValueError("max_capacity cannot be negative.")

    if max_capacity <= reorder_point:
        raise ValueError(
            "max_capacity must be greater than reorder_point."
        )

    if supplier_batch_size <= 0:
        raise ValueError(
            "supplier_batch_size must be greater than zero."
        )

    if current_stock >= reorder_point:
        return 0

    order_quantity = max_capacity - current_stock

    if high_velocity:
        safety_stock = ceil(order_quantity * 0.15)
        order_quantity += safety_stock

    rounded_order = (
        ceil(order_quantity / supplier_batch_size)
        * supplier_batch_size
    )

    return rounded_order