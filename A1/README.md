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

```python3 httpc.py get  "http://httpbin.org/redirect/330"``` 

```python3 httpc.py get -v "http://httpbin.org/absolute-redirect/330""```

## POST Testing 

#### 1. POST with inline data [--d] or [-d]

```python3 httpc.py post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post'``` 

```python3 httpc.py post -h Content-Type:application/json --d '{"Assignment": 1}' 'http://httpbin.org/post' -v``` 

#### 2. POST with File [--f] or [-f] (Enter full path of file)

```python3 httpc.py post  http://httpbin.org/post --f 'post.json'``` 

```python3 httpc.py post  http://httpbin.org/post --f 'post.json' -v``` 