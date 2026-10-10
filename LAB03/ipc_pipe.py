import os
import time


def main():
    r, w = os.pipe()
    pid = os.fork()

    if pid > 0:
        # Parent: รับข้อมูลจาก Pipe
        os.close(w)
        r_file = os.fdopen(r, "r")

        print(f"[Trainer PID:{os.getpid()}] Waiting for data from DataLoader...")
        data = r_file.read()
        print(f"[Trainer PID:{os.getpid()}] Received Data: '{data}'")
        print(f"[Trainer PID:{os.getpid()}] Training complete.")

        r_file.close()
        os.wait()

    elif pid == 0:
        # Child: ส่งข้อมูลผ่าน Pipe
        os.close(r)
        w_file = os.fdopen(w, "w")

        print(f"  -> [DataLoader PID:{os.getpid()}] Loading image from disk...", flush=True)
        time.sleep(2)

        image_data = "Image_Tensor_Batch_01"
        print(f"  -> [DataLoader PID:{os.getpid()}] Sending data through OS Pipe...", flush=True)
        w_file.write(image_data)
        w_file.close()


if __name__ == "__main__":
    main()