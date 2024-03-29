# Python Code Challenges: Lists

### Challenges

## 1. Append Size
<p>For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:</p>

<ol type="1">
  <li>Define the function to accept one parameter for our list</li>
  <li>Get the length of the list</li>
  <li>Append the length of the list to the end of the list</li>
  <li>Return the modified list</li>
</ol>

## 2. Append Sum
<p>Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:</p>

<ol type="1">
  <li>Define the function to accept one parameter for our list of numbers</li>
  <li>Add the last and second to last elements from our list together</li>
  <li>Append the calculated value to the end of our list. </li>
  <li>Repeat steps 2 and 3 two more times </li>
  <li>Return the modified list</li>
</ol> 


## 3. Larger List
<p>Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:</p>

<ol type="1">
  <li>Define the function to accept two parameters for our two lists of numbers</li>
  <li>Check if the length of the first list is greater than or equal to the length of the second list</li>
  <li>If true, then return the last element from the first list. Otherwise, return the last element from the second list</li>
</ol> 


## 4. More Than N
<p>Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:</p>

<ol type="1">
  <li>Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances</li>
  <li>Count the number of occurrences of item (the second parameter) in lst (the first parameter)</li>
  <li>If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False</li>
</ol>

## 5. Combine Sort
<p>Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:</p>

<ol type="1">
  <li>Define the function to accept two parameters, one for each list. </li>
  <li>Combine the two lists together</li>
  <li>Sort the result </li>
  <li>Return the sorted and combined list</li>
</ol>
