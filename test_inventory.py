import pytest

from inventory import calculate_restock_order


# --------------------------
# Happy Path Tests
# --------------------------

def test_standard_restock():
    result = calculate_restock_order(
        current_stock=20,
        reorder_point=30,
        max_capacity=100,
        supplier_batch_size=10,
        high_velocity=False,
    )

    assert result == 80


def test_high_velocity_restock():
    result = calculate_restock_order(
        current_stock=20,
        reorder_point=30,
        max_capacity=100,
        supplier_batch_size=10,
        high_velocity=True,
    )

    # Base = 80
    # Safety stock = ceil(80 * 0.15) = 12
    # Total = 92
    # Rounded to nearest batch of 10 = 100

    assert result == 100


# --------------------------
# Defensive Tests
# --------------------------

def test_negative_stock():
    with pytest.raises(ValueError):
        calculate_restock_order(
            current_stock=-1,
            reorder_point=20,
            max_capacity=100,
            supplier_batch_size=10,
        )


def test_zero_batch_size():
    with pytest.raises(ValueError):
        calculate_restock_order(
            current_stock=10,
            reorder_point=20,
            max_capacity=100,
            supplier_batch_size=0,
        )


def test_invalid_capacity_relationship():
    with pytest.raises(ValueError):
        calculate_restock_order(
            current_stock=10,
            reorder_point=50,
            max_capacity=50,
            supplier_batch_size=10,
        )


def test_non_integer_input():
    with pytest.raises(TypeError):
        calculate_restock_order(
            current_stock=10.5,
            reorder_point=20,
            max_capacity=100,
            supplier_batch_size=10,
        )