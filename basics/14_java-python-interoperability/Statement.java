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

  public static void main(String[] args){
    int number = Integer.parseInt(args[0]);

    System.out.println(statement(number));
  }
}
