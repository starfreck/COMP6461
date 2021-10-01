## GET Testing

#### 1. GET with query parameters

```python3 httpc.py get 'http://httpbin.org/get?course=networking&assignment=1'``` 

```python3 httpc.py get 'http://httpbin.org/get?course=networking&assignment=1' -v``` 

#### 2. GET with headers

```python3 httpc.py get -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

```python3 httpc.py get -v -h 'Authorization:Basic YWxhZGRpbjpvcGVuc2VzYW1l' 'http://httpbin.org/get?course=networking&assignment=1'``` 

## POST Testing 

#### 1. POST with inline data [--d] or [-d]

```python3 httpc.py post -h Content-Type:application/js --d '{"Assignment": 1}' 'http://httpbin.org/post'``` 

```python3 httpc.py post -h Content-Type:application/js --d '{"Assignment": 1}' 'http://httpbin.org/post' -v``` 

#### 2. POST with File [--f] or [-f] (Enter full path of file)

```python3 httpc.py post  http://httpbin.org/post --f 'post.json'``` 

```python3 httpc.py post  http://httpbin.org/post --f 'post.json' -v``` 