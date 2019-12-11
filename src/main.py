#!/bin/python3

import threading
import os

from http_server import run_http_server



if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', '8080'))

    HTTP_THREAD = threading.Thread(target=run_http_server, args=(PORT,))
    HTTP_THREAD.daemon = True
    HTTP_THREAD.start()

    threading.Event().wait()
