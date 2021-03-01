package thread;

public class Main {

    public static void main(String[] args) {
        CommonResource commonResources = new CommonResource();
        for (int i=1;i<5;i++){
            Thread t = new Thread(new CountThread(commonResources), "Thread"+i);
            t.start();
        }
        System.out.println("Main thread finished");
    }
}
