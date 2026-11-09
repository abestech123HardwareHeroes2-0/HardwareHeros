import platform

import psutil


def detect_hardware():
    print("Hardware Detection Results:")
    print("---------------------------")
    print(f"CPU: {platform.processor() or 'Unknown'}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False) or 'Unknown'}")
    print(f"CPU Threads: {psutil.cpu_count(logical=True) or 'Unknown'}")
    print(f"RAM: {psutil.virtual_memory().total / (1024.0 ** 3):.2f} GB")
    print(f"Operating System: {platform.system()} {platform.release()}")


if __name__ == "__main__":
    detect_hardware()
