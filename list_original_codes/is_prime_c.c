#include <stdbool.h>
#include <math.h>

bool is_prime_sqrt(int number){
	
	bool prime = true;
	
	if (number == 1 || (number%2 == 0)){
		prime = false;
	}
	else{
		for (int i=2; i<=sqrt(number);i++){
			if (number%i == 0){
				prime = false;
				break;
			}
		}
	}
	return prime;
}