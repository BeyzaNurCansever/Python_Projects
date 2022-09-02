
def main():
    email_input=input("Input your email adress:")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("username:",username)
    print("domain:",domain)
    print("extension:",extension)

while True:
    main()

