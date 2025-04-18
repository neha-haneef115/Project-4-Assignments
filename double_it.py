def main():
    current_num = int(input("Number: "))
    
    while current_num <= 100:
        current_num *= 2  
        print(current_num, end=" ")

if __name__ == "__main__":
    main()
