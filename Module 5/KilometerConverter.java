/*****
* Author: Glowstudent
* Program: Kilometer Converter
*****/

import java.util.Scanner;

public class KilometerConverter {

    static float convertToMiles(float km) {
        return km * 0.6214f;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        float km;
        float miles;

        System.out.print("Enter the number of kilometers to convert to miles: ");
        km = sc.nextFloat();

        miles = convertToMiles(km);

        System.out.printf("%s kilometers is approximately %.4g miles.", km, miles);
    }
}