Project 02: Meal Price Calculator
---------------------------------

#### Regarding Milestones:

A milestone or milepost is a marker placed along a highway to tell you how far you have come, or to indicate your progress toward your destination. In software development projects, a Project Milestone marks a specific point along a project timeline.

To help you make progress toward finishing this project, you will complete part of the program during the middle of the week and submit a "Milestone Submission." Then, by the end of the week, you will complete the program and submit the finished version.

You should read over the complete project description first. Then, at the bottom of this page, you will see which features are required for the milestone and which are required for the overall project.

### Overview

Programs can obtain information from users and then combine those values to compute meaningful results. In this assignment, you will write a program to calculate the price of a meal.

### Instructions

Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate. Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.

Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

Ask the user for the following:

*   The price of a child's meal (floating point)
    
*   The price of an adult's meal (floating point)
    
*   The number of children (integer)
    
*   The number of adults (integer)
    

Then, complete the following steps:

*   Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal, and multiplying the number of adults by the price of their meal and adding those two values together.
    
*   Display the subtotal.
    

Hint from Instructor:

As you will see in the requirements list below, this is all that is needed for the milestone requirements in the middle of the week, but you should try to get as far as you can to make it even easier for yourself to finish the week, especially if you run into trouble.

*   Ask the user for the sales tax rate as a percentage (floating point). Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.
    
*   Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
    
*   Compute and display the total price of the meal by adding the subtotal and the sales tax.
    

Finally:

*   Ask the user for the the payment amount (floating point)
    
*   Compute and display the change.
    

A sample run of the program might look as follows:

    
    What is the price of a child's meal? 4.50
    What is the price of an adult's meal? 9.00
    How many children are there? 4
    How many adults are there? 2
    
    Subtotal: $36.00
    
    What is the sales tax rate? 6
    Sales Tax: $2.16
    Total: $38.16
    
    What is the payment amount? 40
    Change: $1.84
    
    

Another example, in which the user typed different values, might look like this:

    
    What is the price of a child's meal? 2.25
    What is the price of an adult's meal? 6.99
    How many children are there? 2
    How many adults are there? 1
    
    Subtotal: $11.49
    
    What is the sales tax rate? 4
    Sales Tax: $0.46
    Total: $11.95
    
    What is the payment amount? 20
    Change: $8.05
    
    

### Showing Creativity and Exceeding Requirements

For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage, or anything else you can think of. Play around with different ideas and see what you can learn!

**Important:** In order to receive credit for showing creativity, you must include a comment at the top of the program that describes in 1-2 sentences what you have added.

### Milestone Requirements

By midweek, to help make sure you are on track to finish the assignment, you need to complete the following:

1.  Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
    
2.  Ask the user for the number of adults and children and store these values properly into variables as integers.
    
3.  Compute and display the subtotal (you do not need to worry about the sales tax or rounding to two decimals at this point).
    

### Final requirements

At the end of the week, in addition to the milestone requirements above, you need to also complete the following:

1.  Ask the user for the sales tax rate and store the value properly as a floating point number.
    
2.  Compute and display the sales tax.
    
3.  Compute and display the total.
    
4.  Ask the user for the payment amount and store the value properly as a floating point number.
    
5.  Compute and display the change.
    
6.  Include the appropriate currency symbol (for example $, €, etc.) before each displayed value.
    
7.  Display each value to two decimals.
    
8.  Double check that the calculations are correct.
    
9.  Show creativity and exceed the core requirements by adding additional features.
    
10.  Use good style in your program, including variable names and whitespace.
