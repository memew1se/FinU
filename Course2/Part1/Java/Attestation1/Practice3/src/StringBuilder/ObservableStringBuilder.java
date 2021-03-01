package StringBuilder;

interface ChangeListener {

    void onChange(ObservableStringBuilder stringBuilder);
}
class Listener implements ChangeListener{

    @Override
    public void onChange(ObservableStringBuilder stringBuilder) {
        System.out.println("Change: " + stringBuilder.toString());
    }
}
public class ObservableStringBuilder {

    private ChangeListener listener;
    private StringBuilder stringBuilder;

    public ObservableStringBuilder(){
        stringBuilder = new StringBuilder();
    }

    public void setListener(ChangeListener listener){
        this.listener = listener;
    }
    private void notifylistener(){
        if(listener != null){
            listener.onChange(this);
        }
        else{
            System.out.println("Notify off");
        }
    }

    public ObservableStringBuilder appendCodePoint(int CodePoint) {
        stringBuilder.appendCodePoint(CodePoint);
        notifylistener();
        return this;
    }
    public ObservableStringBuilder append(Object obj) {
        stringBuilder.append(obj);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder append(String string) {
        stringBuilder.append(string);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder insert(int index, char[] string, int offset, int len) {
        stringBuilder.insert(index, string, offset, len);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder replace(int start, int end, String string) {
        stringBuilder.replace(start, end, string);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder delete(int start,int end) {
        stringBuilder.delete(start, end);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder deleteCharAt(int index) {
        stringBuilder.deleteCharAt(index);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder indexOf(String string) {
        stringBuilder.indexOf(string);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder indexOf(String string, int fromindex) {
        stringBuilder.indexOf(string, fromindex);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder lastIndexOf(String string, int fromindex) {
        stringBuilder.lastIndexOf(string, fromindex);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder lastIndexOf(String string) {
        stringBuilder.lastIndexOf(string);
        notifylistener();
        return this;
    }

    public ObservableStringBuilder reverse() {
        stringBuilder.reverse();
        notifylistener();
        return this;
    }

    public String toString() {
        return stringBuilder.toString();
    }
}