package UE02_Labyrinth;
//TODO: Mein Name in der Javadoc

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class Labyrinth {
	static final char FILLCHAR = 'x';
	public static String[][] maps = {{
		"############",
		"#  #     # #",
		"## # ### # #",
		"#  # # # # #",
		"## ### # # #",
		"#        # #",
		"## ####### #",
		"#          #",
		"# ######## #",
		"# #   #    #",
		"#   #   # ##",
		"######A#####"
	}, {
		"################################",
		"#                              #",
		"# ############################ #",
		"# # ###       ##  #          # #",
		"# #     ##### ### # ########## #",
		"# #   ##### #     # #      ### #",
		"# # ##### #   ###   # # ## # # #",
		"# # ### # ## ######## # ##   # #",
		"# ##### #  # #   #    #    ### #",
		"# # ### ## # # # # ####### # # #",
		"# #        # #   #     #     # #",
		"# ######## # ######### # ### # #",
		"# ####     #  # #   #  # ##### #",
		"# # #### #### # # # # ## # ### #",
		"#                      # #     #",
		"###########################A####"
	}, {
		"###########################A####",
		"#   #      ## # # ###  #     # #",
		"# ###### #### # # #### ##### # #",
		"# # ###  ## # # # #          # #",
		"# # ### ### # # # # # #### # # #",
		"# #     ### # # # # # ## # # # #",
		"# # # # ### # # # # ######## # #",
		"# # # #     #          #     # #",
		"# ### ################ # # # # #",
		"# #   #             ## # #   # #",
		"# # #### ############# # #   # #",
		"# #                    #     # #",
		"# # #################### # # # #",
		"# # #### #           ###     # #",
		"# # ## # ### ### ### ### # ### #",
		"# #    #     ##  ##  # ###   # #",
		"# ####   ###### #### # ###  ## #",
		"###########################A####"
	}, {
		"#############",
		"#           #",
		"#           #",
		"#           #",
		"###########A#"
	}};

	/**
	 * Wandelt (unveränderliche) Strings in Char-Arrays
	 * @param map  der Plan, ein String je Zeile
	 * @return char[][] des Plans
	 */
	public static char[][] fromStrings(String[] map) {
		char[][] res = new char[map.length][map[0].length()];
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length(); j++) {
				res[i][j] = map[i].charAt(j);
			}
		}
		return res;
	}
	/**
	 * Ausgabe des Layrinths
	 * @param lab
	 */
	public static void printLabyrinth(char[][] lab) {
		for (int i = 0; i < lab.length; i++) {
			for (int j = 0; j < lab[0].length; j++) {
				System.out.print(lab[i][j]);
			}
			System.out.println("");
		}
	}

	/**
	 * Suche den Weg
	 * @param zeile     aktuelle Position
	 * @param spalte     aktuelle Position
	 * @param lab
	 * @throws InterruptedException    für die verlangsamte Ausgabe mit sleep()
	 */
	public static boolean suchen(int zeile, int spalte, char[][] lab) throws InterruptedException {
		switch (lab[zeile][spalte]) {
			case 'A', 'a':
				printLabyrinth(lab);
				return true;
			case '#', FILLCHAR:
				return false;
		}

		lab[zeile][spalte] = FILLCHAR;
		Boolean n1 = suchen(zeile-1, spalte, lab);
		Boolean n2 = suchen(zeile+1, spalte, lab);
		Boolean n3 = suchen(zeile, spalte-1, lab);
		Boolean n4 = suchen(zeile, spalte+1, lab);
		lab[zeile][spalte] = ' ';
		return n1 || n2 || n3 || n4;
	}

	/**
	 * Sucht alle möglichen Wege
	 * @param zeile Startzeile
	 * @param spalte Startspalte
	 * @param lab das zu lösense Labyrinth
	 * @return 0 wenn Rand, 1 wenn Ausgang, Summe aller gefundenen Ausgänge wenn alle gefunden wurden
	 * @throws InterruptedException
	 */
	public static int sucheAlle(int zeile, int spalte, char[][] lab) throws InterruptedException {
		switch (lab[zeile][spalte]) {
			case 'A', 'a':
				printLabyrinth(lab);
				return 1;
			case '#', FILLCHAR:
				return 0;
		}

		lab[zeile][spalte] = FILLCHAR;
		int n1 = sucheAlle(zeile-1, spalte, lab);
		int n2 = sucheAlle(zeile+1, spalte, lab);
		int n3 = sucheAlle(zeile, spalte-1, lab);
		int n4 = sucheAlle(zeile, spalte+1, lab);
		lab[zeile][spalte] = ' ';
		return n1 + n2 + n3 + n4;
	}

	public static char[][] readFile(String filepath){
		try {
			return fromStrings(Files.readAllLines(Paths.get(filepath)).toArray(new String[0]));
		}
		catch(IOException e){
			e.printStackTrace();
		}
		return new char[][]{};
	}

	public static void main(String[] args) throws InterruptedException {
		char[][] labyrinth = fromStrings(maps[2]);
		printLabyrinth(labyrinth);
		System.out.println("Ausgang gefunden: " + (suchen(5, 5, labyrinth) ? "ja" : "nein"));
		System.out.println("Anzahl Wege: " + sucheAlle(5, 5, labyrinth));
		printLabyrinth(readFile("/home/alex/SEW5CN/sew5j/src/UE02_Labyrinth/l1.txt"));
	}

}
