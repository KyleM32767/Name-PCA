/**
 * NameGenerator.java
 * 
 * A class that generates names using principle component analysis
 * This class handles all of the logic, so it can be implemented in any interface (graphical or not).
 * 
 * This uses the Efficient Java Matrix Library
 * http://ejml.org/
 * 
 * 
 * @author Kyle Mitard
 * Created 23 March 2020
 */

import org.ejml.simple.*;
import java.io.IOException;
import java.util.Scanner;

public class NameGenerator
{
	/*=====================================================================================================================================
	 * INSTANCE VARIABLES
	 *=====================================================================================================================================*/
	
	/**
	 * the eigenvectors used for principle component analysis
	 */
	private SimpleMatrix eigenvectors;

	
	/*=====================================================================================================================================
	 * METHODS
	 *=====================================================================================================================================*/

	/**
	 * Constructor
	 * 
	 * @param eigenvectorFile The path to a CSV file containing the eigenvectors
	 * @param size The length of each eigenvector, which equals of the longest name in the training set times 27
	 */
	public NameGenerator(String eigenvectorFile, int size) throws IOException
	{
		eigenvectors = new SimpleMatrix(size, size);
		eigenvectors.loadCSV(eigenvectorFile);
	}
	
	public static void main(String[] args) throws IOException
	{
		NameGenerator n = new NameGenerator("training\\eigenvectors\\female.csv", 270);
	}
}