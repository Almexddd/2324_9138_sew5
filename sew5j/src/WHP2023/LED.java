package WHP2023;

public class LED extends Component{
    /**
     * Erstellt eine LED
     * @author Alexander Smyrnov
     */
    LED(){
        super(1,0);
    }
    /**
     * Erstellt eine LED
     * @param input Input der LED
     * @author Alexander Smyrnov
     */
    LED(Input input){
        super(1,0);
        inputs = new Input[]{input};
    }

    @Override
    void calc(){}

    boolean getState(){
        return inputs[0].value;
    }
}
