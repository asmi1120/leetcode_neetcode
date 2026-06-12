class Solution:
    def calculate(self, s: str) -> int:
        s += '+'  # Dummy character to process the last number
        total = 0
        last_term = 0
        current_num = 0
        op = '+'

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch != ' ':
                # Process the previous operator
                if op == '+':
                    total += last_term
                    last_term = current_num
                elif op == '-':
                    total += last_term
                    last_term = -current_num
                elif op == '*':
                    last_term = last_term * current_num
                elif op == '/':
                    # Int division that truncates toward zero
                    last_term = int(last_term / current_num)
                
                # Reset for the next number
                op = ch
                current_num = 0

        return total + last_term

        