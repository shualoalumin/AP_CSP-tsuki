# AP CSP Create Performance Task — Written Responses

---

## Row 1 – Program Purpose and Function

**Question:** Describe the overall purpose of the program. Identify the input and output demonstrated in the video.

The purpose of this program is to help users create strong, personalized passwords based on information meaningful to them — such as their name, a favorite word, and their age — rather than relying on a fully random sequence they cannot remember. The program takes three text inputs entered by the user (name, favorite thing, and age), as well as a button click specifying the desired password length (4 or 8 characters), and produces a randomized password displayed on a result screen as its output. The video demonstrates a user entering values into the three input fields, pressing the 4-character or 8-character button, and seeing the generated password appear on the output screen.

---

## Row 2 – Data Abstraction

**Question:** Identify the name of the list, what the data in the list represents, and describe what the two code segments do.

The list is named charList. It represents a collection of individual characters drawn from the user's three inputs — their name, favorite thing, and age — combined into a single pool of characters that can be used to build a password. The first code segment shows data being stored into the list: a for loop iterates over a combined string of all three inputs and uses appendItem to add each character one by one into charList. The second code segment shows the list being used: a second for loop fills the password to the desired length by randomly selecting an index from charList and appending that character to the password string. Together, these two segments demonstrate that charList both stores and actively fulfills the program's purpose of generating a personalized password.

---

## Row 3 – Managing Complexity

**Question:** Explain how the named list manages complexity in your program. Describe how the program would be written differently without using this list.

The list charList manages complexity by consolidating all possible password characters into a single collection that can be accessed with one variable, regardless of how many characters the user enters. Because the total number of characters depends entirely on what the user types at runtime — and this length cannot be known in advance — it is impossible to store every character using individual variables. Without charList, the program would need to predict the maximum number of characters a user could ever type across all three fields, declare a separate variable for each possible position (such as char1, char2, char3, and so on), and write individual lines of code to reference each one. This would make the program significantly more complex, unscalable, and nearly impossible to maintain. The list eliminates this problem by allowing the program to dynamically store and access any number of characters with a single structure.

---

## Row 4 – Procedural Abstraction

**Question:** Describe what the procedure does and explain how the parameter affects its functionality.

The procedure generate(length) produces a randomized password by reading the user's three text inputs, seeding the password with one random character from each input, then filling the remaining characters by randomly sampling from charList until the password reaches the target length. The procedure is called in two places: generate(4) when the user clicks the 4-character button, and generate(8) when the user clicks the 8-character button. The parameter length directly controls the behavior of the procedure — it determines how many total characters the final password will contain by setting the upper bound of the second for loop. Without the parameter, the procedure could only generate passwords of one fixed length and would need to be rewritten entirely for each different length, making it far less reusable and flexible.
