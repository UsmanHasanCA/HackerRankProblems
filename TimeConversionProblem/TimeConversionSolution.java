import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static String timeConversion(String s) {
        
        //checks if the time is XX:XX:XX AM and that its not 12:XX:XX AM and returns the given string if so.
        if(s.contains("A") && s.charAt(0) != '1' && s.charAt(1) != '2')
            return s.substring(0, s.length()-2);
        
        //checks if the time is AM and it is 12:XX:XX AM, if so returns 12 as 00:XX:XX
        if(s.contains("A") && s.charAt(0) == '1' && s.charAt(1) == '2'){
            String midnight = "00" + s.substring(2, s.length()-2);
            return midnight;
        }
        
        //This section only runs if the time that was given is a PM time
        //takes the integer value of the first two characters of the given string
        int n = Integer.valueOf(s.substring(0, 2));
        
        //if the first 2 characters of the string (int n) are 12 then we just return the string that was given without the PM
        if(n == 12)
            return s.substring(0, s.length()-2);
        
        //otherwise add 12 to integer n
        n += 12;
        
        //concatenate the altered hour value with the remainder of the time that was given
        String output = String.valueOf(n) + s.substring(2, s.length()-2);
        
        //returns 24 hour value of given time.
        return output;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        String result = timeConversion(s);
        System.out.println(result);
    }
}
