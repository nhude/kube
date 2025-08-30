import random
import time


def main():
    # Print a random string and store it into memory, print it out after every 5 seconds with a timestamp
    random_string = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
    while True:
        time.sleep(5)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {random_string}", flush=True)


main()
