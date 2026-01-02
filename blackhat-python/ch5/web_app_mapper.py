import queue
import threading
import os
import urllib3

threads   = 10
target    = "https://nostarch.com"
directory = "."
filters = [".jpg",".gif",".png",".css"]

os.chdir(directory)

web_paths = queue.Queue()

for r,d,f in os.walk("."):
    for files in f:
        remote_path = "%s/%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target, path)

        try:
            response = urllib3.request("GET",url) 
            content = response.data
            print("[%d] => %s" % (response.status,path))

        except urllib3.exceptions.HTTPError:
            pass

for i in range(threads):

    print ("Spawing thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()



