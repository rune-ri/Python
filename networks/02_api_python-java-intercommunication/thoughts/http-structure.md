# HTTP Message Structure

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between clients and servers.

An HTTP message consists of:

1. Start line
2. Headers
3. Empty line
4. Optional message body

```text
+------------------------------+
| Start Line                   |
+------------------------------+
| Headers                      |
| Header-Name: Header-Value    |
| Header-Name: Header-Value    |
+------------------------------+
| Empty Line                   |
+------------------------------+
| Optional Message Body        |
+------------------------------+
```

The request and response have different start lines.

---

## 1. HTTP Request Structure

An HTTP request is sent from a client to a server.

### General structure

```http
METHOD /path?query HTTP/version
Header-Name: Header-Value
Header-Name: Header-Value

Optional Request Body
```

### Example: GET request

```http
GET /add?a=10&b=20 HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

### Request components

| Component | Meaning | Example |
|---|---|---|
| Method | Operation requested | `GET` |
| Path | Requested endpoint | `/add` |
| Query | Additional URL parameters | `a=10&b=20` |
| HTTP version | Protocol version | `HTTP/1.1` |
| Headers | Additional request information | `Host: 127.0.0.1:5000` |
| Body | Optional data sent to the server | JSON data |

### HTTP methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Submit data or create a resource |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### Query parameters

Query parameters are placed after `?` in the URL.

```http
GET /add?a=10&b=20 HTTP/1.1
```

The query is:

```text
a=10&b=20
```

The parameters are separated by `&`.

Each parameter consists of a name and a value separated by `=`.

```text
a=10
b=20
```

Query parameters are not HTTP headers. They are part of the request URI.

---

## 2. HTTP Response Structure

An HTTP response is sent from a server back to a client.

### General structure

```http
HTTP/version Status-Code Reason-Phrase
Header-Name: Header-Value
Header-Name: Header-Value

Optional Response Body
```

### Example: JSON response

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13

{"result":30}
```

### Response components

| Component | Meaning | Example |
|---|---|---|
| HTTP version | Protocol version | `HTTP/1.1` |
| Status code | Result of the request | `200` |
| Reason phrase | Human-readable status description | `OK` |
| Headers | Additional response information | `Content-Type` |
| Body | Data returned to the client | `{"result":30}` |

### Common status codes

| Code | Meaning |
|---|---|
| 200 | OK — request succeeded |
| 201 | Created — resource created |
| 204 | No Content — successful, no response body |
| 400 | Bad Request — invalid request |
| 404 | Not Found — resource not found |
| 500 | Internal Server Error — server-side failure |

---

## 3. HTTP Headers

Headers provide additional information about the request or response.

### Common headers

| Header | Purpose |
|---|---|
| Host | Identifies the requested host |
| Content-Type | Specifies the media type of the body |
| Content-Length | Specifies the body length in bytes |
| Accept | Specifies acceptable response media types |
| Authorization | Provides authentication credentials |

### Example

```http
Content-Type: application/json
Content-Length: 13
```

`Content-Type` tells the receiver how to interpret the body.

`Content-Length` specifies how many bytes are in the body.

Headers are separated from the body by an empty line.

---

## 4. HTTP Request and Response Example

Suppose a Python client requests an addition operation from a Java server.

### Request

```http
GET /add?a=10&b=20 HTTP/1.1
Host: 127.0.0.1:5000
Accept: application/json

```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13

{"result":30}
```

### Communication flow

```text
Python Client
     |
     | HTTP Request
     | GET /add?a=10&b=20
     v
Java HTTP Server
     |
     | Extract a = 10
     | Extract b = 20
     | Calculate result = 30
     |
     | HTTP Response
     | {"result":30}
     v
Python Client
```

---

## 5. Accessing HTTP Components in Java

Java's `HttpExchange` provides methods to access the request and construct the response.

### Request

```java
String method = exchange.getRequestMethod();

String path = exchange.getRequestURI().getPath();

String query = exchange.getRequestURI().getQuery();

Headers headers = exchange.getRequestHeaders();

InputStream body = exchange.getRequestBody();
```

| Java method | Retrieves |
|---|---|
| `getRequestMethod()` | HTTP method |
| `getRequestURI()` | Request URI |
| `getRequestURI().getPath()` | Request path |
| `getRequestURI().getQuery()` | Query parameters |
| `getRequestHeaders()` | Request headers |
| `getRequestBody()` | Request body as bytes |

### Response

```java
exchange.getResponseHeaders()
    .set("Content-Type", "application/json");

exchange.sendResponseHeaders(200, responseBytes.length);

try (OutputStream os = exchange.getResponseBody()) {
    os.write(responseBytes);
}
```

| Java method | Purpose |
|---|---|
| `getResponseHeaders()` | Access response headers |
| `sendResponseHeaders()` | Send status code and response headers |
| `getResponseBody()` | Obtain output stream for response body |
| `OutputStream.write()` | Write response bytes |

---

## 6. HTTP, JSON, and Bytes

These are three different concepts.

| Concept | Responsibility |
|---|---|
| HTTP | Defines how requests and responses are structured |
| JSON | Defines the structure of data |
| Bytes | Represent the actual data transmitted |

Example JSON:

```json
{"result":30}
```

Java represents this as a string:

```java
String response = "{\"result\":30}";
```

The string is converted to bytes:

```java
byte[] responseBytes =
    response.getBytes(StandardCharsets.UTF_8);
```

The bytes are written to the HTTP response:

```java
os.write(responseBytes);
```

The receiver decodes the bytes back into text.

---

## 7. HTTP and Transport Protocols

HTTP operates at the application layer.

```text
Application Layer: HTTP
Transport Layer:   TCP or UDP-based transport
Network Layer:     IP
Link Layer:        Ethernet / Wi-Fi
```

Common HTTP versions:

| HTTP version | Transport |
|---|---|
| HTTP/1.1 | TCP |
| HTTP/2 | TCP |
| HTTP/3 | QUIC over UDP |

When using a high-level HTTP API, the underlying transport is handled by the HTTP implementation.

---

## Key Takeaways

- A request is sent from a client to a server.
- A response is sent from a server to a client.
- The start line identifies the request or response.
- Headers provide additional information.
- The empty line separates headers from the body.
- The body contains optional data.
- HTTP defines the message structure.
- JSON defines the data format.
- Bytes are used to transmit the data.
- Java's `HttpExchange` provides access to the request and response.
