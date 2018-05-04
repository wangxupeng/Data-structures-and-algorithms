# 链表
## 为什么需要链表
顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，所以使用起来并不是很灵活。

链表结构可以充分利用计算机内存空间，实现灵活的内存动态管理。

## 链表的定义
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是不像顺序表一样连续存储数据，而是在每一个节点（数据存储单元）里存放下一个节点的位置信息（即地址）。

![](../PIC/chapter3/chapter3-1.png)

# 单向链表
单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

![](../PIC/chapter3/chapter3-2.png)

*  表元素域elem用来存放具体的数据。
*  链接域next用来存放下一个节点的位置（python中的标识）
*  变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。

## 节点实现

``` py
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
```
## 单链表的操作
*  is_empty() 链表是否为空
*  length() 链表长度
*  travel() 遍历整个链表
*  add(item) 链表头部添加元素
*  append(item) 链表尾部添加元素
*  insert(pos, item) 指定位置添加元素
*  remove(item) 删除节点
*  search(item) 查找节点是否存在
## 单链表的实现
``` py
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print cur.item,
            cur = cur.next
        print ""
```
### 头部添加元素

![](../PIC/chapter3/chapter3-3.png)
``` py
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node
```
