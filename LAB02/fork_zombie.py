import os
import time
import sys

def main():
    print(f"[Parent] My PID is {os.getpid()}")
    print("[Parent] Forking a child process...")

    pid = os.fork()

    if pid > 0:
        print(f"[Parent] Created Child with PID {pid}.")
        print("[Parent] Waiting 60 seconds without calling os.wait()...")
        time.sleep(180)
        print("[Parent] Waking up and exiting.")

    elif pid == 0:
        print(f"[Child] My PID is {os.getpid()}. I am finishing my task quickly!")
        sys.exit(0)

if __name__ == "__main__":
    main()