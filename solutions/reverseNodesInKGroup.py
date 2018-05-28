from data_struct import ListNode

def reverseKGroup_Recur(head, k):
  tail = head
  cnt = 0
  while (tail and cnt < k):
    tail = tail.next
    cnt += 1

  if cnt < k:
    return head
  else:
    tail = reverseKGroup_Recur(tail, k)
    while (cnt > 0):
      tmp = head.next
      head.next = tail
      tail = head
      head = tmp
      cnt -= 1
    return tail


def reverseKGroup_Iter(head, k):
  dmy = ListNode(-1)
  dmy.next = head
  tmp_pre = dmy

  while (head):
    tail = head
    cnt = 0
    while (tail and cnt < k):
      tail = tail.next
      cnt += 1
      
    if cnt < k:
      tmp_pre.next = head
      head = tail
    else:
      pre = head
      while (cnt > 0):
        tmp = head.next
        head.next = tail
        tail = head
        head = tmp
        cnt -= 1
      tmp_pre.next = tail
      tmp_pre = pre
  return dmy.next

def createLL(n):
  head = None
  i = n
  while (i > 0):
    tmp = ListNode(i)
    tmp.next = head
    head = tmp
    i -= 1
  return head

def readLL(head):
  mark = head
  repr_str = "["
  while (mark):
    repr_str += str(mark.val)
    mark = mark.next
    if mark:
      repr_str += ","
  
  repr_str += "]"
  return repr_str

if __name__ == '__main__':
  head = createLL(5)
  print (readLL(head))  
  rhead = reverseKGroup_Recur(head, 2)
  print ("recur", 2, readLL(rhead))
  rhead = reverseKGroup_Iter(rhead, 4)
  print ("iter", 4, readLL(rhead))
