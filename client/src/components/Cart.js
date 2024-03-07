import React, { useState, useEffect } from 'react';

function Cart() {
    const [cartItems, setCartItems] = useState([]);
    const [subtotal, setSubtotal] = useState(0);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchCartItems();
    }, []);

    const fetchCartItems = () => {
        setLoading(true);
        fetch('/cart')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch cart items');
                }
                return response.json();
            })
            .then(data => {
                setCartItems(data);
                calculateSubtotal(data);
                setLoading(false);
            })
            .catch(error => {
                setError('Error fetching cart items');
                setLoading(false);
            });
    };

    const removeFromCart = (orderItem) => {
        setLoading(true);
        fetch(`/cart/${orderItem.id}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to remove item from cart');
                }
                fetchCartItems();
            })
            .catch(error => {
                setError('Error removing item from cart');
                setLoading(false);
            });
    };

    const calculateSubtotal = (items) => {
        const total = items.reduce((acc, item) => {
            return acc + (item.price * item.quantity);
        }, 0);
        setSubtotal(total);
    };

    return (
        <div>
            <h2>Your Cart</h2>
            {loading && <p>Loading...</p>}
            {error && <p>{error}</p>}
            {cartItems.length === 0 && !loading && !error && <p>Your cart is empty</p>}
            {cartItems.length > 0 && (
                <>
                    <ul>
                        {cartItems.map(item => (
                            <li key={item.id}>
                                <div>{item.name}</div>
                                <div>Quantity: {item.quantity}</div>
                                <div>Price: ${item.price}</div>
                                <button onClick={() => removeFromCart(item)}>Remove</button>
                            </li>
                        ))}
                    </ul>
                    <p>Subtotal: ${subtotal}</p>
                </>
            )}
        </div>
    );
}

export default Cart;