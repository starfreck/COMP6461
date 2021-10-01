import sys
from http_lib import httpclient

Debug = True


def main(argv):
    """The Entry Point of httpc"""

    if len(argv) == 1 and argv[0] == "help":
        help_info = """\nhttpc is a curl-like application but supports HTTP protocol only.
    
    Usage:
        httpc command [arguments]
    
    The commands are:
        get     executes a HTTP GET request and prints the response.
        post    executes a HTTP POST request and prints the response.
        help    prints this screen.
    
    Use \"httpc help [command]\" for more information about a command."""

        print(help_info)

    elif len(argv) == 2 and argv[0] == "help" and argv[1] == "get":
        get_info = """\nUsage:
        httpc get [-v] [-h key:value] URL
    
    Get executes a HTTP GET request for a given URL.
    
        -v              Prints the detail of the response such as protocol, status and headers.
        -h key:value    Associates headers to HTTP Request with the format 'key:value'."""

        print(get_info)

    elif len(argv) == 2 and argv[0] == "help" and argv[1] == "post":
        post_info = """\nUsage:
        httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL
    
    Post executes a HTTP POST request for a given URL with inline data or from file.
    
        -v              Prints the detail of the response such as protocol, status and headers.
        -h key:value    Associates headers to HTTP Request with the format 'key:value'.
        -d string       Associates an inline data to the body HTTP POST request.
        -f file         Associates the content of a file to the body HTTP POST request.
    
    Either [-d] or [-f] can be used but not both."""

        print(post_info)

    elif len(argv) > 1 and argv[0] == "get":
        get_handler(argv[1:])
    elif len(argv) > 1 and argv[0] == "post":
        post_handler(argv[1:])
    else:
        print("Invalid choice. Please try again!")


def get_handler(argv):
    """GET request handler"""
    headers = None
    verbose = False

    # Process verbose
    if "-v" in argv:
        argv.remove("-v")
        verbose = True
    # Process header
    if "-h" in argv:
        location = argv.index("-h")
        argv.remove("-h")
        headers = argv[location]
        argv.remove(headers)

    if len(argv) >= 1:
        if Debug: print("Debug---->","verbose:", verbose,"headers:", headers, "url:",argv[0])
        # Call GET Method
        httpclient(verbose=verbose, headers=headers, url=argv[0]).get()
    else:
        print("Invalid choice. Please try again!")

def post_handler(argv):
    """POST request handler"""

    file = None
    string = None
    headers = None
    verbose = False

    # Check if string and file are specified together
    if "-d" in argv and "-f" in argv:
        print("Either [-d] or [-f] can be used but not both.")
        return
    else:
        print(argv)
        # Process verbose
        if "-v" in argv:
            argv.remove("-v")
            verbose = True
        # Process header
        if "-h" in argv:
            location = argv.index("-h")
            argv.remove("-h")
            headers = argv[location]
            argv.remove(headers)
        # Process string
        if "-d" in argv:
            location = argv.index("-d")
            argv.remove("-d")
            string = argv[location]
            argv.remove(string)
        # Process file
        if "-f" in argv:
            location = argv.index("-f")
            argv.remove("-f")
            file = argv[location]
            argv.remove(file)

        if len(argv) >= 1:
            if Debug: print("Debug---->", "verbose:", verbose, "headers:", headers, "url:", argv[0], "string:", string,"file:", file)
            # Call POST Method
            httpclient(verbose=verbose, headers=headers, url=argv[0],string=string,file=file).post()
        else:
            print("Invalid choice. Please try again!")

def filter_args(argv):
    for arg in argv:
        if len(arg) == 3 and "--" in arg:
            index = argv.index(arg)
            argv[index] = arg.replace("--", "-")
    return argv

if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    argv = filter_args(sys.argv)
    main(argv)

