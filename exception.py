try:
    with open ("D;/sesk/SSGT/Django/hellos.txt","r")as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("The file was not found.")
except Exception as err:
    print(f"An error occurred: {err}")
finally:
    #db close 
     print("Cleaning up")                   