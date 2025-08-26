def myFunc():
    print("Hello module 1")


if __name__ == "__main__":
    print("you're directly running this code")
    myFunc()
print(__name__)  # ? gives the file name from where im running the module
