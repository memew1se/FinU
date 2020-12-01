package task2;

public class SyncThread extends Thread{

    private Object obj;

    public SyncThread(Object obj){
        this.obj = obj;
    }

    public void run(){
        synchronized (obj){
            try{
                System.out.println(getName());
                obj.notify();
                obj.wait();
            }
            catch (InterruptedException e){
                obj.notify();
            }
        }
    }
}
