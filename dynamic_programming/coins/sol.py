

def coinsHelper(n, curr_res, total_res, baseCoin):
  if n < 0 or len(baseCoin) == 0:
    return
  if n == 0:
   total_res.append(curr_res)
   return 
  
  coinsHelper(n, curr_res, total_res, baseCoin[1:])
  coinsHelper(n - baseCoin[0], [baseCoin[0]] + curr_res, total_res, baseCoin)

def coins(n):
  baseCoin = [25, 10, 5, 1]
  curr_res = []
  total_res = []
  coinsHelper(n, curr_res, total_res, baseCoin)
  return total_res
  

if __name__ == "__main__":
  n = 8
  #coins(n)
  print len(coins(n))
  
  n = 30
  print len(coins(n))