package WHP2023;

public class FF extends Component {
    public static final int S = 0;
    public static final int R = 1;
    public static final int Q = 0;
    public static final int NQ = 1;
    States states = States.LOW;

    /**
     * Erstellt einen FF
     * @author Alexander Smyrnov
     */
    FF() {
        this("FF_NN");
    }

    FF(String name) {
        super(name,2,2);
        outputs[NQ] = !outputs[Q];
    }

    /**
     * Erstellt einen FF
     * @param R Reset-Input
     * @param S Set-Input
     * @author Alexander Smyrnov
     */
    FF(Input R, Input S) {
        super(2,2);
        inputs = new Input[]{R, S};
    }

    /**
     * Berechnet die Outputs einer Komponente
     * @author Alexander Smyrnov
     */
    @Override
    void calc() {
        states = states.handle(this.inputs, this.outputs);
    }

    static enum States {
        LOW {
            @Override
            States handle(Input[] inputs, boolean[] outputs) {
                if (inputs[S].value && !inputs[R].value) {
                    outputs[Q] = true;
                    outputs[NQ] = false;
                    return HIGH;
                }
                outputs[Q] = false;
                outputs[NQ] = true;
                return LOW;
            }
        }, HIGH {
            @Override
            States handle(Input[] inputs, boolean[] outputs) {
                if (!inputs[S].value && inputs[R].value) {
                    outputs[Q] = false;
                    outputs[NQ] = true;
                    return LOW;
                }
                outputs[Q] = true;
                outputs[NQ] = false;
                return HIGH;
            }
        };
        /**
         * Berechnet den Output des FFs
         * @param inputs Inputs des FFs
         * @param outputs Outputs des FFs
         * @author Alexander Smyrnov
         */
        abstract States handle(Input[] inputs, boolean[] outputs);
    }
}
