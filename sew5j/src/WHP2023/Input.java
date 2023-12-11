package WHP2023;

public class Input {
    boolean value;
    Component previous;
    int previousPin;

    Input(){
    }

    /**
     * Verbindet den Input mit einem Output
     * @param comp Komponente mit der der Input verbunden ist
     * @param previousPin Pinnummer des Outputs der Komponente
     * @author Alexander Smyrnov
     */
    void connect(Component comp, int previousPin) {
        this.previous = comp;
        this.previousPin = previousPin;
    }

    /**
     * Updatet den State des Inputs
     * @author Alexander Smyrnov
     */
    void fetch(){
        if (previous != null) {
            value = previous.getOut(previousPin);
        }
    }
}
