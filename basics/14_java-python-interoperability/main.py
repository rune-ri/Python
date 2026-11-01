import subprocess 

def main():
    number = int(input("Choose a number between and including 0 to 4: "))
    
    result = subprocess.run(
        ["java", "Statement", str(number)], capture_output=True, text=True
    )
    
    print(result.stdout)

if __name__ == "__main__":
    main()

