#no3

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    #menambahkan simpul diawal
    def tambahDepan(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    #menambahkan simpul diakhir
    def tambahAkhir(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    #menyisipkan simpul sesuai posisi 
    def tambahNode(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            node.next = prev.next
            prev.next = node
        return self.head
    #menghapus simpiul sesuai posisi
    def hapusNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position ):
            prev = temp
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        prev.next = temp.next
        temp= None 
    #mencari data yang dicari
    def cari(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    #mencetak seluruh isi node
    def cetak(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   

llist = LinkedList() 
llist.tambahDepan(21)
llist.tambahDepan(22)
llist.tambahDepan(12)
llist.tambahDepan(14)
llist.tambahDepan(2)
llist.tambahDepan(19)
llist.tambahAkhir(9)
llist.cetak()
print(llist.cari(21))

llist.tambahNode(10,5)
llist.cetak()
llist.cari(21)
print(llist.cari(10))

llist.hapusNode(6)
llist.cetak()

llist.cari(21)
llist.cari(10)
