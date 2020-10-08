#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #初始化一個節點，temp與head都指向該節點，但是temp需要不斷擴充套件，因為明顯結果不是一個節點能完成的。然後head.next就是我們要返回的頭結點地址了。因為head本身是儲存的0,它的next才是我們想要的第一個有用的數所在的地方。
        temp = ListNode(0)
        head = temp
        #sum是l1,l2對應位相加的和，例如2+3=5。那麼temp就存5。也可能是7+8=15,那麼sum%10的數，即餘數就是temp。商為1，被sum儲存進入下一次迴圈，也就是下一位相加，例如下一位原來是3+4，但是這裡有個進位1，就變成了3+4+1。之後不斷迴圈即可。
        sum = 0
        #只要l1,l2或者sum有值就迴圈加。l1,l2=None,即說明到了連結串列尾部了。sum=0就說明最後一位沒有進位了，合在一起是跳出來迴圈的條件
        while l1!=None or l2!=None or sum!=0:
        #只要l1，l2還有值，就加給sum。然後l1,l2往後走一步。
            if l1!=None:
                sum+=l1.val
                l1 = l1.next
            if l2!=None:
                sum+=l2.val
                l2 = l2.next
              #a:餘數。sum:商。也可寫成：sum,a=divmod(sum,10)
              # divmod() 函式把除數和餘數運算結果結合起來，返回一個包含商和餘數的元組(a // b, a % b)。
            a = sum%10
            sum = sum//10
            #就是程式開頭的0節點後面就是和的第一位了
            temp.next = ListNode(a)
            #之後就開始進行ListNode(0).next.next的計算了
            temp =temp.next
            #返回ListNode(0)的下一個節點，因為那是和的第一位。
        return head.next
# @lc code=end

