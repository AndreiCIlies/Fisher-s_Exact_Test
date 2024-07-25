# Fisher's Exact Test

![image](https://github.com/user-attachments/assets/3d42d8e5-b7d0-42a6-8361-1b3087284f95)

## Introduction
This application provides a calculator that computes the one-tailed and two-tailed p-values for the Fisher's Exact Test on any 2 x 2 contingency table.
It displays the p-values both using the implemented methods and the fisher_exact method from the Scipy Library in Python.

## Usage
* The user has to introduce the 4 values in the entries and press the button to see the p-values.
* The values can be introduced as many times as the user wants to use the calculator.
* The user can also change categories to visualize the contingency table for the wanted data.

![image](https://github.com/user-attachments/assets/da9c8cd6-9666-4fd0-a5a5-771d327c9dc1)


## Features
* Calculating both one-tailed and two-tailed p-values with four decimal places.
* Category editing for a easily visualisation of the data.
* Errors displayed in a messagebox in case user doesn't introduce all the values, integer values or values lower than or equal to 100.

## Contingency Table
A Contingency Table is a n x n table that displays data for one variable in rows and data for another variable in columns.
The relationship between two variables can be easily detected by evaluating the table cells where the two data sets overlap.
An example of such table is the following one:

![image](https://github.com/user-attachments/assets/0fb74a2d-45bc-43d0-b29c-82c0d5742a4e)

## Fisher's Exact Test
A Fisher's Exact Test is a statistical hypothesis test used to access the association between two binary variables in a contingency table.
It is particularly useful when:
* Working with low counts.
* Fewer than 80% of the categories have expected values of < 5.

## One-tailed test
For a one-tailed test, we want to take into account only those tables that are more extreme than the observed table (the input table), but only in one direction:
* If A <= B, then sum the probabilities of all tables that have the upper-left corner value lower than or equal to A, including the observed table.
* If A > B, then sum the probabilities of all tables that have the upper-left corner value greater than or equal to A, including the observed table.

## Two-tailed test
For a two-tailed test, we add together the probabilities of every table that has a probability lower than or equal to the probability of the observed table.

## Technologies used
* Python.
* Tkinter Library for the window, entries, labels, button and messagebox.
* Scipy Library for the fisher_exact method to display one-tailed and two-tailed p-values to see that the implemented methods calculate the p-values correct.
