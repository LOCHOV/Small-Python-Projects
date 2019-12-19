import socket


def parse(data, rec):
    try:
        parse_data = str(data)
        url = parse_data.split("\n")[0].split(" ")[1]
        port = parse_port(url)
        url_noport = url.replace(port, "")
        url = url_noport.replace(":", "")
        ip = socket.gethostbyname(url)

        print("\n" + url + " ____ " + ip + " ____ " + port)
        forward_proxy(ip, port, data, rec)
    except Exception:
        pass


def parse_port(url):
    try:
        url_list = list(url)
        index = url_list.index(":")
        port_list = url[index + 1:]
        port_str = "".join(port_list)
        return port_str
    except Exception:
        pass


def forward_proxy(web, port, data, rec):
    try:
        # send request to webserver
        new_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with new_serv as s:
            s.connect((web, 80))
            s.send(data)
            print("data sent to web")
            # pick the answer from the webserver on the first request
            while True:
                answer = s.recv(8192)
                print("answer from web:    " + str(answer))
                if len(answer) > 0:
                    rec.sendall(answer)
                    print("answer was sent to client (localhost)")
                else:
                    print("Problem with web data")
                    s.close()
                    break

            rec.close()
    except socket.error:
        print("error")


def main():
    host = ""
    port = 12345

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with serv as a:
        a.bind((host, port))
        print("Successfull bind:")
        a.listen(5)
        print("Server started on port " + str(port))
        while True:
            (rec, addr) = a.accept()
            data = rec.recv(8192)
            # Data parsing
            output = parse(data, rec)


main()






