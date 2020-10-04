//Benjamin Singleton
//I pledge my honor that I have abided by the Stevens Honor System.

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Anagrams {
	//Data Fields
	final Integer[] primes = {2 , 3 , 5 , 7, 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 ,
						 43 , 47 , 53 , 59 , 61 ,67 , 71 , 73 , 79 , 83 , 89 , 97 , 101};
	Map<Character,Integer> letterTable;
	Map<Long, ArrayList<String>> anagramTable;
	
	
	//Constructors
	public Anagrams() {
		letterTable = new HashMap<Character,Integer>();
		buildLetterTable();
		anagramTable = new HashMap<Long, ArrayList<String>>();
	}
	
	//Methods
	/**
	 * Receives the name of a text file containing words, one per line, and builds the
	 * has table anagramTable using addWord method.
	 * @param  s: the name of a text file.
	 * @throws IOException if the text file is not valid.
	 */
	private void processFile(String s) throws IOException {
		FileInputStream fstream = new FileInputStream(s);
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
		String strLine;
		while ((strLine = br.readLine()) != null) {
			this.addWord(strLine);
		}
		br.close();
	}
	
	/**
	 * Builds the hash table letterTable.
	 */
	private void buildLetterTable() {
		char[] alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
				'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
		for (int i = 0; i<alphabet.length; i++) {
			letterTable.put(alphabet[i], primes[i]);
		}
	}
	
	/**
	 * Computes the hash code of a string and adds word to the hash table.
	 * @param s: The word to be added to the hash table.
	 */
	private void addWord(String s) {
		if (anagramTable.containsKey(myHashCode(s))) {
			ArrayList<String> temp = anagramTable.get(myHashCode(s));
			temp.add(s);
			anagramTable.replace(myHashCode(s), temp);
		} else {
			ArrayList<String> temp = new ArrayList<String>();
			temp.add(s);
			anagramTable.put(myHashCode(s), temp);
		}
	}
	
	/**
	 * Receives a string and computers its hash code.
	 * @param  s: A word.
	 * @return The hash code of the given string s.
	 */
	private Long myHashCode(String s) {
		long key = 1;
		for (int i=0; i<s.length(); i++) {
			key *= letterTable.get(s.charAt(i));
		}
		return key;
	}
	
	/**
	 * Finds and returns the entries in the anagramTable which have the largest number
	 * of anagrams.
	 * @return List of the entries with the largest number of anagrams.
	 */
	private ArrayList<Map.Entry<Long, ArrayList<String>>> getMaxEntries() {
		ArrayList<Map.Entry<Long,ArrayList<String>>> max_entries = new ArrayList<Map.Entry<Long,ArrayList<String>>>();
		int max_value = 0; 
		for(Map.Entry<Long, ArrayList<String>> entry: anagramTable.entrySet()) {
			if (entry.getValue().size()>max_value) {
				max_entries.clear();
				max_entries.add(entry);
				max_value=entry.getValue().size();
			} else if (entry.getValue().size()==max_value) {
				max_entries.add(entry);
			}
		}
		return max_entries;
	}
	
	public static void main(String[] args) {
		Anagrams a = new Anagrams();
		
		final long startTime = System.nanoTime();
		try {
			a.processFile("words_alpha.txt");
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		
		ArrayList < Map . Entry < Long , ArrayList < String > >> maxEntries = a.getMaxEntries();
		final long estimatedTime = System.nanoTime() - startTime;
		final double seconds = (( double ) estimatedTime /1000000000);
		System.out.println("Time : " + seconds);
		System.out.println("Key of max anagrams: " + maxEntries.get(0).getKey());
		System.out.println("List of max anagrams: " + maxEntries.get(0).getValue());
		System.out.println("Length of list of max anagrams: " + maxEntries.get(0).getValue().size());
	}
}
