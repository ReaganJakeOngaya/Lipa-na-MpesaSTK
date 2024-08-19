import React, { useState } from 'react';
import '../Payment.css'; // Import the CSS file

function Payment() {
    const [phone, setPhone] = useState('');

    const initiatePayment = async () => {
        try {
            // Fetch the token
            const tokenResponse = await fetch(`${process.env.REACT_APP_BACKEND_URL}/get_token`);
            const tokenData = await tokenResponse.json();
            const token = tokenData.access_token;

            // Fetch the payment response
            const paymentResponse = await fetch(`${process.env.REACT_APP_BACKEND_URL}/stk_push`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({ phone }),
            });

            const paymentData = await paymentResponse.json();
            console.log(paymentData);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className="payment-container">
            <h3 className="payment-title">Lipa na Mpesa</h3>
            <div className='phone-no'>
            <label className='labeling'>Phone No.</label>
            <input
                type="text"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
                placeholder=" +254XXXXXXXXX "
                className="payment-input"
            />
            </div>
            <button onClick={initiatePayment} className="payment-button">
                Pay Now
            </button>
        </div>
    );
}

export default Payment;


