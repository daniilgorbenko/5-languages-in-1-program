package pkg_java;
import java.util.*;
public class JavaPrime {


    public static void main(String[] args) {

        boolean rez = is_prime_ferma(3574);
        System.out.println(rez);
    }

    public static boolean is_prime_ferma(int number){
        List<Integer> rnd_list = new ArrayList<Integer>();
        int rnd_value;
        boolean is_prime = true;
        while (rnd_list.size() < 20){
            rnd_value = get_rnd_value(number+1, number+100000);
            if ((number % rnd_value != 0) && !rnd_list.contains(rnd_value)){
                rnd_list.add(rnd_value);
            }
        }
        for (int rnd_number : rnd_list) {
            if (mod_pow(rnd_number, number-1, number) != 1){
                is_prime = false;
                break;
            }
        }
        return is_prime;
    }

    public static int get_rnd_value(int min, int max){
        return (int)Math.floor(Math.random()*(max-min+1)+min);
    }

    public static long mod_pow(long a, long b, int m) {
        a %= m;
        if (b == 0) return 1;
        else if (b % 2 == 0) {
            return mod_pow((a * a) % m, b / 2, m);
        }
        else return (a * mod_pow(a, b - 1, m)) % m;
    }

}








































