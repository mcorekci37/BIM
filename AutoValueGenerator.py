




import random

def main():
    # for i in range(10):
    #     print(str(random.randint(0, 1)) + ",")

    while(True):
        choice = int( input("1 ) Temperature\n"
                       "2 ) Humidity\n"
                       "3 ) CO2\n"
                       "4 ) Light\n"
                       "5 ) Presense\n"
                       "6 ) All Of Them\n"
                       "0 ) Exit\n>> ") )

        if choice == 1:
            tempFile = open("data/temperature.txt", "w")
            for x in range(1000):
                print("1")
                tempFile.write(str(random.randint(-30, 30)) + ",")
            tempFile.close()
        elif choice == 2:
            tempFile = open("data/humidity.txt", "w")
            for x in range(1000):
                print("2")
                tempFile.write(str(random.random())[:4] + ",")
            tempFile.close()
        elif choice == 3:
            tempFile = open("data/co2.txt", "w")
            for x in range(1000):
                print("3")
                tempFile.write(str(random.randint(0, 5000)) + ",")
            tempFile.close()
        elif choice == 4:
            tempFile = open("data/light.txt", "w")
            for x in range(1000):
                print("4")
                tempFile.write(str(random.randint(0, 4095)) + ",")
            tempFile.close()
        elif choice == 5:
            tempFile = open("data/presence.txt", "w")
            for x in range(1000):
                print("5")
                tempFile.write(str(random.randint(0, 1)) + ",")
            tempFile.close()
        elif choice == 6:
            tempFile = open("data/temperature.txt", "w")
            for x in range(1000):
                print("1")
                tempFile.write(str(random.randint(-30, 30)) + ",")
            tempFile.close()

            tempFile = open("data/humidity.txt", "w")
            for x in range(1000):
                print("2")
                tempFile.write(str(random.random()) + ",")
            tempFile.close()

            tempFile = open("data/co2.txt", "w")
            for x in range(1000):
                print("3")
                tempFile.write(str(random.randint(0, 5000)) + ",")
            tempFile.close()

            tempFile = open("data/light.txt", "w")
            for x in range(1000):
                print("4")
                tempFile.write(str(random.randint(0, 4095)) + ",")
            tempFile.close()

            tempFile = open("data/presence.txt", "w")
            for x in range(1000):
                print("5")
                tempFile.write(str(random.randint(0, 1)) + ",")
            tempFile.close()
        elif choice == 0:
            print("0")
            break
if __name__ == '__main__':
    main()