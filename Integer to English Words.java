class Solution {

    String[] ones = {"", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"};
        String[] tens = {"", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"};
        String[] thousands = {"", " Thousand", " Million", " Billion"};

    public String toWords(int n) {
        if (n < 20) {
            return ones[n];
        }
        if (n < 100) {
            return tens[n/10] + toWords(n % 10);
        }
        if (n < 1000) {
            return toWords(n / 100) + " Hundred" + toWords(n % 100);
        }
        for (int i = 3; i >= 0; i--) {
            if (n >= Math.pow(1000, i)) {
                return toWords((int)(n / Math.pow(1000, i))) + thousands[i] + toWords((int)(n % Math.pow(1000, i)));
            }
        }
        return "";
    }

    public String numberToWords(int num) {
      if (num == 0) {
          return "Zero";
      }
      return toWords(num).substring(1);  
    };

}
