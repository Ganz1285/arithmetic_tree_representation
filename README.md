# Math Operations in Tree Representation

Created By: Selvaganapathy Kannan
Type: Project Kickoff 🚀
Last Edited Time: August 24, 2023 3:30 PM
Last Edited By: Selvaganapathy Kannan

# Overview

To Represent a Mathematical Operation and flow of processes in a tree.

### Problem Statement

- Track and represent the flow of math operations in a tree.

### Proposed Solution

1. Check for arithmetic operators in the input (follow precedence orders)
    1. Check if the Input is a valid arithmetic operation 
        
        > each operators has left and right operands which are operands, not operators
        > 
        
        > first and last elements are operands, not operators
        > 
        
        > No two operators are next to each other
        > 
        
        > Input only contains `[0-9]`, `+`, `-`, `*`, `/`
        > 
        > 
        > ```bash
        > regex = `^[0-9+\-*/]+$`
        > ```
        > 
        
    2. locate and extract left - right operands of each operators
        - Complete function `splitter`
            -  Basic `splitter` that extracts left and right operands not with nodes  @today
                
                ```bash
                77+4-3*88/12*56
                >>>[('/', (88, 12)), ('*', (3, 88)), ('*', (12, 56)), ('+', (77, 4)), ('-', (4, 3))]
                ```
                
    3. Improve by declaring nodes for each operators
        - operators
            - left operand
            - right operand
            - operator
            - result
    4. Represent each node of operation in a tree manner 
        -  individual representions

1. Parse through the given input and create a doubly-linked tree where each has operators and values
    

# Success Criteria

The project will be considered successful if it can accurately represent mathematical expressions in a tree structure and evaluate them correctly. It should also be able to handle complex expressions with parentheses and variables.

# User Stories

- After the solution is shipped, users will be able to input complex mathematical expressions and have them represented in a clear and organized tree structure. They will also be able to evaluate the expressions and get accurate results.

# Scope

- This project will focus on representing and evaluating mathematical expressions in a tree structure. It will not include graphing or visualization of the expression. It will also not include support for complex functions or equations beyond basic arithmetic operations and variables.

### Requirements

- 

### Non-Requirements

-