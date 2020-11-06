/**
	localizer.cpp

	Purpose: implements a 2-dimensional histogram filter
	for a robot living on a colored cyclical grid by 
	correctly implementing the "initialize_beliefs", 
	"sense", and "move" functions.

	This file is incomplete! Your job is to make these
	functions work. Feel free to look at localizer.py 
	for working implementations which are written in python.
*/

#include "localizer.h"
#include "helpers.cpp"
#include <stdlib.h>
#include "debugging_helpers.cpp"

using namespace std;

/**
	TODO - implement this function 
    
    Initializes a grid of beliefs to a uniform distribution. 

    @param grid - a two dimensional grid map (vector of vectors 
    	   of chars) representing the robot's world. For example:
    	   
    	   g g g
    	   g r g
    	   g g g
		   
		   would be a 3x3 world where every cell is green except 
		   for the center, which is red.

    @return - a normalized two dimensional grid of floats. For 
           a 2x2 grid, for example, this would be:

           0.25 0.25
           0.25 0.25
*/
// INITIALIZE BELIEFS --------------------------------------------------------------------------------------------
vector< vector <float> > initialize_beliefs(vector< vector <char> > grid) {
	vector< vector <float> > newGrid;

//height, width, @param 2D grid
  	int height = grid.size();
  	int width = grid[0].size();
//calculate area, floating point
  	float area = width * height;
  	float cell_belief = 1 / area;
  	vector <float> row_transient;
//i, height loop and j, width loop
  	for (int i = 0; i < height; i++) {
    		row_transient.clear();
      		for (int j = 0; j < width; j++) {
            		row_transient.push_back(cell_belief);
            }
			newGrid.push_back(row_transient);      
    }
	return newGrid;
}

/**
  TODO - implement this function 
    
    Implements robot motion by updating beliefs based on the 
    intended dx and dy of the robot. 

    For example, if a localized robot with the following beliefs

    0.00  0.00  0.00
    0.00  1.00  0.00
    0.00  0.00  0.00 

    and dx and dy are both 1 and blurring is 0 (noiseless motion),
    than after calling this function the returned beliefs would be

    0.00  0.00  0.00
    0.00  0.00  0.00
    0.00  0.00  1.00 

  @param dy - the intended change in y position of the robot

  @param dx - the intended change in x position of the robot

    @param beliefs - a two dimensional grid of floats representing
         the robot's beliefs for each cell before sensing. For 
         example, a robot which has almost certainly localized 
         itself in a 2D world might have the following beliefs:

         0.01 0.98
         0.00 0.01

    @param blurring - A number representing how noisy robot motion
           is. If blurring = 0.0 then motion is noiseless.

    @return - a normalized two dimensional grid of floats 
         representing the updated beliefs for the robot. 
*/


//-----------------------------------------------ROBOT MOTION ----------------------------------------------------------


vector< vector <float> > move(int dy, int dx, 
  		vector < vector <float> > beliefs,
  		float blurring) 
{

  		vector < vector <float> > newGrid;
  		vector <float> rows;

  //h and w, @param beliefs 2D grid
  		int height = beliefs.size();
  		int width = beliefs[0].size();
  		for (int i = 0; i < height; i++) {
    			rows.clear();
          		for (int j = 0; j < width; j++) {
                		rows.push_back(0.0);
                }
          		newGrid.push_back(rows);
    
        }
  		//signed - so it can hold positive and negative values - REFERENCE: "Modulus with negative numbers in C++"(stack overflow). Modulo function in helpers.cpp (Modl)
  		// use g++ -std=c++ tests.cpp
  		/* output should be:
        	1 0 0
            0 0 0
            0 0 0
        */  
  		signed int changed_i;
  		signed int changed_j;
  		for (int i = 0; i < height; i++) {
        		for (int j = 0; j < width; j++) {
                		changed_i = Modl((i + dy), height);
                		changed_j = Modl((j + dx), width);
                		newGrid[changed_i][changed_j] = beliefs[i][j];
                }
        }

  		return blur(newGrid, blurring);
}


//------------------------------------------------END ROBOT MOTION-----------------------------------------------------



/**
	TODO - implement this function 
    
    Implements robot sensing by updating beliefs based on the 
    color of a sensor measurement 

	@param color - the color the robot has sensed at its location

	@param grid - the current map of the world, stored as a grid
		   (vector of vectors of chars) where each char represents a 
		   color. For example:

		   g g g
    	   g r g
    	   g g g

   	@param beliefs - a two dimensional grid of floats representing
   		   the robot's beliefs for each cell before sensing. For 
   		   example, a robot which has almost certainly localized 
   		   itself in a 2D world might have the following beliefs:

   		   0.01 0.98
   		   0.00 0.01

    @param p_hit - the RELATIVE probability that any "sense" is 
    	   correct. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

   	@param p_miss - the RELATIVE probability that any "sense" is 
    	   incorrect. The ratio of p_hit / p_miss indicates how many
    	   times MORE likely it is to have a correct "sense" than
    	   an incorrect one.

    @return - a normalized two dimensional grid of floats 
    	   representing the updated beliefs for the robot. 
*/



//--------------------------------SENSE--------------------------------------------------------------------

vector< vector <float> > sense(char color, 
		vector< vector <char> > grid, 
		vector< vector <float> > beliefs, 
		float p_hit,
		float p_miss) 
{
		vector< vector <float> > newGrid;
  		
		vector <float> sense_rows;
		//i,height for loop and j, width for loop 
  		for (int i = 0; i < grid.size(); i++) {
        		for (int j = 0; j < grid[0].size(); j++) {
                		//param color equal to 2D grid
                		if (color == grid[i][j]) {
                				sense_rows.push_back(beliefs[i][j] * p_hit);
                		}
                		else {
                          		sense_rows.push_back(beliefs[i][j] * p_miss);
                		}
                }
          		newGrid.push_back(sense_rows);
        }

// reference for push_back (checked against): https://www.tutorialspoint.com/cpp_standard_library/cpp_vector_push_back.htm 
  
		return normalize(newGrid);
}




//--------------------------------END SENSE---------------------------------------------------------------

