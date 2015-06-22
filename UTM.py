# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:17:12 2015

@author: Jaime
"""
from collections import deque

class UTM:
    def __init__(self, program = "test.tm", tape = "test.tape"):
        self.instructions = {
            "0": self.zero,
            "1": self.stroke,
            "L": self.left,
            "R": self.right
        }
        self.UTM_compile(program)
        self.state = 1
        
        self.tape = deque([1,1,0,1,1,1]) #Todo: load tape
        self.cursor = 0
        self.run()
    
    def run(self):
        print(self.tape)
        self.halted = False
        while(not self.halted):
            try:
                self.do()
                print(self.tape)
            except IndexError:
                print("Enlarging tape...")
                if self.cursor < 0: self.tape.appendleft(0)
                elif self.cursor >= len(self.tape): self.tape.append(0)
            except KeyError:
                print("Finished")
                self.halted = True
            
    def do(self):
        if self.cursor < 0: raise IndexError
        instruction = self.program[self.state][self.tape[self.cursor]]
        instruction["instruction"]()
        self.state = instruction["next_state"]
    
    def UTM_compile(self,filename):
        with open(filename) as file:
            self.program = {}
            for instruction in file:
                instruction = instruction.split()
                if not int(instruction[0]) in self.program:
                    self.program[int(instruction[0])] = {}
                self.program[int(instruction[0])].update(
                        {int(instruction[1]):
                            {"instruction": self.instructions[
                                instruction[2]],
                             "next_state": int(instruction[3])
                            }
                        }
                    )
        
    def zero(self): self.tape[self.cursor] = 0
    def stroke(self): self.tape[self.cursor] = 1
    def left(self): self.cursor -= 1
    def right(self): self.cursor += 1
        
if __name__ == "__main__":
    utm = UTM()