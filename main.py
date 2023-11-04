import pandas as pd

table = pd.DataFrame([
    ["+","-","-","-","-","-","+"],
    ["|"," ","|"," ","|"," ","|"],
    ["|","-","+","-","+","-","|"],
    ["|"," ","|"," ","|"," ","|"],
    ["|","-","+","-","+","-","|"],
    ["|"," ","|"," ","|"," ","|"],
    ["+","-","-","-","-","-","+"]])

tmp_table=table.copy()

def check(mark):
  chk = 0
  for i in range(7):
    #　行方向のチェック
    tmp =(tmp_table.iloc[i,:]==mark).sum()
    if chk<tmp:
      chk = tmp

    #　列方向のチェック
    tmp =(tmp_table.iloc[:,i]==mark).sum()
    if chk<tmp:
      chk = tmp

  # 斜めのチェック
  if (tmp_table.iloc[1,1]==mark)&(tmp_table.iloc[3,3]==mark)&(tmp_table.iloc[5,5]==mark):
   return 3

  if (tmp_table.iloc[1,3]==mark)&(tmp_table.iloc[3,3]==mark)&(tmp_table.iloc[5,1]==mark):
   return 3

  return chk

def point(mark,n):

  row = input("縦の座標を1,3,5で入力してください ")
  col = input("横の座標を1,3,5で入力してください ")
  if int(row) in [1,3,5]:
    if int(col) in [1,3,5]:

      if (tmp_table.iloc[int(row),int(col)]=="X")|(tmp_table.iloc[int(row),int(col)]=="O"):
        print("ほかの場所に入力してください")
        return n
      else:
        tmp_table.iloc[int(row),int(col)]=mark
        return n+1
    else:
      print("1,3,5のうちから入力してください")
      return n
  else:
      print("1,3,5のうちから入力してください")
      return n

n = 0
check_point = 0
print(tmp_table)

while (check_point<3)|(n==9):

  if n%2 ==0:
    mark="O"
  else:
    mark="X"
  n = point(mark,n)
  check_point = check(mark)
  if check_point == 3:
    print(f"{mark} is WIN!!!\n")
  print(tmp_table)

  if n == 9:
    print("Draw!")
    break