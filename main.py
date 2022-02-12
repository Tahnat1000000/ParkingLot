# CREATING PARKING LOT
# parkingLot METHOD - FOR MAKING NEW PARKING LOT, PARAMETERS (SIZE)
# markParkingSpot METHOD - FOR MARK NEW CAR IN PARKING , PARAMETERS (SPOT NUMBER)
import turtle, random, time

LOT_MIN_SIZE = 1
LOT_MAX_SIZE = 120
VERTICAL_LINE = 30
HORIZINTAL_LINE = 40

parking_lot_size = 0
occupied_parking_lots = []

tur = turtle.Turtle()
tur.hideturtle()
tur.speed(100)


def goToStartPoint():
    tur.penup()
    tur.goto(-250, 180)
    tur.pendown()

def parkingSpot1():
    tur.forward(VERTICAL_LINE)
    tur.left(90)
    tur.forward(HORIZINTAL_LINE)
    tur.backward(HORIZINTAL_LINE)
    tur.right(90)

def parkingSpot2():
    tur.forward(VERTICAL_LINE)
    tur.left(90)
    tur.forward(HORIZINTAL_LINE)
    tur.backward(HORIZINTAL_LINE * 2)
    tur.forward(HORIZINTAL_LINE)
    tur.right(90)


def parkingLot(size):
    goToStartPoint()

    if size < LOT_MIN_SIZE or size > LOT_MAX_SIZE:
        print("ERROR: PARKING LOT SIZE MUST BE NUMBER BETWEEN 1-120")
        pass

    parkingSpots = 0
    if (type(size) != int):
        print("ERROR: PARKING LOT SIZE MUST BE NUMBER BETWEEN 1-120")
        pass

    # IF ALL CHECK PASSED, WE WILL DEFINE parking_lot_size AS THE SIZE OF PARKING LOT FOR FUTURE CHECK IN markParkingSpot
    global parking_lot_size
    parking_lot_size = size

    while size != 0:
        if size >= 2:
            if (parkingSpots % 10 == 0):
                tur.left(90)
                tur.forward(HORIZINTAL_LINE)
                tur.backward(HORIZINTAL_LINE * 2)
                tur.forward(HORIZINTAL_LINE)
                tur.right(90)
            parkingSpot2()
            size -= 2
            parkingSpots += 2
        else:
            if (parkingSpots % 10 == 0):
                tur.left(90)
                tur.forward(HORIZINTAL_LINE)
                tur.backward(HORIZINTAL_LINE)
                tur.right(90)
            parkingSpot1()
            size -= 1
            parkingSpots += 1

        if (parkingSpots % 10 == 0):
            tur.penup()
            tur.forward(VERTICAL_LINE)
            tur.pendown()

        if (parkingSpots % 30 == 0):
            tur.penup()
            tur.backward(VERTICAL_LINE * 18)
            tur.right(90)
            tur.forward(HORIZINTAL_LINE * 3)
            tur.left(90)
            tur.pendown()


def markParkingSpot(spotNumber):
    global parking_lot_size, occupied_parking_lots

    if spotNumber < 1 or spotNumber > parking_lot_size:
        print("ERROR: PARKING SPOT NUMBER IS NOT EXISTS", spotNumber,">",parking_lot_size)
        pass

    if spotNumber in occupied_parking_lots:
        print("ERROR: PARKING NUMBER:", spotNumber, "IS OCCUPIED")
        pass
    else:
        occupied_parking_lots.append(spotNumber)

    goToStartPoint()
    tur.penup()
    tur.backward(VERTICAL_LINE // 2)

    if (spotNumber % 30 != 0):
        tur.right(90)
        tur.forward(HORIZINTAL_LINE * 3 * (spotNumber // 30))
        tur.left(90)
        parkingRowZone = (spotNumber % 30) // 10
        if (spotNumber % 30) % 10 == 0:
            parkingRowZone -= 1
        tur.forward(VERTICAL_LINE * parkingRowZone)
    else:
        tur.right(90)
        tur.forward(HORIZINTAL_LINE * 3 * ((spotNumber // 30) - 1))
        tur.left(90)
        tur.forward(VERTICAL_LINE * 2)

    tur.color("red")
    if spotNumber % 2 == 1:
        tur.forward(VERTICAL_LINE * ((spotNumber % 30) // 2 + 1))
        tur.left(90)
        tur.forward(HORIZINTAL_LINE // 2)
        tur.pendown()
        tur.stamp()
        tur.right(90)
    else:
        if spotNumber % 30 == 0:
            tur.forward(VERTICAL_LINE * 15)
        else:
            tur.forward(VERTICAL_LINE * (spotNumber % 30 // 2))
        tur.right(90)
        tur.forward(HORIZINTAL_LINE // 2)
        tur.pendown()
        tur.stamp()
        tur.left(90)


size = random.randint(LOT_MIN_SIZE, LOT_MAX_SIZE)
parkingLot(size) # CREATE NEW PARKING LOT
for i in range(10):
    markParkingSpot(random.randint(1, parking_lot_size)) # MARK PARKING SPOT AS OCCUPIED
time.sleep(5)
