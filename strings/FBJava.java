
class Solution {
    public static void fizzBuzz(int number) {
        String[] lst = {"Fizz", "Buzz", "FizzBuzz"};

        System.out.println(
            number % 15 == 0 ? lst[2] :
            number % 3 == 0 ? lst[0] :
            number % 5 == 0 ? lst[1] :
            number
        );
    }
}
