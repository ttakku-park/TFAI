class InventoryAllocator :
    def inventory_forwarding(order, warehouse):

        result = []

        a = list(warehouse)
        order_item = list(order.keys())
        fruit_dict = {}

        for obj in warehouse : 
            warehouse_item = obj["inventory"]
            for f in order_item :
                if warehouse_item[f] >= order[f] :
                    
                    fruit_dict[f] = order[f]
                    a = {obj["name"]:fruit_dict}
                    result.append(a)
                    # fruit_dict.clear()
                    continue

                if warehouse_item[f] < order[f] :
                    fruit_dict[f]=warehouse_item[f]
                    order[f] = order[f]-warehouse_item[f]
                    b = {obj["name"]:fruit_dict}
                    result.append(b)
                    # fruit_dict.clear()
                    continue

                    
        return result

    order = { "apple": 10 }
    warehouse = [{ "name": "owd", "inventory": { "apple": 10 }},{ "name": "md", "inventory": { "apple": 10 }}]

    print(inventory_forwarding(order, warehouse))

# Input: { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }] Output: [{ owd: { apple: 1 } }]

# Input: { apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]
# Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]