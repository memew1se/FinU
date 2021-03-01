package task1;

public class Main {

    public static void main(String[] args) throws InterruptedException {

        Object lock = new Object();
        Thread thread = new Thread() {
            @Override
            public void run() {
                try {
                    synchronized (lock) {
                        lock.notifyAll();
                        lock.wait();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };
        synchronized (lock){
            System.out.println(thread.getState());
            thread.start();
            System.out.println(thread.getState());
            lock.wait();
            System.out.println(thread.getState());
            lock.notifyAll();
            System.out.println(thread.getState());
        }
        try {
            thread.join();
        }catch (InterruptedException e){}
        System.out.println(thread.getState());
    }
}
