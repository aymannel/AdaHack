### **NFC-Powered Peer-to-Peer Payment Settlements**

**Problem:**
Casual debts among friends (like rounds at the pub) often go unpaid because there’s no frictionless, fee-free way to settle them. Existing contactless payment systems rely on acquiring banks, introducing fees and unnecessary intermediaries.

**Goal:**
Make casual debt settlement intuitive, fee-free, and as easy as tapping a sticker.

**Solution:**
A peer-to-peer payment system that uses NFC to initiate bank-to-bank transfers directly—bypassing acquiring banks. It functions like a physical interface for debt settlement, combining the simplicity of tap-to-pay with the delayed-settlement flexibility of Splitwise.

**How it works:**
* Users register in-app, link a payment method (e.g. Apple Pay, Google Pay, PayPal) and receiving account (bank details).
* Each user gets an NFC sticker or uses their phone’s NFC.
* Either party can initiate or request a payment by tapping phones or scanning the other’s NFC tag, entering the amount, and approving the transaction.

**Example Scenarios:**
1. A taps B’s NFC, sends £10.
2. B scans A’s NFC, requests £10; A gets a notification to approve/decline/pay later.

**Core Requirements:**
* Physical NFC sticker or phone-based tag
* In-app ordering and registration
* NFC ID is paired with the user’s device/account
* Linked payment and receiving methods

**Limitations:**
* Don't have access to physical NFCs
* Don't have time to set up notificaiton service
* This is why we are simulating the notifications


**Sponsor Integrations:**
* How are we going to use our sponsor's tech stacks?
* Google Cloud infrastructure? 
* Mollie payment processing - they would be used to create and handle a payment session


**Revenue Streams:**
* Deposits in app earn interest
* Deposits come from people who opt to 'pay later'

### SETUP
start the service
```bash
# development
fastapi dev --host 127.0.0.1 --port 8000 service.py

# production
uvicorn service:app --host 127.0.0.1 --port 8000

ngrok ///
```