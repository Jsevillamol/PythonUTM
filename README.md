# PythonUTM
Turing Machine compiler implemented in Python

#How to program the UTM
###Programs
Programs are 4 digit lines plus comments.

Example:

    1 1 0 1 Addittion Program
    1 0 R 2 Input: a,b, integers in monadic notation
    2 1 R 2 Output: a+b in monadic notation
    2 0 1 3
    3 1 L 3
    3 0 R 4

The first two digits are the actual state of the Turing Machine and a blank (0) or stroke (1).

The last two represent an instruction (0,1,L,R) and the next state.

####Instructions
* Zero (0): writes a 0 in the actual position
* Stroke (1): writes a 1 in the actual position
* Left (L): moves the cursor one position to the left of the tape
* Right (R): moves the cursor one position to the right of the tape

###Tapes
Tapes are the memory and interface of the program. It consist of a symbollically infinite array in both directions with a finite quantity of strokes (1) and the remaining filled with blanks (0).

Inputs are feed in monadic notation, and outputs are given in monadic notation as well.

For example, `110111` represents a 2 followed by a 3.

###Running a program
The machine starts over the tile 0 of the tape and state 1.
The machine reads the data in the actual tile, and searchs the instruction corresponding to the pair (state, data).
For example, the program given as an example in the tape given as an example first would execute `1 1 0 1`.
That means writing a blank (0) in the position 0 of the tape and then conserving the state.

The next instruction to be executed would be `1 0 R 2`. Which means moving right and then switching the state to 2.

When no instruction is found for the corresponding pair state data, the machine halts.
The machine is considered to have made a concrete output when it finishes in a valid position. That is:
1. The cursor is over the left-most 1.
2. Every number in the output is expressed in monadic notation separated by blanks.
