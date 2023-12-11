package WHP2023;

public class Taster extends Component{
    /**
     * Erstellt einen Taster
     * @author Alexander Smyrnov
     */
    Taster(){
        super(0, 1);
    }

    @Override
    void calc(){}

    /**
     * Flippt den Output eines Tasters
     * @author Alexander Smyrnov
     */
    void press(){
        outputs[0] = !outputs[0];
    }
}
