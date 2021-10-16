## GET Testing

#### 1. GET with query parameters

```python3 httpc.py get 'http://httpbin.org/get?course=networking&assignment=1'``` 

```python3 httpc.py get 'http://httpbin.org/get?course=networking&assignment=1' -v``` 

#### 2. GET with headers

```python3 httpc.py get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

```python3 httpc.py get -v -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

#### 3. GET with output file [-o]

```python3 httpc.py get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1' -v -o get.json``` 

```python3 httpc.py get -o teapot.txt "http://httpbin.org/status/418"``` 

#### 4. GET with Redirection

```python3 httpc.py get  -r "http://localhost/redirect/330"``` 

```python3 httpc.py get -v "http://localhost/absolute-redirect/330" -r```

#### 5. Multiple Header Support [-h]*

Note: You have to separate each header via comma ',' and Quote all headers together.

```python3 httpc.py get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l,Name: Vasu' 'http://httpbin.org/get?course=networking&assignment=1' -v -o get.json``` 

## POST Testing 

#### 1. POST with inline data [--d] or [-d]

```python3 httpc.py post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post'``` 

```python3 httpc.py post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post' -v``` 

#### 2. POST with File [--f] or [-f] (Enter full path of file)

```python3 httpc.py post  http://httpbin.org/post --f 'post.json'``` 

```python3 httpc.py post  http://httpbin.org/post --f 'post.json' -v``` 

## For demo(on the exe or dmg file)

#### 1. GET with query parameters

```httpc get 'http://httpbin.org/get?course=networking&assignment=1'``` 

```httpc get 'http://httpbin.org/get?course=networking&assignment=1' -v``` 

#### 2. GET with headers

```httpc get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

```httpc get -v -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

#### 3. GET with output file [-o]

```httpc get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1' -v -o get.json``` 

```httpc get -o teapot.txt "http://httpbin.org/status/418"``` 

#### 4. GET with Redirection

```httpc get  -r "http://localhost/redirect/330"``` 

```httpc get -v "http://localhost/absolute-redirect/330" -r```

#### 5. Multiple Header Support [-h]*

Note: You have to separate each header via comma ',' and Quote all headers together.

```httpc get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l,Name: Yun' 'http://httpbin.org/get?course=networking&assignment=1' -v -o get.json``` 

## POST Testing 

#### 1. POST with inline data [--d] or [-d]

```httpc post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post'``` 

```httpc post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post' -v``` 

#### 2. POST with File [--f] or [-f] (Enter full path of file)

```httpc post http://httpbin.org/post --f '/Users/yunni/Desktop/A1/COMP6461/A1/post.json'``` 

```httpc post http://httpbin.org/post --f '/Users/yunni/Desktop/A1/COMP6461/A1/post.json' -v``` 
