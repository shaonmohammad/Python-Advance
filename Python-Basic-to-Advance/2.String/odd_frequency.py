#---------------------Odd Frequency Characters---------------------------
if __name__ == "__main__":
    input_str = list(map(str,input()))
    odd_exist = [i for i in input_str if input_str.count(i)%2!=0]
    print(odd_exist)

