
email = input("Enter your email : ").strip()

name = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print("Name : ", name)
print("Domain : ", domain)