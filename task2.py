import secrets, string

print(
    "".join(
        secrets.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(12)
    )
)
