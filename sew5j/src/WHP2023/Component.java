package WHP2023;

public abstract class Component {
    String name;
    Input[] inputs;
    boolean[] outputs;

    /**
     * Erstellt eine neue Komponente
     * @param nInputs Anzahl der Inputs
     * @param nOutputs Anzahl der Outputs
     * @author Alexander Smyrnov
     */
    public Component(int nInputs, int nOutputs) {
        this("NN", nInputs, nOutputs);
    }

    /**
     * Erstellt eine neue Komponente
     * @param name Name der Komponente
     * @param nInputs Anzahl der Inputs
     * @param nOutputs Anzahl der Outputs
     * @author Alexander Smyrnov
     */
    public Component(String name, int nInputs, int nOutputs) {
        this.name = name;
        inputs=new Input[nInputs];
        while (nInputs-- > 0) {
            inputs[nInputs] = new Input();
        }

        outputs = new boolean[nOutputs];
    }

    /**
     * Verbindet den Input einer Komponente mit dem Output einer anderen
     * @param comp Komponente mit der sich verbunden werden soll
     * @param previousPin Pin des Outputs
     * @param thisPin Pin des Inputs
     * @author Alexander Smyrnov
     */
    void connect(Component comp, int previousPin, int thisPin) {
        this.inputs[thisPin].connect(comp, previousPin);
    }

    /**
     * Setzt den Wert eines Outputs
     *
     * @param value Wert
     * @param Nr    Output
     * @author Alexander Smyrnov
     */
    private void setOut(boolean value, int Nr) {
        outputs[Nr] = value;
    }

    /**
     * Holt den Wert eines Outputs
     * @param Nr Output
     * @author Alexander Smyrnov
     */
    boolean getOut(int Nr) {
        return outputs[Nr];
    }

    /**
     * Pullt alle gegenüberliegenden Outputs in die Inputs
     * @author Alexander Smyrnov
     */
    public void fetch() {
        for (Input input : inputs) {
            input.fetch();
        }
    }

    /**
     * Berechnet die Outputs einer Komponente
     *
     * @author Alexander Smyrnov
     */
    abstract void calc();

    /**
     * Gibt eine Komponente im Format Name>Inputs:Outputs aus
     *
     * @author Alexander Smyrnov
     */
    @Override
    public String toString() {
        StringBuilder b = new StringBuilder();
        b.append(name).append('>');
        for (Input input : inputs) {
            b.append(input.value ? 1 : 0);
        }
        b.append(':');
        for (boolean output : outputs) {
            b.append(output ? 1 : 0);

        }
        return b.toString();
    }
}
