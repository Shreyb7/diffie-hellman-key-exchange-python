"""
Diffie-Hellman-Merkle Key Exchange Demo

A simple Python implementation demonstrating the Diffie-Hellman
key exchange algorithm using user-provided values.

"""


def diffie_hellman():
    print("=" * 45)
    print("   Diffie-Hellman-Merkle Key Exchange")
    print("=" * 45)

    # Public parameters
    p = int(input("\nEnter a prime number (p): "))
    g = int(input("Enter a generator (g): "))

    # Private keys
    a = int(input("\nEnter private key for User A: "))
    b = int(input("Enter private key for User B: "))

    # Compute public values
    A = pow(g, a, p)
    B = pow(g, b, p)

    print("\n----- Public Values -----")
    print(f"User A sends: {A}")
    print(f"User B sends: {B}")

    # Compute shared secret
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("\n----- Shared Secret -----")
    print(f"Key computed by User A: {key_A}")
    print(f"Key computed by User B: {key_B}")

    if key_A == key_B:
        print("\n✅ Key Exchange Successful!")
        print(f"Shared Secret Key: {key_A}")
    else:
        print("\n❌ Key Exchange Failed!")


if __name__ == "__main__":
    diffie_hellman()
