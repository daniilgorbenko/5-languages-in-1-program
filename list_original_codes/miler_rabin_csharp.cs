using System;
using System.Numerics;

namespace is_prime_csharp
{
    public class miler_rabin_csharp
    {
    
        public static bool test_miler_rabin(int n)
        {

            if (n == 2 || n == 3) {
                return true;
            }
            if (n < 2 || n % 2 == 0) {
                return false;
            }
            // we represent n - 1 in the form (2 ^ s) t, where t is odd, this can be done by sequentially dividing n - 1 by 2 
            int t = n - 1;
            int s = 0;
            while (t % 2 == 0) {
                t = t / 2;
                s++;
            }
            Random rnd = new Random();
            // let's take 8 rounds to determine the prime of a number. 
            for (int i= 0; i < 8; i++) {

                int a = rnd.Next(2, n-2);
                // x ← a ^ t mod n, we calculate using the exponentiation modulo
                int x = (int)BigInteger.ModPow(a, t, n);
                if (x == 1 || x == n - 1) {
                    continue;
                }

                for (int j = 0; j < s - 1; j++) {
                    // x ← x^2 mod n
                    x = (int)BigInteger.ModPow(x, 2, n);
                    // if x == 1 then return "compound" 
                    if (x == 1) {
                        return false;
                    }
                    // if x == n - 1, then go to the next iteration of the outer loop 
                    if (x == n - 1) {
                        break;
                    }

                }

                if (x != n - 1) {
                    return false;
                }

            }
            // return "probably simple" 
            return true;

        }


    }
}
