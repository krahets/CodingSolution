- Date: 2019.8.3

#### First round
1. 算法题：非递减数组`arr`，找到和为`P`的所有窗口，输出所有窗口下标；
   - 双指针法解决。
2. HashMap/HashTable/ConcurrentHashMap共同点与区别。
3. 红黑树原理与用途。
4. B树、B+树原理。
5. Java和C++区别？
6. 假设有一台服务器和多个客户端，如何保证多个客户端和服务器之间I/O连接的稳定？

#### Second rount
1. 给定四个点坐标，如何连接出一个四边形？（假设四个点组成的四边形为凸四边形）
  - 找到外接矩形，即可对四个坐标做逆时针排序和顺时针排序。 
  - 4个顶点两两相连共6条线，排除相交的2条对角线，剩余的则为四边形。
2. 下面哪个是原子操作？
   ```java
   a = 1; // Y
   a = 1 + 2; // Y
   a++; // N
   a = b; // N
   ```
3. 三个线程按顺序不断输出ABC的方法？
   ```java
   package thread;

   import java.util.concurrent.locks.Lock;
   import java.util.concurrent.locks.ReentrantLock;

   /**
    * @author Beauxie
    */
   public class TestThresd2 {

   	// //通过JDK5中的锁来保证线程的访问的互斥
   	private static Lock lock = new ReentrantLock();

   	private static int state = 0;// 用state来判断轮到谁执行
   	
   	private static final int RUN_NUMBER=100;//表示循环的次数

   	//A线程
   	static class ThreadA extends Thread {

   		@Override
   		public void run() {
   			for (int i = 0; i < RUN_NUMBER;) {
    				lock.lock();//获取锁定
   				if (state % 3 == 0) {
   					System.out.println("第"+(i+1)+"次:");
   					System.out.println("A");
   					state++;
   					i++;
   				}
    				lock.unlock();//释放锁定,不释放锁定，会被该线程一直保持
   			}
   		}
   	}
   	//B线程
   	static class ThreadB extends Thread {
   		
   		@Override
   		public void run() {
   			for (int i = 0; i < RUN_NUMBER;) {
    				lock.lock();
   				if (state % 3 ==1) {
   					System.out.println("B");
   					state++;
   					i++;
   				}
    				lock.unlock();
   			}
   		}
   	}
   	//C线程
   	static class ThreadC extends Thread {
   		
   		@Override
   		public void run() {
   			for (int i = 0; i < RUN_NUMBER;) {
    				lock.lock();
   				if (state % 3 == 2) {
   					System.out.println("C");
   					state++;
   					i++;
   				}
    				lock.unlock();
   			}
   		}
   	}
   	public static void main (String[] args){
   		new ThreadA().start();
   		new ThreadB().start();
   		new ThreadC().start();
   	}

   }
   ```