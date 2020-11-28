
import sys

def price(call_len, max_t, price_interval):
    return price_interval * (1 + call_len*max_t)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for n in range(N):
        sys.stdin.readline()
        call = [int(x) for x in sys.stdin.readline().split()]

        cost_m = sum([10*(1+c//30) for c in call])
        cost_j = sum([15*(1+c//60)for c in call])
        best_price = min(cost_m, cost_j)
        best_com =[]
        if cost_m <= cost_j:
            best_com.append("Mile")
        if cost_j <= cost_m:
            best_com.append("Juice")
        best_com_name = " ".join(best_com)

        print("Case {}: {} {}".format(n+1, best_com_name, best_price))
