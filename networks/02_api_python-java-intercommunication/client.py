import urllib.request
import json 

def main():
    a = int(input("Put first number to add: "))
    b = int(input("Put second number to add: "))
    
    url = f"http://127.0.0.1:5001/add?a={a}&b={b}"
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    
    print(data["result"])

if __name__ == "__main__":
    main()

