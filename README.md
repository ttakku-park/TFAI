### TFAIsolutions
---
✔️ 정상적인 값 이외의 값이 들어왔을 때의 다양한 예외경우에 초점을 두어 로직 구현.


1. 주문값이 비었을 때, 주문이 들어오지않으면 결과값을 기대 할 수 없으므로 message 반환
```
if len(order) <= 0 :
            return "주문물량이 없습니다."
```
2. 창고값이 비었을 때, 주문과 마찬가지로 결과값을 기대 할 수 없으므로 message 반환 & 수용할 수 있는 창고 공간이 없을 때 

```
for fruit in order_fruit :

            if fruit in warehouse_count :
                if order[fruit] > warehouse_count[fruit] :
                    return f"창고에 {fruit}를 저장할 수 없습니다.(창고수용량보다 주문수가 많습니다.)"
            else : 
                return f"창고에 {fruit}를 저장할 수 없습니다.(해당 주문과일을 수용할 창고가 존재하지않습니다.)"

```
+ `warehouse_count` 에 모든창고의 과일마다의 수용량을 더한 총 창고 수용량을 저장하여 주문수량과 비교.
#### `warehouse_count`
```
for obj in warehouse : 
            warehouse_inven = obj["inventory"]
            warehouse_fruit = list(warehouse_inven.keys())
            
            for i in warehouse_fruit :
                if i in warehouse_count :
                    warehouse_count[i] +=  warehouse_inven.get(i)
                else :
                    warehouse_count[i] = warehouse_inven.get(i)
        
```
