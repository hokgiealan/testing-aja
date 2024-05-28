from pytube import YouTube
import sys
import time
import threading

# Mengubah resolusi menjadi bentuk numerik
def extract_resolution_number(resolution):
    return int(resolution[:-1])

def animasi_loading():
    chars = "/—\|"
    i = 0
    while not done:
        sys.stdout.write("\r" + chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

def pilih_resolusi(url, resolusi):
    global done
    done = False

    video = YouTube(url)
    print(f"\nDownloading \033[1m{video.title}\033[0m with \033[1m{resolusi}\033[0m resolution .... \n" )
    download = video.streams.filter(file_extension="mp4").get_by_resolution(resolusi)

    loading_thread = threading.Thread(target=animasi_loading)
    loading_thread.start()

    download.download()
    done = True
    loading_thread.join()
    print("\nDone...")
    

print("\033[1m==== Insert Url YouTube Video ====\033[0m")
url = str(input())

resolusi = {}
index = 1

try:
    print("\nChecking available resolution.....\n ")
    for stream in YouTube(url).streams.filter(progressive="True"):
        if stream.resolution not in resolusi.values():
            resolusi[index] = stream.resolution
            index += 1

    # Sorting resolusi berdasarkan nilai numerik
    sorted_resolusi = sorted(resolusi.values(), key=extract_resolution_number)

    # Cetak resolusi yang tersedia
    for i, res in enumerate(sorted_resolusi, start=1):
        print(f"{i}. {res}")

    while True :
        pilihan = input("\nInsert your choice : ")
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(sorted_resolusi):
            pilihResolusi = sorted_resolusi[int(pilihan)-1]
            pilih_resolusi(url, pilihResolusi)
            break
        else:
            print("Sorry the resolution you choose doesn't available, please try again ")
except Exception as e:
    print(f"\033[1mThe url video u are inputin can't be handled further by the program caused {e}\033[0m\n")
