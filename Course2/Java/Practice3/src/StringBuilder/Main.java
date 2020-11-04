package StringBuilder;

public class Main {

    public static void main(String[] args) {
	    UndoableStringBuilder undoableStringBuilder = new UndoableStringBuilder();

        System.out.println(undoableStringBuilder.append("abcd"));
        System.out.println(undoableStringBuilder.reverse());

        undoableStringBuilder.undo();
        System.out.println("Undo: " + undoableStringBuilder);

        System.out.println("------");

        ObservableStringBuilder observableStringBuilder = new ObservableStringBuilder();

        observableStringBuilder.append("Some");
        observableStringBuilder.setListener(new Listener());
        observableStringBuilder.append("thing");
    }
}
