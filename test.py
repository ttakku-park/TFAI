import unittest
import InventoryAllocator

class Test_InventoryAllocator(unittest.TestCase):

    def test_A(self) :
        order = { "apple":12 , "banana":1}
        warehouse = [{ "name": "owd", "inventory": { "apple":15,"banana":1}},{ "name": "dm", "inventory": { "apple":6,"banana":1}}]
        result = [{'owd': {'apple': 12, 'banana': 1}, 'dm': {'apple': 0, 'banana': 0}}]
        self.assertAlmostEqual(InventoryAllocator.InventoryAllocator.inventory_forwarding(order,warehouse),result)

    def test_B(self) :
        order = { "apple":5 , "banana":5,"orange":5}
        warehouse = [{ "name": "dm", "inventory": { "apple":0 , "banana":5,"orange":2}},{ "name": "owd", "inventory": { "apple":5 , "banana":5,"orange":5}}]
        result = [{'dm': {'apple': 0, 'banana': 5, 'orange': 2}, 'owd': {'apple': 5, 'banana': 0, 'orange': 3}}]
        self.assertAlmostEqual(InventoryAllocator.InventoryAllocator.inventory_forwarding(order,warehouse),result)
    # 창고가 없을때
    def test_C(self) : 
        print("창고가 존재하지 않는경우")
        order = { "apple":5 , "banana":5,"orange":5}
        warehouse = []
        result = "창고에 apple를 저장할 수 없습니다.(해당 주문과일을 수용할 창고가 존재하지않습니다.)"
        self.assertAlmostEqual(InventoryAllocator.InventoryAllocator.inventory_forwarding(order,warehouse),result)
    # 창고수용량보다 주문량이 많을때 
    def test_D(self) :
        print("창고수용량보다 주문량이 많을 경우1")
        order = { "apple":5 , "banana":5,"orange":5}
        warehouse = [{ "name": "dm", "inventory": { "apple":0 , "banana":0,"orange":0}}]
        result = "창고에 apple를 저장할 수 없습니다.(창고수용량보다 주문수가 많습니다.)"
        self.assertAlmostEqual(InventoryAllocator.InventoryAllocator.inventory_forwarding(order,warehouse),result)

    def test_E(self) : 
        print("창고수용량보다 주문량이 많을 경우2")
        order = { "apple":5 , "banana":6,"orange":7}
        warehouse = [{ "name": "owd", "inventory": { "apple":1 , "banana":5,"orange":2}},{ "name": "dm", "inventory": { "apple":5 , "banana":5,"orange":0}}]
        result = "창고에 orange를 저장할 수 없습니다.(창고수용량보다 주문수가 많습니다.)"
        self.assertAlmostEqual(InventoryAllocator.InventoryAllocator.inventory_forwarding(order,warehouse),result)
    #주문물량이 없을때
    def test_F(self) : 
        print("주문물량이 없을 경우")
        order = {}
        warehouse = [{ "name": "owd", "inventory": { "apple":1 , "banana":5,"orange":2}},{ "name": "dm", "inventory": { "apple":5 , "banana":5,"orange":0}}]
        result = "주문물량이 없습니다."

if __name__ == '__main__' :
    unittest.main()
