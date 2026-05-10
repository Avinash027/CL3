import Pyro4

@Pyro4.expose
class StringConcatenationServer:
    def concatenate_strings(self, str1, str2):
        result = str1 + str2
        return result

def main():
    daemon = Pyro4.Daemon()  
    ns = Pyro4.locateNS()  
    
    server = StringConcatenationServer()
    
    uri = daemon.register(server)
    ns.register("string.concatenation", uri)
    print("Server URI:", uri)
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))
    daemon.requestLoop()

if __name__ == "__main__":
    main()


#How to run it in the future:
#Always ensure you have three separate terminal windows (or background processes) in this order:
#Start Nameserver: python -m Pyro4.naming
#Start Server: python server.py
#Start Client: python client.py