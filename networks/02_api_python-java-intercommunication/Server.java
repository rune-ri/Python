// I first need to familiarize myself with working with  networks on java.
// I have found a new thing, apparently if i work using http server then i dont need 
//    to decide a transport protocol isnce that is handled behind automatically 
//    This is because i am working with applciation layer for now, this is a bit dfferent
//    from the trannsport layer coding i did before which was socket programming.

import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.io.OutputStream;
// 1. javas builtin http server implementation. 
//    to note that htis is good for learning and small thigns but not prefered for larger implementation.
// 2. this is to create the ip address and its host name. its like a tuple of it with most likley supporting functions.
// 3. its for writing bytes to destination. so it can write to network, json or anything else.

// The client side imports are differnt though. this is server side imports.

public class Server{
  public static void main(String[] args) throws Exception{
    HttpServer server = HttpServer.create(new InetSocketAddress("127.0.0.1", 5001), 0);
    // i need to know what 0 is over there, i know about inet socket address, but i dont know what 0 mreans.

    // this is gonna be really confusing.
    server.createContext("/add", exchange ->{
      // Basically if /add then implement the following. lambda function.
      // what is exchange it is the complete container for http exchange.
      // does this mean that everytime in java we do network http communication, we do it in exchange with 
      //    putting it into for loops to make the thing go on forever on a server?
      String query = exchange.getRequestURI().getQuery();
      // the request line of python would look like this:
      // GET /add?a=10&b=20 HTTP/1.1
      // then .getRequestURI() is for /add?a=10&b=20 and the .getQuery() is for a=10&b=20.
      // does this mean each part of the request beign received or requested has its own field names and such? to refer to directly?
      // URI full form is Uniform resource identifier. 
      // URL ie uniform resource locator and URN ie uniform resrouce names are types of URI.

      String[] numbers = query.split("&");
      // after this we need to split the query part into the inputs we need which is a=10 and b=20. we use .split("&")
      // we also define the parameter around which we split. which here is &.

      int a = Integer.parseInt(numbers[0].split("=")[1]);
      int b = Integer.parseInt(numbers[1].split("=")[1]);
      // then we store the values that we have split into variables. and since we only want the numbers not variables, 
      //    we also split with = as centre and then take the first index which would be the number.

      int result = a + b;
      // add.

      String response = "{\"result\":" + result + "}";
      // json string creation, since json string is exchanged. most likely this means taht we use loads and dumps.
      // we need the backslash to skip/escape so that we can input " as the input

      exchange.getResponseHeaders().set("Content-Type", "application/json");
      // the resopnse message has 3 parts.
      // 1. status line ie the first line.
      // 2. the resonse header with metadata. 
      // 3. message body with the actual data.
      // the first is compulsory.
      // second and third are not compurlsory but there are norms to put spome things. 
      //
      // Here we set the Content-Type as application/json so that the receiver has a heads up on what to do. 
      // this is like a configuration. as soon as the input is there in the response, the receiver can configure 
      //    their own code to work only on that type of data instead.

      exchange.sendResponseHeaders(200, response.getBytes().length);
      // this is the response status 200 i think, to say that it worked?
      // and the bit size for checksum?
      // and also for proper reconstuction so that it knows if there is a problem and may ask for a fix or a retransmission.

      try(OutputStream os = exchange.getResponseBody()){
        // this is wehre the actual response is generated. 
        // first get the output streem connected to http response body.
        os.write(response.getBytes());
        // this turns the resopnse string into bytes and those bytes are written. 
        // this method of try is called `try with resources` which means it closes
        // http sends data as bytes so we need to do this everytime.
      }
    });
    server.start();
    // this is what actually starts the server. on exchange deals only with one interaction. you do not loop the excahnge, 
    // you loop this server start i think
    System.out.println("Server running on port 5001.");
  }
}
