import threading
import time
import sys

num_filling_stations = 4

semaphore = threading.Semaphore(num_filling_stations)

total_cars = 0
cars_drove_past = 0
refueling_threads = []


def car_arrives():
    global total_cars, cars_drove_past
    while total_cars < 120:
        time.sleep(2)
        total_cars += 1
        print(f"Car {total_cars} arrives at the gas station.")
        if semaphore.acquire(blocking=False):
            refueling_thread = threading.Thread(target=refuel_car, args=(total_cars,))
            refueling_thread.start()
            refueling_threads.append(refueling_thread)
        else:
            cars_drove_past += 1
            print(f"Car {total_cars} drove past as all filling stations are occupied.")


def refuel_car(car_number):
    global semaphore
    with semaphore:
        print(f"Car {car_number} starts refueling.")
        time.sleep(20)
        print(f"##########Car {car_number} finishes refueling.##################")

    semaphore.release()



if __name__ == "__main__":
    car_arrives_thread = threading.Thread(target=car_arrives)
    car_arrives_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation terminated.")
        print(f"Total cars: {total_cars}")
        print(f"Cars that drove past: {cars_drove_past}")

    car_arrives_thread.join()

    print("All cars have completed the simulation.")
