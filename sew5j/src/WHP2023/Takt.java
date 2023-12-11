package WHP2023;

import java.util.ArrayList;
import java.util.List;

public class Takt {
    static List<Component> comps;

    /**
     * Erstellt einen Takt
     * @author Alexander Smyrnov
     */
    public Takt(){
        comps = new ArrayList<Component>();
    }

    /**
     * Erstellt einen Takt
     * @param components Komponenten die getaktet werden
     * @author Alexander Smyrnov
     */
    public Takt(Component ... components){
        comps = new ArrayList<Component>(List.of(components));
    }

    /**
     * Lässt einen Tick laufen
     * @author Alexander Smyrnov
     */
     void tick(){
        for (Component c: getComps()) {
            c.fetch();
        }
        for (Component c: getComps()) {
            c.calc();
        }
    }

    /**
     * Fügt Komponenten zum Takt hinzu
     * @param components Komponenten die getaktet werden sollen
     * @author Alexander Smyrnov
     */
    public void add(Component ... components){
        for(Component comp : components){
            comps.add(comp);
        }
    }

    /**
     * Gibt eine Liste der Komponenten des Takts zurück
     * @author Alexander Smyrnov
     */
    public static List<Component> getComps(){
        return comps;
    }
}
