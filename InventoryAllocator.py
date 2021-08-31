class InventoryAllocator(object) :
    def inventory_forwarding(order, warehouse):
        # 주문물량 여부확인
        if len(order) <= 0 :
            return "주문물량이 없습니다."

        # 창고수량 합계
        warehouse_count = {}
        for obj in warehouse : 
            warehouse_inven = obj["inventory"]
            warehouse_fruit = list(warehouse_inven.keys())
            
            for i in warehouse_fruit :
                if i in warehouse_count :
                    warehouse_count[i] +=  warehouse_inven.get(i)
                else :
                    warehouse_count[i] = warehouse_inven.get(i)
        
        order_fruit = list(order.keys())
        
        # 창고수용합계와 주문수량 검사 | 1. 창고수용량 < 주문량 -> return message 2. 주문과일 재적창고 미존재시 return message
        for fruit in order_fruit :

            if fruit in warehouse_count :
                if order[fruit] > warehouse_count[fruit] :
                    return f"창고에 {fruit}를 저장할 수 없습니다.(창고수용량보다 주문수가 많습니다.)"
            else : 
                return f"창고에 {fruit}를 저장할 수 없습니다.(해당 주문과일을 수용할 창고가 존재하지않습니다.)"

        warehouse_dict = {}
        for section in warehouse :
            warehouse_name  = section["name"]
            warehouse_inven = section["inventory"]

            for fruit in order_fruit : 

                if not warehouse_name in warehouse_dict :
                    warehouse_dict[warehouse_name] = {}

                if warehouse_inven[fruit] >= order[fruit] :
                    warehouse_dict[warehouse_name][fruit] = order[fruit]
                    order[fruit] = 0

                elif warehouse_inven[fruit] < order[fruit] :
                    warehouse_dict[warehouse_name][fruit] = warehouse_inven[fruit]
                    order[fruit] -= warehouse_inven[fruit]
                
        return [warehouse_dict]

    