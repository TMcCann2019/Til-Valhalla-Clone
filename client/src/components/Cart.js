import React, { useState, useEffect } from 'react';

function Cart() {
    const [cartItems, setCartItems] = useState([]);

    useEffect(() => {
        fetchCartItems();
    }, []);

    const fetchCartItems = () => {
        fetch('/cart')
            .then(response => response.json())
            .then(data => {
                setCartItems(data);
            })
            .catch(error => console.error('Error fetching cart items:', error));
    };

    const removeFromCart = (itemId) => {
        fetch(`/cart/${itemId}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    fetchCartItems();
                } else {
                    console.error('Failed to remove item from cart');
                }
            })
            .catch(error => console.error('Error removing item from cart:', error));
    };

    return (
        <div>
            <h2>Your Cart</h2>
            {cartItems.length === 0 ? (
                <p>Your cart is empty</p>
            ) : (
                <ul>
                    {cartItems.map(item => (
                        <li key={item.id}>
                            <div>{item.product_name}</div>
                            <div>{item.quantity}</div>
                            <div>{item.price}</div>
                            <button onClick={() => removeFromCart(item.id)}>Remove</button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default Cart;