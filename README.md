# 🔑 Diffie-Hellman-Merkle Key Exchange in Python

A simple Python implementation demonstrating the **Diffie-Hellman-Merkle Key Exchange** algorithm for securely establishing a shared secret between two communicating parties.

---

## 📖 Overview

The Diffie-Hellman-Merkle Key Exchange algorithm enables two users to securely generate the same shared secret over an insecure communication channel without transmitting the secret itself.

This implementation accepts user input for the public parameters and private keys, making it suitable for learning and experimenting with the algorithm.

> **Note:** This project is intended for educational purposes and uses small numerical values for demonstration. Real-world implementations use very large prime numbers to provide strong security.

---

## ✨ Features

- Interactive user input
- Diffie-Hellman Key Exchange
- Shared secret generation
- Modular exponentiation
- Command-line interface
- Beginner-friendly implementation

---

## 🛠 Technologies Used

- Python 3

---

## 🚀 Running the Program

Clone the repository:

```bash
git clone https://github.com/yourusername/diffie-hellman-key-exchange-python.git
```

Navigate into the project:

```bash
cd diffie-hellman-key-exchange-python
```

Run the program:

```bash
python diffie_hellman_demo.py
```

---

## 📂 Repository Structure

```
diffie-hellman-key-exchange-python
│
├── diffie_hellman_demo.py
├── README.md
└── .gitignore
```

---

## 📚 Learning Objectives

- Understand public key cryptography
- Learn how secure key exchange works
- Understand modular exponentiation
- Explore shared secret generation
- Learn the fundamentals of modern cryptographic protocols

---

## 📌 Example

```
Enter a prime number (p): 23
Enter a generator (g): 5

Enter private key for User A: 6
Enter private key for User B: 15

----- Public Values -----
User A sends: 8
User B sends: 19

----- Shared Secret -----
Key computed by User A: 2
Key computed by User B: 2

✅ Key Exchange Successful!
Shared Secret Key: 2
```

---

