class node(object):
    "sebuah simpul linked list"
    def __init__ (self, data, next=None):
        self.data = data
        self.next = next

class linkedList(object):
    def __init__ (self, head=None):
        self.head = head

    def kunjungi(self, head):
        curNode = head
        while curNode is not None :
            print(curNode.data)
            curNode = curNode.next

    #menyisipkan node baru
    def sisip(self, before, newNode ):
        newNode.next = before.next
        before.next = newNode

    #menghapus node
    def hapus(self, hps):
        
        key = self.head
        #jika node yg dihapus merupakan head
        if(key is not None):
            if (key == hps):
                self.head = key.next
                key= None
                return

        while key is not None:
            if key == hps :
                break
            prev = key
            key = key.next

        if key==None :
            return

        prev.next = key.next

        temp = None

a = node(50)
b = node(42)
c = node(44)
d = node(11)
e = node(33)


a.next = b
b.next = c
c.next = d
d.next = e

llist = linkedList()
llist.head = a
llist.kunjungi(a)

#menyisipkan node baru
f = node(99)
print('menambahkan node baru x antara node b dan c :')
llist.sisip(b, f)
llist.kunjungi(a)

#menghapus node c
print('menghapus isi dari c')
llist.hapus(c)
llist.kunjungi(a)
