# RFID Door Lock using Python

# RFID Door Lock System

# Simulates RFID card authentication

authorized_cards = {
"RFID12345": "Authorized User 1",
"RFID67890": "Authorized User 2",
"RFID24680": "Authorized User 3"
}

def scan_rfid():
print("\n===== RFID DOOR LOCK =====")

```
card_id = input("Scan or enter RFID card ID: ").strip()

if card_id in authorized_cards:
    user = authorized_cards[card_id]

    print(f"\nCard recognized: {user}")
    print("Access Granted")
    print("Door UNLOCKED")

else:
    print("\nUnknown RFID card!")
    print("Access Denied")
    print("Door LOCKED")
```

while True:
print("\n===== RFID SECURITY SYSTEM =====")
print("1. Scan RFID Card")
print("2. Show Authorized Cards")
print("3. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    scan_rfid()

elif choice == "2":
    print("\n--- Authorized RFID Cards ---")

    for card_id, user in authorized_cards.items():
        print(f"{card_id} -> {user}")

elif choice == "3":
    print("RFID Door Lock System Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
