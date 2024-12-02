class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return convert(num).strip()
        
    
    
def convert(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    
    if num < 10:
        return ones[num]
    
    elif num < 20:
        return teens[num - 10]
    
    elif num < 100:
        return tens[num // 10] + " " +  convert(num % 10)
    
    elif num < 1000:
        return convert(num // 100) +" Hundred " +convert(num % 100)
    elif num < 1000000:
        return convert(num // 1000)+" Thousand " + convert(num % 1000)
    
    elif num < 1000000000:
        return convert(num // 1000000) + " Million " + convert(num % 1000000)
    
    else:
        return convert(num // 1000000000) + " Billion " + convert(num % 1000000000)
    
