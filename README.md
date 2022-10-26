Authors: Mathias Boddicker, Kylie Hall, Caleb Jenkins, Liam Zalubas

Date:10/25/22

Project:
Program 1) Random Number Generator -> already done for you and attached.
publishes 2 random numbers every 1 second on the topic "/random_numbers"
example message -> {"type":"random_number", "num1":12.323, "num2":34.232, "timestamp":"some timestamp"}

Program 2) Calculation Setup
This program will ask for user input as to whether they want to the system to perform addition or subtraction
Ask the user to input either a "+" for addition or a "-" for subtraction
Once the user input is received, the program will publish the selection over the topic "/calculation/setup"
This format can be in any format you wish to use
The program should continue asking the user for input as it should be able to change at any point in time
example message -> {"type":"setup", "setup":"+"} or {"type":"setup", "setup":"-"} 

Program 3) Calculation 
This program will receive data on the topics "/random_numbers" and "/calculation/setup"
The program will use the input from "Calculation Setup" to tell it whether to perform addition("+") or subtraction("-")
The program will use the random number data to calculate either the addition or subtraction of "num1" and "num2"
Once the calculation is complete, the program will publish the result on topic "/calculated/add" for "+" or "/calculated/subtract" for "-"
example message {"type":"calculation","setup":"+","result":43.3453}

Program 4) Results Client
This program will subscribe to the topic "calculated/#"
The program shall print out all received data
