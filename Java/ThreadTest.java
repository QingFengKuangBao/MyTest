import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

/**
 * 多线程的实现
 * 
 * @author 24179
 *
 */
public class ThreadTest {

	public static void main(String[] args) {

		// 继承Thread类 重写 run 方法
		Thread t = new ExtendThread();
		t.start();

		
		
		// 实现 Runnable接口
		Runnable r = new ImplRunnable();
		// 构建线程
		Thread tr = new Thread(r);
		tr.start();

		
		
		// 实现 Callable接口 可以有返回值 FutureTask
		Callable<Integer> c = new ImplCallable();
		FutureTask<Integer> fu = new FutureTask<>(c);
		// 构建线程
		Thread tf = new Thread(fu);
		tf.start();
		try {
			// 获取线程执行结果
			fu.get();
		} catch (InterruptedException | ExecutionException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}

// 继承Thread类 重写 run 方法
class ExtendThread extends Thread {

	public ExtendThread() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("继承 Thread类           实现多线程.......");
	}
}

// 实现 Runnable接口
class ImplRunnable implements Runnable {

	@Override
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("实现 Runnable接口     实现多线程.......");
	}

}

// 实现 Callable接口 可以有返回值 , 构造 FutureTask对象 new FutureTask<>(Callable)来执行;
class ImplCallable implements Callable<Integer> {

	@Override
	public Integer call() throws Exception {
		// TODO Auto-generated method stub
		System.out.println("实现 Callable接口     实现多线程.......");
		return 10;
	}

}
