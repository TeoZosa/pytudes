# Language Compiler
## Introduction #
A language compiler is a software used to convert the source code of a language into machine code, which is then executed by the computer’s processor. A compiler can have various components, including a scanner, lexical analyzer, semantic analyzer, code generations, etc., which might be handled by different modules of the program. The compilers are both language-specific and specific to the underlying hardware processor.

The scenarios and problems discussed in this chapter relate to handling language compiler’s code comments and expression computation functionality in different scenarios.

## Statement #
For this project, imagine that you are a developer at a company that is experimenting with the development of a new type of compiler for the C++ language. This compiler does not follow the architecture of conventional compilers.

The compiler program that your team is working on has various modules that handle different parts of the conversion. Your team is working on several optimizations to the compiler for large as well asa small program compilations.

## Features #
We will need to introduce the following features to implement the functionalities we discussed above:

- Feature #1: Detect comments in the source code and remove them.

- Feature #2: Compute the result of a mathematical expression given to you in string format in the C++ language.

- Feature #3: Unroll a loop by replacing it with repeated instructions.

- Feature #4: Optimize a code by replacing slow function calls with faster ones.

- Feature #5: Find the first build step that failed so we do not have to compile all the files again.

- Feature #6: Find the most frequently used variable or function call in a code.

The coming lessons will discuss these features and their implementation in detail. By the end of the section, you’ll be able to apply the solution to this scenario to different interview problems.
