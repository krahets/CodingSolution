#### 1. 概述
1. Java集合框架提供了数据持有对象的方式，提供了对数据集合的操作，位于`java.util`包下，主要有三个大类：Collection（接口）、Map（接口）、集合工具类。
   1. **Collection**
      1. List
         1. ArrayList：线程不同步。默认初始容量为10，数组大小不足时扩充为1.5倍。为追求效率，未实现线程同步，如果需要多个线程并发访问，可以手动同步，或使用Vector代替。
         2. LinkedList：线程不同步。双向链接实现。同时实现了List接口和Deque接口，既可以看作一个顺序容器，又可以看作一个队列。
         4. Vector：线程同步。默认初始容量10，当数组大小不容时扩充为2倍，同是通过`Iterator`和`synchronized`实现的。
            1. Stack：线程同步。继承自Vector，添加了几个方法完成栈的功能。现在已经不推荐用Stack，栈和队列优先使用`ArrayDeque`，其次是`LinkedList`。
      2. Queue
         1. ArrayDeque：线程不同步，栈和队列优先选用。
         2. PriorityQueue：通过完全二叉树实现的小顶堆。不允许存入null元素。
      3. Set：不包含重复元素的Collection，Set最多存一个null元素，Set集合通常通过Map集合通过适配器模式得到。
         1. NavigableSet：添加了搜索功能，可以对给定元素进行搜索：<, <=, >, >=，放回一个符合条件的最接近给定元素的key。
            1. TreeSet：线程不同步。提供有序的Set集合，内部使用NavigableMap操作，默认元素“自然顺序”排列，可以通过`Comparator`改变排序。TreeSet里面有一个TreeMap(适配器模式)。
         2. HashSet：线程不同步。内部使用HashMap进行数据存储，和HashMap本质一样，集合元素可以为null。
         3. EnumSet：线程不同步。内部使用Enum数组实现，速度比HashSet快。只能存储再构造函数传入的枚举类枚举值。
   2. **Map**
      1. TreeMap：线程不同步。基于红黑树的NavigableMap实现，能够把它保存的记录根据键值排序，默认是按键值升序排序，用Iterator遍历TreeMap时，得到的记录是排序过的。
      2. HashTable：线程安全。HashTable中大部分方法都经过synchronized修饰，在同一时间仅有一个线程修改，因此效率低。不允许存储null值。
      3. HashMap：线程不同步。根据key的hashcode存储，默认大小16，每次扩大一倍，当发生hash冲突时，采用拉链法。Java 1.8后，当单个桶中的元素大于等于8时，链表改为红黑树实现，当元素小于6个时，改回链表实现。是HashTable的轻量级体现，可以存储null值。
      4. LinkedHashMap：记录了插入顺序，用Iterator遍历时，按照插入顺序输出。遍历比HashMap慢（当HashMap容量很大数据很小时比HashMap快）。
   3. 工具类：
      1. Collections, Arrays：集合类的一个工具帮助类，其中提供了一系列静态方法，对于集合元素进行排序、搜索及线程安全等各种操作。
      2. Comparable, Comparator：一般用于对象比较、实现排序，两者略有区别。

   4. 通用实现：
|       | Hash Table | Resizable Array | Balanced Tree | Linked List | Hash Table + Linked List |
| ----- | ---------- | --------------- | ------------- | ----------- | ------------------------ |
| Set   | HashSet    |                 | TreeSet       |             | LinkedHashSet            |
| List  |            | ArrayList       |               | LinkedList  |                          |
| Deque |            | ArrayDeque      |               | LinkedList  |                          |
| Map   | HashMap    |                 | TreeMap       |             | LinkedHashMap            |

#### 2. 深入源码分析

1. **ArrayList**
   1. 概览
      1. 实现了RandomAccess接口，因此支持随机访问，因为ArrayList是基于数组实现的。
      2. 数据默认大小为10。
   2. 序列化
      1. 保存元素的数组使用transient修饰，不会被序列化。ArrayList重写了writeObject()和readObject()来控制只序列化数组有元素填充的那部分内容。
   3. 扩容
      1. 每次扩容是原容量的1.5倍。
      2. 扩容操作需要调用Arrays.copyOf()把原数组整个复制到新数组中，本操作代价很高，因此最好提前指定大概的容量，减少扩容次数。
   4. 删除元素
      1. 需要调用System.arraycopy()将index+1后面的元素都复制到index上。
   5. Fail-Fast
      1. 在遍历一个集合时，当集合结构被修改，抛出Cocurrent Modification Exception；
      2. modCount用来记录ArrayList结构变化发生次数，设置元素值、添加删除元素、调整内部数组大小都不算做结构发生变化。
      3. 单线程环境：
         1. 集合创建后，在遍历过程中修改了结构；
         2. remove()会使expectModcount和modcount相等，所以不会抛出这个异常。
      4. 多线程环境：
         1. 当一个线程在遍历集合，另一个线程对这个集合进行修改。

2. **Vector**
   1. 同步
      1. 实现与ArrayList类似，但使用sychronized实现同步。
      2. ArrayList和Vector
         1. Vector是同步的，因此开销比ArrayList大，访问速度慢。
         2. 同步操作可以由程序员自己控制，因此尽量使用ArrayList。
         3. Vector每次扩容扩大至2倍，ArrayList是1.5倍。
      3. Vector替代方案
         1. 为了获得线程安全的ArrayList，可以使用Collections.synchronizedList()得到一个线程安全的ArrayList。
            ```java
            List<String> list = new ArrayList<>();
            List<String> symList = Collections.synchronizedList(list);
            ```
         2. 可以使用cocurrent并发包下的CopyOnWriteArrayList类。原理是不直接向当前List添加元素，而是先将当前容器进行Copy，复制出一个新的容器，然后向新的容器添加元素，然后再将原容器引用指向新的容器。是一种读写分离思想。
            1. 内存占用问题：两份对象内存；
            2. 数据一致性问题：只能保证数据最终一致性，无法保证实时一致性。
            ```java
            List<String> list = new CopyOnWriteArrayList<>();
            ```

3. **LinkedList**
   1. 概览
      1. LinkedList底层是基于双向链表实现。同时实现了List和Deque接口，可以看作顺序容器、队列、栈。
      2. 栈和队列首选ArrayDeque，比LinkedList有更好的性能。
      3. 内部使用Node来存储链表节点信息，每个链表存储Head和Tail指针。
   2. add()
      1. `add(E e)`：在LinkedList末尾插入元素，因为有last指向链表末尾，复杂度`O(1)`；
      2. `add(int index, E element)`：在指定下标插入元素，通过线性查找找到位置（从头端尾端哪个开始取决于条件`index < (size >> 1))`），修改相关引用完成插入操作。
   3. remove()
      1. `remove(Object o)`：删除与指定元素相等的元素；
      2. `remove(int index)`：删除指定下标的元素。
      3. 两个删除操作都要：先找到删除元素的引用（用的是元素的equals()方法），修改相关引用，完成删除操作。复杂度`O(N)`。
   4. get()
      1. `get(int index)`：通过比较index和链表中点距离来判断是从`head`正序找还是从`tail`倒序找，时间复杂度`O(N)`。

4. **HashMap**
   1. 存储结构
      1. 链地址法：数组和链表结合的形式。取元素的时候先通过hash计算得到数组下标，找到对应链表，再在链表中找到与key相同的节点，就能找到对应值了。
      2. JDK 1.8后，在hash冲突较多的情况下（此时查找的复杂度`O(N)`），在链表长度>8时，链表会被转化为红黑树（复杂度O(logN)），<6时还原为链表。
      3. 数据底层存储方式：`Node[] table`，即哈希桶数组，明显它是一个Node数组。
         ```java
         static class Node<K,V> implements Map.Entry<K,V> {
             final int hash;    //用来定位数组索引位置
             final K key;
             V value;
             Node<K,V> next;   //链表的下一个node

             Node(int hash, K key, V value, Node<K,V> next) { ... }
             public final K getKey(){ ... }
             public final V getValue() { ... }
             public final String toString() { ... }
             public final int hashCode() { ... }
             public final V setValue(V newValue) { ... }
             public final boolean equals(Object o) { ... }
         }
         ```
      4. 如果哈希桶数组很小，容易引起哈希碰撞；如果哈希桶数组很大，比较浪费空间。因此，带来了空间成本和时间成本的权衡问题。解决此问题有两种方式：Hash算法和扩容机制。
         1. Hash桶数组初始化容量capacity默认16，键值对超过threshold就扩容为原来的2倍。
            ```java
            int threshold; // 所能容纳的key-value对极限数量；threshold = capacity * loadFactor
            final float loadFactor; // 负载因子，默认0.75，时空间平衡的选择，不要轻易修改；内存空间富裕可以降低之，时间富裕可以提升之；
            int modCount; // 记录HashMap结构发生变化的次数；
            int size; // 实际存在的键值对数量。
            ```
         2. HashMap中哈希桶数组的`capacity = 2 ^ n`，这是一种非常规设计，因为桶的大小为素数时，导致冲突的概率比较低。Hashtable初始化桶的大小为11，就参照了这个特性。
   2. 重要参数
      | Parameter  | Description                                  |
      | ---------- | -------------------------------------------- |
      | buckets    |                                              |
      | capacity   | table容量大小，默认16，每次扩容×2            |
      | size       | table的实际使用量                            |
      | threshold  | 存储最多键值对数量，size临界值，超过必须扩容 |
      | loadFactor | 负载因子，threshold = capacity * loadFactor  |
   3. 确定哈希桶数组索引位置
      1. 计算hash值
      2. 取模（取余）：将key的hash值对桶的个数取模`hash % capacity`，如果能保证capacity为`2 ^ n`，则可以将取模运算转化为位运算。因为`y % x = y & (x - 1)`。
   4. 分析put()方法
      1. 判断hash桶数组是否为空或null，否则执行resize()进行扩容；
      2. 根据键值key计算hash值得到插入的数组索引i，若table[i] == null则直接添加节点，转至6.,否则转至3.
      3. 判断table[i]首个元素key是否一样，如果一样则覆盖，不一样则转向4.；
      4. 判断table[i]是否是TreeNode，若是则在树中插入键值对，若不是则转向5.；
      5. 遍历table[i]，判断链表长度是否大于8，若大于则转化为红黑树，在红黑树中插入，否则执行链表插入；遍历过程中若发现key已存在则直接覆盖value。
      6. 插入成功后，判断实际存在的键值对数量size是否超过了最大容量threshold，若超过则扩容。
   5. 扩容机制
      1. 扩容后，需要将原Hash桶中元素转入新Hash桶中，这里牵扯到新index!=旧index的问题：
      2. 由于扩容2倍，新的x-1相当于高位多了一个1，我们只用检查每个键值对的hash值在此位是1 or 0，若是0则index不变，若是1则为index += old_capacity。
   6. 线程安全性
      1. 多线程下，尽量使用线程安全的CocurrentHashMap，避免使用线程不安全的HashMap；
      2. HashMap多线程访问时可能会出现环装链表，导致无限循环的情况。

5. **CocurrentHashMap**
   1. 存储结构：
      1. 主干是一个Segment数组。和HashMap实现类似，主要差别是采用了分段锁。
      2. 每个分段锁维护着几个桶，多个线程可以同时访问不同分段锁上的桶，从而使并发度更高（并发数就是Segment的数量）。
   2. Size()
      1. 每个Segment维护count统计该Segment的键值对数量。
      2. 执行size()操作时，需遍历所有Segment并将count累加起来。
   3. 同步方式
      1. 读操作：获取key所在的Segment时需保证其可见性。具体实现上使用volatile关键字或锁，锁开销太大，volatile也有一定开销。
      2. 写操作：根据key获取对应Segment的锁，然后就像普通HashMap一样操作。理论上可以支持Segment数量的并发写。
   4. JDK1.8改动
      1. JDK1.7使用分段锁机制实现并发更新；
      2. JDK1.8使用CAS操作来支持更高的并发度，操作失败时使用内置锁synchronized；
      3. JDK1.8也在链表过长时转化为红黑树。

6. **HashSet**
   1. 成员变量：HashSet几乎全部借助HashMap实现，`HashMap<E,Object> map`用于存放数据，`PRESENT`是所有写入map的value值。
   2. 构造函数：利用HashMap初始化map。
   3. add(): `e`是key值，所有value值为PRESENT。当有重复的`e`写入时，会对value覆盖，但key不会受到影响。
      ```java
      public boolean add(E e) {
         return map.put(e, PRESENT) == null;
      }
      ```

7. **LinkedHashSet and LinkedHashMap**
   1. 概览
      1. 两者关系与HashMap和HashSet关系类似。LinkedHashMap实现了Map接口，允许放入key和value为null的元素。可将LinkedHashMap看作采用LinkedList增强的HashMap。
      2. LinkedHashMap是HashMap的直接子类，两者的唯一区别是，LinkedHashMap采用双向链表的形式将所有entry连接起来，保证元素迭代顺序和插入顺序相同。
      3. 迭代LinkedHashMap无需像HashMap一样遍历整个table，而只需要遍历header指向的双向链表即可。
      4. 两个参数影响性能：初始容量（initial capacity）和负载系数（load factor）。初始容量指定了初始table大小，capacity * loadfactor指定了自动扩容的临界值。
   2. get()/put()/remove()：与HashMap类似。
   3. LinkedHashMap经典用法：
      1. `protected boolean removeEldestEntry(Map.Entry<K,V> eldest)`告诉Map是否删除最老的Entry，如果返回true就删除。只需要在子类中重写该方法，当元素超过一定数量让removeEldestEntry()返回true，即删除最老的元素。
      2. 比如手机app一览界面，最多保存10个app，当新开一个app时，最老的app会被移除，若切换至其中一个app，此app会被移动至最顶部（链表尾部）。

#### 3. 容器中设计模式

1. 迭代器模式
   1. Collection实现了Iterable接口，其中的iterator()方法能够产生一个Iterator对象，通过此对象可遍历Collection中的元素。
   2. JDK 1.5之后，可用`foreach`方法遍历Iterable接口的聚合对象。
2. 适配器模式
   1. java.util.Arrays.asList()可以把数组转换为List类型。需要注意，asList()的参数时泛型的变长参数，因此不能使用基本类型数组作为参数，只能使用相应的包装类型数组。
      ```java
      Integer[] arr = {1, 2, 3};
      List list = Arrays.asList(arr);
      // or
      List list = Arrays.asList(1,2,3);
      ```
#### 4. 面试指南

1. **ArrayList和LinkedList的区别**
   1. 底层数据结构：ArrayList动态数组、LinkedList链表
   2. 随机访问时：ArrayList比LinkedList效率高，因为LinkedList需要移动指针依次查找。
   3. 增加删除操作：LinkedList比ArrayList效率高，ArrayList在中间添加元素，其后面所有的元素都需要向后移动一位。
   4. 利用效率：ArrayList自由度较低，例如需要设置容量等，但使用方便。LinkedList自由度高，随着数据量动态变化，但是相对不便使用。
   5. 空间开销：ArrayList需要预留一定额外空间用于添加元素；LinkedList主要存储节点和指针信息。
2. **HashMap和HashTable区别**
   1. HashTable基于Dictionary类，HashMap基于AbstractMap类。Dictionary是任何可将键映射到相应值的类的抽象父类；AbstractMap是基于Map的接口实现，可以最大限度地减少实现此接口所需的工作。
   2. HashMap的key和value可以为null，但不能为可变对象，因为可变对象发生变化时key也发生变化，会导致无法查询到在Map中的数据。（如果可以保证对象改变不改变哈希值，也可以）。HashTable的key和value不允许为null。
   3. HashTable通过synchronized关键字实现线程安全，由于在执行方法时需要获得对象锁，因此执行起来比较慢。推荐使用CurrentHashMap。
3. **HashMap和CurrentHashMap**
   1. CurrentHashMap应用分段锁，即容器里有多个Segment，每个Segment拥有一把锁，可以支持Segment数量的并发。
   2. get()操作高效，因为整个过程不需要加锁（除非读到null值需要加锁重读）。get()将要使用的共享变量都定义成volatile，能够在线程之间保持可见性，被多线程同时读并且不会读到过期的值。
   3. put()方法首先定位到Segment，然后在Segment进行类似HashMap的插入操作。
4. **Hash冲突解决方法**
   1. 链地址法（HashMap, HashTable, HashSet采用的方案）
   2. 开放地址法
   3. 再哈希法
5. **什么是迭代器**
   1. 我们把Java集合框架的集合类称为容器（如ArrayList, LinkedList等），每种容器都有自身特点。
   2. 为了简化遍历容器中元素的操作，Java引入迭代器模式。把访问逻辑从不同类型集合类中抽取出来，从而避免向外部暴露集合的内部结构。
   3. 迭代器模式：提供一种方法，对一个容器对象的各个元素访问，而不暴露该对象容器的内部细节。
      ```java
      public static void main(String[] args) {
          // 使用迭代器遍历ArrayList集合
          Iterator<String> listIt = list.iterator();
          while(listIt.hasNext()){
              System.out.println(listIt.hasNext());
          }
          // 使用迭代器遍历Set集合
          Iterator<String> setIt = set.iterator();
          while(setIt.hasNext()){
              System.out.println(listIt.hasNext());
          }
          // 使用迭代器遍历LinkedList集合
          Iterator<String> linkIt = linkList.iterator();
          while(linkIt.hasNext()){
              System.out.println(listIt.hasNext());
          }
      }
      ```
6. **构造相同hash字符串进行攻击，该怎么处理此情况？**
   1. 攻击原理：有人恶意构造请求，在请求中加入大量相同hash的String参数名，在服务器端用于存储这些key-value对的HashMap会被强制退化为链表。
   2. 如何处理:
      1. 限制POST和GET请求的参数个数
      2. 限制POST请求的请求体大小
      3. Web Application FireWall (WAF)
   3. JDK 1.7如何处理：HashMap会动态地使用一个专门TreeMap实现来替换掉它。
7. HashMap的容量为什么是2 ^ n？
   1. 在给定key后，需要经过hash计算确定桶下标，最后一步是对桶容量取模(`%`)，而当`x = 2^n`时，`y % x = y & (x - 1)`，位运算比取模运算效率高很多。
   2. HashMap每次扩容为2倍，当`x = 2^n`时，每次扩容后重新计算Hash值只需要看key的hash值新最高位为1还是0，若是0则不变，若是1则加上此位十进制值。