import threading
import time

shared_resource_lock = threading.Lock()
job_counts = {
    "Greedy_Model_A": 0,
    "Greedy_Model_B": 0,
    "Polite_Model": 0
}
is_running = True


def greedy_task(name):
    global is_running

    while is_running:
        with shared_resource_lock:
            job_counts[name] += 1

        # พักสั้น ๆ แล้วกลับมาแย่ง Lock ใหม่
        time.sleep(0.00001)


def polite_task(name):
    global is_running

    while is_running:
        # รอนานกว่าก่อนขอใช้ทรัพยากร
        time.sleep(0.01)

        with shared_resource_lock:
            job_counts[name] += 1


def main():
    global is_running

    print("--- Starting Cluster Starvation Simulation (Running for 3 seconds) ---")

    t1 = threading.Thread(target=greedy_task, args=("Greedy_Model_A",))
    t2 = threading.Thread(target=greedy_task, args=("Greedy_Model_B",))
    t3 = threading.Thread(target=polite_task, args=("Polite_Model",))

    t1.start()
    t2.start()
    t3.start()

    time.sleep(3.0)
    is_running = False

    t1.join()
    t2.join()
    t3.join()

    print("\n--- Final Resource Acquisition Counts ---")
    for worker_name, count in job_counts.items():
        print(f"{worker_name}: {count} times")


if __name__ == "__main__":
    main()