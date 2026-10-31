import java.util.List;

public class Statement{
  public static String statement(int number){
    List<String> statements = List.of(
        
            "Growth requires consistency.",
            "Calmness creates awareness.",
            "Curiosity drives learning.",
            "Perseverance creates progress.",
            "Presence requires attention."
        );
    if(number <0 || number >= statements.size()){
      return "Invalid number input";
    }

    return statements.get(number);
  }
  // i was going to make the initial one main itself, but i thought lets make it simpler for 
  // now, calls are easier with main separate.

  public static void main(String[] args){
    int number = Integer.parseInt(args[0]);
    // i was going to merge this directly into one statement, but i saw onlien that it would 
    // become too long, need to make things short and easy to understand

    System.out.println(statement(number));
    // i just need to somehow send the output to stdout. which python can then pick up, so print is enough.
  }
}
