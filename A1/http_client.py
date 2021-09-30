from urllib.parse import urlparse


def cmd_help(arg):
    if arg == 'help':
        print('General')
        print('httpc help')
        print('httpc is a curl-like application but supports HTTP protocol only.')
        print('Usage:')
        print('\t httpc command [arguments]')
        print('The commands are:')
        print('get \t executes a HTTP GET request and prints the response.')
        print('post \t executes a HTTP POST request and prints the response.')
        print('help \t prints this screen.')
        print('Use "httpc help [command]" for more information about a command.')

    elif arg == 'get':
        print('Get Usage')
        print('httpc help get')
        print('usage: httpc get [-v] [-h key:value] URL')
        print('-v \t Prints the detail of the response such as protocol, status,and headers.')
        print('-h key:value  \t Associates headers to HTTP Request with the format key:value.')

    elif arg == 'post':
        print('Post Usage')
        print('httpc help get')
        print('usage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL')
        print('Post executes a HTTP POST request for a given URL with inline data or from file.')
        print('-v \t Prints the detail of the response such as protocol, status,and headers.')
        print("-h key:value \t Associates headers to HTTP Request with the format'key:value'.")
        print('-d string \t Associates an inline data to the body HTTP POST request.')
        print('-f file \t Associates the content of a file to the body HTTP POST request.')
        print('Either [-d] or [-f] can be used but not both.')


class http_client:
    pass


if __name__ == '__main__':
    url = urlparse('http://httpbin.org/get?course=networking&assignment=1"')
    rqst_msg = 'GET ' + url.path
    para = url.query
    if len(para) > 0:
        rqst_msg = rqst_msg + '?' + para
    print(rqst_msg)

    # cmd_help('help')
