# for python, to allow commmunication through process of - subprocesses - we use import subprocess.
import subprocess 

def main():
    number = int(input("Choose a number between and including 0 to 4: "))
    
    result = subprocess.run(
        ["java", "Statement", str(number)], capture_output=True, text=True
    )
    # we do java and statement in this coz that would run `java Statement` from terminal, the numberbecomes the first arg then.
    # we send the number as string coz command line args are sent as strings so javs should receive strings.
    # for the text = True, its coz captured output is default returned as butes, we need text.
    
    print(result.stdout)
    # we need result.stdout coz of a single reaosn
    # result that is an object after subprocess.run, has many differnet fields of data in it.
    # stdout, stderr, stdreturncode.
    # we only need stdout to print it.

if __name__ == "__main__":
    main()

