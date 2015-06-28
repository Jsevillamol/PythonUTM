# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:17:12 2015

@author: Jaime
"""
from collections import deque

class UTM:
    def __init__(self, program = "test.tm", tape = deque([0,0,0]), 
                 cursor = 0, state = 1):
        self.UTM_compile(program)
        self.state = state
        
        self.tape = tape #Todo: load tape
        self.cursor = cursor
        self.run()
    
    def run(self):
        print(self.tape, "cursor:", self.cursor, "state:", self.state)
        self.halted = False
        while(not self.halted):
            try:
                self.do()
                print(self.tape, "cursor:", self.cursor, "state:", self.state) #Todo: show cursor
            except IndexError:
                print("Enlarging tape...")
                if self.cursor < 0: 
                    self.tape.appendleft(0)
                    self.cursor = 0
                elif self.cursor >= len(self.tape): self.tape.append(0)
            except KeyError:
                print("Finished")
                self.halted = True
            
    def do(self):
        if self.cursor < 0: raise IndexError
        instruction = self.program[self.state][self.tape[self.cursor]]
        try:
            instruction["instruction"](self)
        except TypeError:
            self.call(instruction["instruction"])
        self.state = instruction["next_state"]
    
    def UTM_compile(self,filename):
        with open(filename) as file:
            self.program = {}
            for instruction in file:
                instruction = instruction.split()
                if not int(instruction[0]) in self.program:
                    self.program[int(instruction[0])] = {}
                
                try:
                    self.program[int(instruction[0])].update(
                            {int(instruction[1]):
                                {"instruction": self.instructions[
                                    instruction[2]],
                                 "next_state": int(instruction[3])
                                }
                            }
                        )
                except KeyError:
                    self.program[int(instruction[0])].update(
                            {int(instruction[1]):
                                {"instruction": instruction[2],
                                 "next_state": int(instruction[3])
                                }
                            }
                        )
        
    def zero(self): self.tape[self.cursor] = 0
    def stroke(self): self.tape[self.cursor] = 1
    def left(self): self.cursor -= 1
    def right(self): self.cursor += 1
	
    instructions = {
         "0": zero,
         "1": stroke,
         "L": left,
         "R": right
    }
    
    def call(self, program):
        print("Calling subprogram", program)
        subroutine = UTM(program, self.tape, self.cursor)
        self.tape = subroutine.tape
        self.cursor = subroutine.cursor
        
if __name__ == "__main__":
    utm = UTM("subroutine_test.tm")