package StringBuilder;

import java.util.Stack;

public class UndoableStringBuilder {

    private java.lang.StringBuilder stringBuilder;

    public interface Action{
        void undo(); // Интерфейс для поддержки undo в каждой функции
    }

    private class DeleteAction implements Action{
        private int size;

        public DeleteAction(int size){
            this.size = size;
        }

        @Override
        public void undo(){
            stringBuilder.delete(stringBuilder.length() - size, stringBuilder.length());
        }
    }

    private Stack<Action> actions = new Stack<>();

    public UndoableStringBuilder(){
        stringBuilder = new StringBuilder();
    }

    public void undo(){
        if (!actions.isEmpty()){
            actions.pop().undo();
        }
    }

    public UndoableStringBuilder appendCodePoint(int codePoint) {
        int len = stringBuilder.length();
        stringBuilder.appendCodePoint(codePoint);

        DeleteAction action = new DeleteAction(stringBuilder.length() - len);

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder append(String string){
        stringBuilder.append(string);

        Action action = new Action(){
            public void undo(){
                stringBuilder.delete(stringBuilder.length() - string.length(),
                                     string.length());
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder insert(int index, char[] string, int offset, int len){
        stringBuilder.insert(index, string, offset, len);

        Action action = new Action(){
            public void undo(){
                stringBuilder.delete(index, len);
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder insert(int offset, String string) {
        stringBuilder.insert(offset, string);

        Action action = new Action(){
            public void undo(){
                stringBuilder.delete(offset, string.length());
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder replace(int start, int end, String string){
        String del_string = stringBuilder.substring(start, end);
        stringBuilder.replace(start, end, string);

        Action action = new Action(){
            public void undo(){
                stringBuilder.replace(start, end, del_string);
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder delete(int start, int end) {
        String deleted = stringBuilder.substring(start, end);
        stringBuilder.delete(start, end);

        Action action = new Action() {
            public void undo() {
                stringBuilder.insert(start, deleted);
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder deleteCharAt(int index) {
        char deleted = stringBuilder.charAt(index);
        stringBuilder.deleteCharAt(index);

        Action action = new Action(){
            public void undo(){
                stringBuilder.insert(index, deleted);
            }
        };

        actions.add(action);
        return this;
    }

    public UndoableStringBuilder reverse(){
        stringBuilder.reverse();

        Action action = new Action() {
            public void undo() {
                stringBuilder.reverse();
            }
        };

        actions.add(action);
        return this;
    }

    public String toString(){
        return stringBuilder.toString();
    }
}

