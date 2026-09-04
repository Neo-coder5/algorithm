class LinearSearch:
    def find_number(self, n):
        for i in range(1, n+1):
            print(i)
            ans = str(input("thinking number y/n: "))
            if ans == 'y':
                print("Win!")
                return i
            elif ans == 'n':
                print("Not found")
sol = LinearSearch()
print(sol.find_number(10))


