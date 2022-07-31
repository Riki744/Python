# Day26

# Python Code Challenges: Control Flow (Advanced)

### Challenges

## 1. In Range
<p>Let’s start the advanced challenge problems by testing if a number falls within a certain range. We will accept three parameters where the first parameter is the number we are testing, the second parameter is the lower bound and the third parameter is the upper bound of our range. These are the steps required:</p>

<ol type="1">
  <li>Define the function to accept three numbers as parameters</li>
  <li>Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound</li>
  <li>If this is true, return True, otherwise, return False</li>
</ol>

## 2. Same Name
<p>We need to write a program that checks different names and determines if they are equal. We need to accept two strings and compare them. Here are the steps:</p>

<ol type="1">
  <li>Define the function to accept two strings, your_name and my_name</li>
  <li>Test if the two strings are equal</li>
  <li>Return True if they are equal, otherwise return False</li>
</ol> 


## 3. Always False
<p>There are some situations that you normally want to avoid when programming using conditional statements. One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. Let’s create an example of a function that contains a contradiction. It will contain a few steps:</p>

<ol type="1">
  <li>Define the function to accept a single parameter called num</li>
  <li>Use a combination of <, > and and to create a contradiction in an if statement.</li>
  <li>If the condition is true, return True, otherwise return False. The trick here is that because we’ve written a contradiction, the condition should never be true, so we should expect to always return False</li>
</ol> 


## 4. Movie Review
<p>We want to create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating. Here are the steps needed:</p>

<ol type="1">
  <li>Define our function to accept a single number called rating</li>
  <li>If the rating is equal to or less than 5, return "Avoid at all costs!"</li>
  <li>If the rating was less than 9, return "This one was fun."</li>
  <li>If neither of the if statement conditions were met, return "Outstanding!"</li>
</ol>

## 5. Max number
<p>For the final challenge, we are going to select which number from three input values is the greatest using conditional statements. To do this, we need to check the different combinations of values to see which number is greater than the other two. Here is what we need to do:</p>

<ol type="1">
  <li>Define a function that has three input parameters, num1, num2, and num3</li>
  <li>Test if num1 is greater than the other two numbers If so, return num1</li>
  <li>Test if num2 is greater than the other two numbers If so, return num2 </li>
  <li>Test if num3 is greater than the other two numbers If so, return num3 </li>
  <li>If there was a tie between the two largest numbers, then return "It's a tie!"</li>
</ol>



