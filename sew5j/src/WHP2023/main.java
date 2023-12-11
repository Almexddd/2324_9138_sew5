package WHP2023;

public class main {
    public static void main(String[] args) {
        Takt takt = new Takt();
        Taster taster1 = new Taster();
        Taster taster2 = new Taster();
        FF ff = new FF("FF");
        ff.connect(taster1, 0, FF.S);
        ff.connect(taster2, 0, FF.R);
        LED led = new LED();
        led.connect(ff, FF.Q,0);
        takt.add(taster1, taster2, ff, led);

        taster1.press();
        takt.tick();
        System.out.println("Taster 1: " + taster1.getOut(0));
        System.out.println("Taster 2: " + taster2.getOut(0));
        System.out.println("FF: " + ff.getOut(0));
        System.out.println("LED: " + led.getState());
        System.out.println();

        taster2.press();
        taster1.press();
        takt.tick();
        System.out.println("Taster 1: " + taster1.getOut(0));
        System.out.println("Taster 2: " + taster2.getOut(0));
        System.out.println("FF: " + ff.getOut(0));
        System.out.println("LED: " + led.getState());

        takt.tick();
        System.out.println();
        System.out.println("LED: " + led.getState());
    }
}