class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def remove_duplicates(head):
    if not head:
        return head

        seen = set()
        current = head
        seen.add(current.val)

        while current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next

        return head

#function aux para imprimir la lista
def print_list(head):
    current = head
    while current:
        print(current.val, end=" ->")
        current = current.next
    print("None")

#Ejemplo de us
# Crear la lista: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

print("Lista original:")
print_list(head)

head = remove_duplicates(head)

print("Lista sin duplicados:")
print_list(head)