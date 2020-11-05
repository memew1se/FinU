package Collections2;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Stack;

public class PlaneIterator implements Iterator<String> {
    private Stack<Iterator> iteratorStack;
    private String next;
    private boolean hasNext;

    public PlaneIterator(Iterator<?> iterator) {
        this.iteratorStack = new Stack<Iterator>();
        iteratorStack.push(iterator);
        updateNext();
    }

    @Override
    public boolean hasNext() {
        return hasNext;
    }

    private void updateNext() {
        if (iteratorStack.empty()) {
            next = null;
            hasNext = false;
        }
        Iterator current = iteratorStack.peek();
        if (current.hasNext()) {
            Object o = current.next();
            if (o instanceof String) {
                next = (String) o;
                hasNext = true;
            } else if (o instanceof Iterator) {
                Iterator iterator = (Iterator) o;
                iteratorStack.push(iterator);
                updateNext();
            } else {
                throw new IllegalArgumentException();
            }
        } else {
            iteratorStack.pop();
            updateNext();
        }
    }

    @Override
    public String next() throws NoSuchElementException {
        if (!hasNext) {
            throw new NoSuchElementException();
        }
        String nexttoreturn = next;
        updateNext();
        return nexttoreturn;
    }
}